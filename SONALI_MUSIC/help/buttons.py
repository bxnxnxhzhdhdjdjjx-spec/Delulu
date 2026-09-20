from pyrogram.types import InlineKeyboardButton
import config


class BUTTONS(object):
    BBUTTON = [
        [
            InlineKeyboardButton("ᴄʜᴧᴛ-ɢᴘᴛ", callback_data="TOOL_BACK HELP_01"),
            InlineKeyboardButton("ᴧᴄᴛɪση", callback_data="TOOL_BACK HELP_14"),
            InlineKeyboardButton("ᴄσᴜᴘʟєs", callback_data="TOOL_BACK HELP_08"),
        ],
        [
            InlineKeyboardButton("sєᴧʀᴄʜ", callback_data="TOOL_BACK HELP_02"),
            InlineKeyboardButton("ᴛʀᴧηsʟᴧᴛє", callback_data="TOOL_BACK HELP_24"),
            InlineKeyboardButton("ɪηғσ", callback_data="TOOL_BACK HELP_04"),
        ],
        [
            InlineKeyboardButton("ғσηᴛ", callback_data="TOOL_BACK HELP_05"),
            InlineKeyboardButton("ᴡʜɪsᴘєʀ", callback_data="TOOL_BACK HELP_03"),
            InlineKeyboardButton("ᴛᴧɢᴧʟʟ", callback_data="TOOL_BACK HELP_07"),
        ],
        [
            InlineKeyboardButton("ғυη", callback_data="TOOL_BACK HELP_11"),
            InlineKeyboardButton("ǫυσᴛʟʏ", callback_data="TOOL_BACK HELP_12"),
            InlineKeyboardButton("Ⓣ-ɢʀᴧᴘʜ", callback_data="TOOL_BACK HELP_26"),
        ],
        [
            InlineKeyboardButton("ɢᴧϻє", callback_data="TOOL_BACK HELP_21"),
            InlineKeyboardButton("sєᴛᴜᴘ", callback_data="TOOL_BACK HELP_17"),
            InlineKeyboardButton("sᴧηɢϻᴧᴛᴧ", callback_data="TOOL_BACK HELP_23"),
        ],
        [
            InlineKeyboardButton("ɢɪᴛʜᴜʙ", callback_data="TOOL_BACK HELP_25"),
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"MAIN_CP"),
            InlineKeyboardButton("sᴛɪᴄᴋєʀs", callback_data="TOOL_BACK HELP_10"),
        ]
    ]

    ALPHABUTTON = [
        [
            InlineKeyboardButton("ᴧɪ | ᴄʜᴧᴛɢᴘᴛ", callback_data="TOOL_BACK HELP_01"),
        ],
        [
            InlineKeyboardButton("sєᴧʀᴄʜ", callback_data="TOOL_BACK HELP_02"),
            InlineKeyboardButton("ᴛᴛs", callback_data="TOOL_BACK HELP_03"),
            InlineKeyboardButton("ɪηғσ", callback_data="TOOL_BACK HELP_04"),
        ],
        [
            InlineKeyboardButton("ғσηᴛ", callback_data="TOOL_BACK HELP_05"),
            InlineKeyboardButton("ϻᴧᴛʜ", callback_data="TOOL_BACK HELP_06"),
            InlineKeyboardButton("ᴛᴧɢᴧʟʟ", callback_data="TOOL_BACK HELP_07"),
        ],
        [
            InlineKeyboardButton("ɪϻᴧɢє", callback_data="TOOL_BACK HELP_08"),
            InlineKeyboardButton("ʜᴧsᴛᴧɢ", callback_data="TOOL_BACK HELP_09"),
            InlineKeyboardButton("sᴛɪᴄᴋєʀs", callback_data="TOOL_BACK HELP_10"),
        ],
        [
            InlineKeyboardButton("ғυη", callback_data="TOOL_BACK HELP_11"),
            InlineKeyboardButton("ǫυσᴛʟʏ", callback_data="TOOL_BACK HELP_12"),
            InlineKeyboardButton("ᴛ-ᴅ", callback_data="TOOL_BACK HELP_13"),
        ],
        [   
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"MAIN_CP"),
        ]
    ]

    MBUTTON = [
        [
            InlineKeyboardButton("єxᴛʀᴧ", callback_data="MANAGEMENT_BACK HELP_25"),
        ],
        [
            InlineKeyboardButton("ʙᴧη", callback_data="MANAGEMENT_BACK HELP_14"),
            InlineKeyboardButton("ᴋɪᴄᴋ", callback_data="MANAGEMENT_BACK HELP_15"),
            InlineKeyboardButton("ϻυᴛє", callback_data="MANAGEMENT_BACK HELP_16"),
        ],
        [
            InlineKeyboardButton("ᴘɪη", callback_data="MANAGEMENT_BACK HELP_17"),
            InlineKeyboardButton("sᴛᴧғғ", callback_data="MANAGEMENT_BACK HELP_18"),
            InlineKeyboardButton("sєᴛ-υᴘ", callback_data="MANAGEMENT_BACK HELP_19"),
        ],
        [
            InlineKeyboardButton("ᴢσϻʙɪє", callback_data="MANAGEMENT_BACK HELP_20"),
            InlineKeyboardButton("ɢᴧϻє", callback_data="MANAGEMENT_BACK HELP_21"),
            InlineKeyboardButton("ɪϻᴘσsᴛєʀ", callback_data="MANAGEMENT_BACK HELP_22"),
        ],
        [
            InlineKeyboardButton("sɢ", callback_data="MANAGEMENT_BACK HELP_23"),
            InlineKeyboardButton("ᴛʀ", callback_data="MANAGEMENT_BACK HELP_24"),
            InlineKeyboardButton("ɢʀᴧᴘʜ", callback_data="MANAGEMENT_BACK HELP_26"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"MAIN_CP"), 
        ]
    ]

    @property
    def PBUTTON(self):
        owner = config.OWNER_USERNAME.lstrip("@") if getattr(config, "OWNER_USERNAME", None) else ""
        owner_url = f"https://t.me/{owner}" if owner else config.SUPPORT_CHAT
        return [
            [
                InlineKeyboardButton("ㅤ- 𝑶𝑾𝑵𝑬𝑅 ! ", url=owner_url)
            ],
            [
                InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data="MAIN_CP"),
            ]
        ]

    @property
    def ABUTTON(self):
        return [
            [
                InlineKeyboardButton("⌯ sυᴘᴘσʀᴛ ⌯", url=config.SUPPORT_CHAT),
                InlineKeyboardButton("⌯ υᴘᴅᴧᴛєs ⌯", url=config.SUPPORT_CHANNEL),
            ],
            [
                InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data="settingsback_helper"),
            ]
        ]

    SBUTTON = [
        [
            InlineKeyboardButton("⌯ ϻᴜѕɪᴄ ⌯", callback_data="settings_back_helper"),
            InlineKeyboardButton("⌯ ϻᴧηᴧɢєϻєηᴛ ⌯", callback_data="TOOL_CP"),
        ],
        [
            InlineKeyboardButton("ᴧʟʟ ʙσᴛ's", callback_data="MAIN_BACK HELP_ABOUT"),
            InlineKeyboardButton("⌯ ᴘʀσϻσᴛɪση ⌯", callback_data="PROMOTION_CP"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
        ]
    ]
