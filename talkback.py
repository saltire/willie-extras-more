"""
talkback.py - Willie Talkback Module
Author: saltire sable
About: http://willie.dftba.net
"""

import itertools
import random
import re


def configure(config):
    """
    | [talkback] | example | purpose |
    | ---------- | ------- | ------- |
    | file       | /home/user/.willie/replies.txt | File containing regexes and replies. |
    """

    q = '\n'.join((
        'You can specify a file containing expressions that the bot will respond to in chat.',
        'The file should contain stanzas consisting of a regular expression on one line,',
        'and at least one (randomly chosen) response on the following line(s),',
        'with blank lines separating each stanza.\n'))
    config.interactive_add('talkback', 'file', q + 'File to use for automatic chat replies')


def setup(bot):
    if bot.config.has_option('talkback', 'file') and bot.config.talkback.file:
        replies = import_from_file(bot.config.talkback.file)

    else:
        replies = {r'PING!': 'PONG!',
                   r'(hi|hello|hey),? $nickname': ('Hi, $trigger!',
                                                   'Greetings, $trigger!'),
                   r'(fuck|screw) you,? $nickname': '$1 you, $trigger!',
                   }

    # set the rule property for the replace function, as if it was given a @rule decorator
    replace.rule = [pattern for pattern in replies]

    # run the patterns through the same substitution function that the @rule decorator uses
    bot.memory['replies'] = dict((bot.sub(pattern), reply) for pattern, reply in replies.items())


def import_from_file(path):
    """Import expressions and responses from a text file.
    Expressions should be on one line, followed by a list of possible responses
    each on their own line, and then a blank line before the next expression."""
    with open(path) as tfile:
        lines = [line.strip() for line in tfile.readlines() if line[0] != '#']

        # split the list of lines into groups, separated by blank lines
        groups = [list(g) for k, g in itertools.groupby(lines, lambda v: v != '') if k]

    return dict((group[0], group[1:]) for group in groups)


def replace(bot, trigger):
    """Replace the triggering expression with a response from the text file.
    If the expression has more than one possible response, pick one at random."""
    reply = bot.memory['replies'][trigger.match.re.pattern]

    # if the reply is a list, pick a random string from the list
    if not isinstance(reply, basestring):
        reply = random.choice(reply)

    # replace $trigger with the triggering user's nick
    reply = reply.replace('$trigger', trigger.nick)

    # replace numbered wildcards in reply with matching group from pattern
    reply = re.sub(r'\$(\d+)', lambda m: trigger.group(int(m.group(1))), reply)

    bot.say(reply)


