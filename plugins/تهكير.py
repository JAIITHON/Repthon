# Repthon - UserBot
# Copyright (C) 2020 RepthonTeam
#
# This file is a part of < https://github.com/rogerpq/Repthon/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/rogerpq/Repthon/blob/main/LICENSE/>.

"""
✘ Commands Available
• `{i}تهكير`
    Do a Prank With Replied user.
"""

import asyncio
import random

from . import *

from plugins import ultroid_cmd


@ultroid_cmd(pattern="تهكير")
async def _(event):

    animation_interval = 0.7
    animation_ttl = range(0, 11)
    xx = await event.eor("جار بدء تهكير المستخذم😈")
    animation_chars = [
        "`جار الرفع إلى سيرفر التهكير`",
        "`تم الرفع`",
        "`Installing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`lnstallig... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 84%\n█████████████████████▒▒▒▒ `",
        "`Installing... 100%\n████████تم التهكير██████████ `",
        "`تم التهكير بنجاح😂😉`",
    ]
