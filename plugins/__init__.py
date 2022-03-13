# Rawana - UserBot
# Copyright (C) 2021-2022 TeamRawana
#
# This file is a part of < https://github.com/Rawana-Developers/Rawana-User-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Rawana-Developers/Rawana-User-Bot/blob/main/LICENSE/>.


import asyncio
import os
import time
from random import choice

from pyRawana import *
from pyRawana.dB import DEVLIST, RAWANA_IMAGES
from pyRawana.functions.helper import *
from pyRawana.functions.info import *
from pyRawana.functions.misc import *
from pyRawana.functions.tools import *
from pyRawana.misc._assistant import asst_cmd, callback, in_pattern
from pyRawana.misc._decorators import ultroid_cmd
from pyRawana.misc._wrappers import eod, eor
from pyRawana.version import __version__, Rawana_version
from telethon import Button, events
from telethon.tl import functions, types

from strings import get_string

Redis = udB.get_key
con = TgConverter
OWNER_NAME = Rawana_bot.full_name
OWNER_ID = Rawana_bot.uid

LOG_CHANNEL = udB.get_key("LOG_CHANNEL")

INLINE_PIC = udB.get_key("INLINE_PIC")

if INLINE_PIC is None:
    INLINE_PIC = choice(RAWANA_IMAGES)
elif INLINE_PIC == False:
    INLINE_PIC = None

Telegraph = telegraph_client()

List = []
Dict = {}
N = 0

STUFF = {}

# Chats, which needs to be ignore for some cases
# Considerably, there can be many
# Feel Free to Add Any other...

NOSPAM_CHAT = [
    -1001327032795,  # RawanaSupport
    -1001387666944,  # PyrogramChat
    -1001109500936,  # TelethonChat
    -1001050982793,  # Python
    -1001256902287,  # DurovsChat
]

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]

ATRA_COL = [
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "Cyan",
    "LightSkyBlue",
    "Turquoise",
    "MediumVioletRed",
    "Aquamarine",
    "Lightcyan",
    "Azure",
    "Moccasin",
    "PowderBlue",
]
