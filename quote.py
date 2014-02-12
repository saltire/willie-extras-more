"""
quote.py - Willie Quote Module
Author: saltire sable
About: http://willie.dftba.net
"""

# TODO: Implement the quote feature from the "bucket" module in willie-extras
# in a standalone module.

from collections import deque
import random
import re

from willie.module import commands, priority, rule, thread
from willie.config import ConfigurationError


def setup(bot):
    bot.memory['nickmem'] = {}

    if not bot.db:
        raise ConfigurationError("Database not set up, or unavailable.")
    conn = bot.db.connect()
    c = conn.cursor()

    try:
        c.execute('SELECT * FROM quotes')
    except StandardError:
        c.execute('''CREATE TABLE IF NOT EXISTS quotes (
            channel TEXT,
            nick TEXT,
            quote TEXT
            )''')
        conn.commit()

    conn.close()


def normalize(text):
    return re.sub('[^\w\s-]', '', text.lower())


@thread(False)
@commands('remember')
def save_quote(bot, trigger):
    """Save the last message from a user, or the last one containing a given word."""
    nick = trigger.group(3)
    word = trigger.group(4)
    nickmem = bot.memory['nickmem'].get(trigger.sender, {}).get(nick, [])

    try:
        quote = next(msg for msg in nickmem if
                     not word or normalize(word) in normalize(msg).split())

        sub = bot.db.substitution
        conn = bot.db.connect()
        c = conn.cursor()
        c.execute('INSERT INTO quotes VALUES ({0},{0},{0})'.format(sub),
                  (trigger.sender, nick, quote))
        conn.commit()
        conn.close()

        bot.reply("Remembered {0} saying: {1}".format(nick, quote))

    except StopIteration:
        bot.reply("Sorry, I don't remember what {0} said about '{1}'.".format(nick, word)
                  if word else "Sorry, I don't remember anything {0} said.".format(nick))


@thread(False)
@commands('quote')
def read_quote(bot, trigger):
    """Read out a random quote from a user, or look for one containing a given word."""
    nick = trigger.group(3)
    word = trigger.group(4)

    sub = bot.db.substitution
    conn = bot.db.connect()
    c = conn.cursor()
    c.execute('SELECT quote FROM quotes WHERE channel = {0} AND nick = {0}'.format(sub),
              (trigger.sender, nick))
    nickquotes = c.fetchall()

    try:
        quote = random.choice([msg[0] for msg in reversed(nickquotes) if
                               not word or normalize(word) in normalize(msg[0]).split()])
        bot.say("<{0}> {1}".format(nick, quote))

    except IndexError:
        bot.reply("Sorry, I don't remember what {0} said about '{1}'.".format(nick, word)
                  if word else "Sorry, I don't have any quotes from {0}.".format(nick))


@priority('low')
@thread(False)
@rule('(.*)')
def remember_lines(bot, trigger):
    """Remember the last 10 messages from each user."""
    nickmem = bot.memory['nickmem'].setdefault(trigger.sender, {}).setdefault(trigger.nick, deque())
    nickmem.appendleft(trigger.group(1))
    if len(nickmem) > 10:
        nickmem.pop()
