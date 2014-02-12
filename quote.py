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


def setup(bot):
    bot.memory['nickmem'] = {}
    bot.memory['nickquotes'] = {}


def normalize(text):
    return re.sub('[^\w\s-]', '', text.lower())


@thread(False)
@commands('remember')
def save_quote(bot, trigger):
    """Given a user's nick, save the last message from that user.
    If a word is specified, look for the last message containing that word."""
    nick = trigger.group(3)
    word = trigger.group(4)
    nickmem = bot.memory['nickmem'].get(trigger.sender, {}).get(nick, [])

    try:
        quote = next(msg for msg in nickmem if
                     not word or normalize(word) in normalize(msg).split())
        bot.memory['nickquotes'].setdefault(trigger.sender, {}).setdefault(nick, []).append(quote)
        bot.reply("Remembered {0} saying: {1}".format(nick, quote))

    except StopIteration:
        bot.reply("Sorry, I don't remember what {0} said about '{1}'.".format(nick, word)
                  if word else "Sorry, I don't remember anything {0} said.".format(nick))


@thread(False)
@commands('quote')
def read_quote(bot, trigger):
    """Given a user's nick, read out a random quote from that user.
    If a word is specified, read out the last quote containing that word."""
    nick = trigger.group(3)
    word = trigger.group(4)
    nickquotes = bot.memory['nickquotes'].get(trigger.sender, {}).get(nick, [])

    try:
        quote = random.choice([msg for msg in reversed(nickquotes) if
                               not word or normalize(word) in normalize(msg).split()])
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
