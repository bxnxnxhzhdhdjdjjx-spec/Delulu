from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI_MUSIC import app
import config


@app.on_message(filters.command("repo"))
async def start(_, msg):
    owner = config.OWNER_USERNAME.lstrip("@") if config.OWNER_USERNAME else ""
    owner_link = f"https://t.me/{owner}" if owner else config.SUPPORT_CHAT
    bot_user = config.BOT_USERNAME.lstrip("@") if config.BOT_USERNAME else app.username

    start_txt = f"""**
<u>❃ ᴡєʟᴄσϻє ᴛᴏ ʀєᴘσ ❃</u>
 
✼ ʀєᴘᴏ ɪs ηᴏᴡ ᴧᴠᴧɪʟᴧʙʟє ʙᴧʙʏ 😌
 
❉ ʏᴏᴜ ᴄᴧη ᴄʜєᴄᴋ σᴜʀ ʀєᴘσ, sυᴘᴘσʀᴛ ᴄʜᴧᴛ & ᴄʜᴧηηєʟ !!

✼ || [˹ ɴᴇᴛᴡᴏʀᴋ ˼ 💞]({config.SUPPORT_CHANNEL}) ||
 
❊ ʀᴜη 24x7 ʟᴧɢ ϝʀєє ᴡɪᴛʜσᴜᴛ sᴛσᴘ**
"""

    buttons = [
        [ 
          InlineKeyboardButton("✙ ᴧᴅᴅ ϻє вᴧʙʏ ✙", url=f"https://t.me/{bot_user}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ɴєᴛᴡᴏʀᴋ •", url=config.SUPPORT_CHANNEL),
          InlineKeyboardButton("• 𝛅ᴜᴘᴘσʀᴛ •", url=config.SUPPORT_CHAT),
        ],
        [
          InlineKeyboardButton("• ʀєᴘσ •", url=config.UPSTREAM_REPO),
          InlineKeyboardButton("• σᴡηєʀ •", url=owner_link),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo=config.REPO_IMG_URL,
        caption=start_txt,
        reply_markup=reply_markup
    )
