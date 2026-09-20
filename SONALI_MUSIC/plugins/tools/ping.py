from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
import config
from SONALI_MUSIC import app
from SONALI_MUSIC.core.call import Sona
from SONALI_MUSIC.utils import bot_sys_stats
from SONALI_MUSIC.utils.decorators.language import language
from SONALI_MUSIC.utils.inline import supp_markup
from config import BANNED_USERS


@app.on_message(filters.command("ping", prefixes=["/", "!"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    ping_media = getattr(config, "PING_IMG_URL", "https://litter.catbox.moe/xyedznhk80hmial2.mp4")

    if ping_media.endswith(".mp4") or ping_media.endswith(".webm") or ping_media.endswith(".mkv"):
        response = await message.reply_video(
            video=ping_media,
            caption=_["ping_1"].format(app.mention),
        )
    else:
        response = await message.reply_photo(
            photo=ping_media,
            caption=_["ping_1"].format(app.mention),
        )

    pytgping = await Sona.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
