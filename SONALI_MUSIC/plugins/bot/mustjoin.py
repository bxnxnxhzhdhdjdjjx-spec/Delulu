from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
import config
from SONALI_MUSIC import app

#--------------------------

#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    must_join = getattr(config, "MUST_JOIN", None)
    if not must_join:
        return
    try:
        try:
            await app.get_chat_member(must_join, msg.from_user.id)
        except UserNotParticipant:
            if must_join.startswith("http://") or must_join.startswith("https://"):
                link = must_join
            elif must_join.isalpha() or must_join.isalnum() or must_join.startswith("@"):
                clean_username = must_join.lstrip("@")
                link = f"https://t.me/{clean_username}"
            else:
                chat_info = await app.get_chat(must_join)
                link = chat_info.invite_link
            try:
                channel_btn = config.SUPPORT_CHANNEL if config.SUPPORT_CHANNEL else link
                chat_btn = config.SUPPORT_CHAT if config.SUPPORT_CHAT else link
                img_photo = getattr(config, "MUST_JOIN_IMG", "https://files.catbox.moe/fu6jk3.jpg")
                await msg.reply_photo(
                    photo=img_photo,
                    caption=f"๏ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ [๏ sᴜᴘᴘᴏʀᴛ ๏]({link}) ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴄʜᴇᴀᴋ ᴍʏ ғᴇᴀᴛᴜʀᴇs.\n\nᴀғᴛᴇʀ ᴊᴏɪɴ ᴛʜᴇ [๏ ᴄʜᴀɴɴᴇʟ ๏]({link}) ᴄᴏᴍᴇ ʙᴀᴄᴋ ᴛᴏ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴛʏᴘᴇ /start ᴀɢᴀɪɴ !! ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("• sᴜᴘᴘᴏʀᴛ •", url=chat_btn),
                                InlineKeyboardButton("• ᴄʜᴀɴɴᴇʟ •", url=channel_btn),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_ᴊᴏɪɴ ᴄʜᴀᴛ ๏: {must_join} !")
