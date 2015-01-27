# -*- coding: utf-8
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
                    ],
         'Orc': [['Akoth', 'Amug', 'Ashgam', 'Azdush', 'Bagabug', 'Barfa', 'Blorg', 'Borgu', 'Brogg', 'Bûbol', 'Buth', 'Dûgza', 'Dûsh', 'Feldush', 'Flak', 'Fûlgum', 'Ghâm', 'Ghûra', 'Gimub', 'Glûk', 'Golm', 'Gorfel', 'Gorgûm', 'Goroth', 'Grublik', 'Gûndza', 'Horhog', 'Hork', 'Horza', 'Hoshû', 'Humgrat', 'Hûra', 'Ishgha', 'Ishmoz', 'Kâka', 'Kothûg', 'Krimp', 'Kruk', 'Kugaluga', 'Lamlûg', 'Latbag', 'Lorm', 'Lûga', 'Lûgdash', 'Lûgnak', 'Máku', 'Malmûg', 'Mogg', 'Mormog', 'Mozfel', 'Muggrish', 'Mûglûk', 'Muzglob', 'Nákra', 'Nazdûg', 'Názkûga', 'Nazû', 'Norsko', 'Norûk', 'Ogthrak', 'Olgoth', 'Olrok', 'Orthog', 'Paash', 'Pigug', 'Prák', 'Pug', 'Pûgrish', 'Pushkrimp', 'Ratanak', 'Ratbag', 'Ratlûg', 'Ronk', 'Rûg', 'Rûkdûg', 'Shágflak', 'Shaká', 'Skak', 'Skûn', 'Snagog', 'Takra', 'Tarz', 'Thakrak', 'Thrak', 'Torz', 'Tûgog', 'Tûkâ', 'Tûmhom', 'Ugakuga', 'Ûggû', 'Ûkbûk', 'Ûkrom', 'Ukshak', 'Ushbaka', 'Ushgol', 'Uthûg', 'Zaathra', 'Zog', 'Zogdûsh', 'Zûgor', 'Zûmug', 'Zunn'],
                 ['Archer Trainer', 'Ash-Skin', 'Bag-Head', 'Barrel-Scraper', 'Beast Slayer', 'Black-Blade', 'Blade Master', 'Blade Sharpener', 'Blood-Lover', 'Bone-Licker', 'Bone-Ripper', 'Brawler', 'Cannibal', 'Caragor Slayer', 'Cave Rat', 'Corpse-Eater', 'Death-Blade', 'Deathbringer', 'Drooler', 'Elf-Slayer', 'Evil Eye', 'Fat Head', 'Fire-Brander', 'Flesh-Render', 'Foul-Spawn', 'Frog-Blood', 'Ghûl Slayer', 'Graug Catcher', 'Grog-Burner', 'Halfling-Lover', 'Head-Chopper', 'Head-Hunter', 'Heart-Eater', 'Horn Blower', 'Hot Tongs', 'Jaws', 'Learned Scribe', 'Life-Drinker', 'Limp-Leg', 'Literate One', 'Long-Tooth', 'Lucky Shot', 'Mad-Eye', 'Maggot-Nest', 'Man-Stalker', 'Meat Hooks', 'Metal-Beard', 'Night-Bringer', 'of Lithlad', 'of the Spiders', 'One-Eye', 'Pit Fighter', 'Plague-Bringer', 'Pot-Licker', 'Quick-Blades', 'Rabble Rouser', 'Raid Leader', 'Ranger-Killer', 'Ravager', 'Sawbones', 'Scar-Artist', 'Shaman', 'Shield Master', 'Skull Bow', 'Skull-Cracker', 'Slashface', 'Slave Taskmaster', 'Storm-Bringer', 'Sword Master', 'the Advisor', 'the Assassin', 'the Beheader', 'the Bitter', 'the Black', 'the Bleeder', 'the Bloated', 'the Bone Collector', 'the Bowmaster', 'the Brander', 'the Brave', 'the Brewer', 'the Brown', 'the Choker', 'the Chunky', 'the Claw', 'the Clever', 'the Cook', 'the Corruptor', 'the Coward', 'the Crazy', 'the Dark', 'the Defender', 'the Defiler', 'the Destroyer', 'the Devourer', 'the Diseased', 'the Disgusting', 'the Drunk', 'the Endless', 'the Fanatical', 'the Flesh Glutton', 'the Fool', 'the Friendly', 'the Gentle', 'the Gorger', 'the Grinder', 'the Hacker', 'the Handsome', 'the Humiliator', 'the Hungry', 'the Immovable', 'the Infernal', 'the Judge', 'the Killer', 'the Kin-Slayer', 'the Knife', 'the Legend', 'the Loaded', 'the Lookout', 'the Mad', 'the Man-Eater', 'the Meat Hoarder', 'the Merciful', 'the Messenger', 'the Mindless', 'the Mountain', 'the Other Twin', 'the Poet', 'the Proud', 'the Puny', 'the Rash', 'the Raven', 'the Red', 'the Runious', 'the Runner', 'the Runt', 'the Savage', 'the Scholar', 'the Screamer', 'the Serpent', 'the Shadow', 'the Shield', 'the Skinless', 'the Slasher', 'the Slaughterer', 'the Small', 'the Smasher', 'the Spike', 'the Stout', 'the Surgeon', 'the Swift', 'the Tongue', 'the Twin', 'the Unkillable', 'the Vile', 'the Wanderer', 'the Watcher', 'the Whiner', 'the Wise', 'the Wrestler', 'Thin Bones', 'Thunderhead', 'Tree-Killer', 'Troll Slayer', 'Troll-Born', 'Ugly Face', 'Who Flees']
                 ],
         }

@commands('name')
def generate_name(bot, trigger):
    """From the list specified, construct a name and reply with it."""
    for ntype, parts in names.iteritems():
        if trigger.group(2).lower() == ntype.lower():
            name = ' '.join(random.choice(plist) for plist in parts)
            bot.reply('Your {0} name is: {1}'.format(ntype, name))
