"""
name.py - Willie Name Generator
Author: saltire sable
About: http://willie.dftba.net
"""

import random

from willie.module import commands


names = {'Diablo': [['Gloom', 'Gray', 'Dire', 'Black', 'Shadow', 'Haze', 'Wind', 'Storm', 'Warp', 'Night', 'Moon', 'Star', 'Pit', 'Fire', 'Cold', 'Seethe', 'Sharp', 'Ash', 'Blade', 'Steel', 'Stone', 'Rust', 'Mold', 'Blight', 'Plague', 'Rot', 'Ooze', 'Puke', 'Snot', 'Bile', 'Blood', 'Pulse', 'Gut', 'Gore', 'Flesh', 'Bone', 'Spine', 'Mind', 'Spirit', 'Soul', 'Wrath', 'Grief', 'Foul', 'Vile', 'Sin', 'Chaos', 'Dread', 'Doom', 'Bane', 'Death', 'Viper', 'Dragon', 'Devil', 'Pox', 'Fester', 'Blister', 'Pus', 'Slime', 'Drool', 'Froth', 'Sludge', 'Venom', 'Poison', 'Break', 'Shard', 'Flame', 'Maul', 'Thirst', 'Lust'],
                    ['Touch', 'Spell', 'Feast', 'Wound', 'Grin', 'Maim', 'Hack', 'Bite', 'Rend', 'Burn', 'Rip', 'Kill', 'Call', 'Vex', 'Jade', 'Web', 'Shield', 'Killer', 'Razor', 'Drinker', 'Shifter', 'Crawler', 'Dancer', 'Bender', 'Weaver', 'Eater', 'Widow', 'Maggot', 'Spawn', 'Wight', 'Grumble', 'Growler', 'Snarl', 'Wolf', 'Crow', 'Hawk', 'Cloud', 'Bang', 'Head', 'Skull', 'Brow', 'Eye', 'Maw', 'Tongue', 'Fang', 'Horn', 'Thorn', 'Claw', 'Fist', 'Heart', 'Shank', 'Skin', 'Wing'],
                    ['the Hammer', 'the Axe', 'the Sharp', 'the Jagged', 'the Flayer', 'the Slasher', 'the Impaler', 'the Hunter', 'the Slayer', 'the Mauler', 'the Destroyer', 'the Quick', 'the Witch', 'the Mad', 'the Wraith', 'the Shade', 'the Dead', 'the Unholy', 'the Howler', 'the Grim', 'the Dark', 'the Tainted', 'the Unclean', 'the Hungry', 'the Cold'],
                    ]
         }

@commands('name')
def generate_name(bot, trigger):
    """From the list specified, construct a name and reply with it."""
    for ntype, parts in names.iteritems():
        if trigger.group(2).lower() == ntype.lower():
            name = ' '.join(random.choice(plist) for plist in parts)
            bot.reply('Your {0} name is: {1}'.format(ntype, name))
