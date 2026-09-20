import config


class HelperMeta(type):
    @property
    def HELP_M(cls):
        return '''```
❖ ᴄʜσσsє ᴛʜє ᴄᴧᴛєɢσʀʏ ғσʀ ᴡʜɪᴄʜ ʏσυ ᴡᴧηηᴧ ɢєᴛ ʜєʟᴩ```
**ᴧsᴋ ʏσυʀ ᴅσυʙᴛs ᴧᴛ sυᴘᴘσʀᴛ ᴄʜᴧᴛ ᴧʟʟ ᴄσϻϻᴧηᴅs ᴄᴧη ʙє υsєᴅ ᴡɪᴛʜ : /**
'''

    @property
    def HELP_B(cls):
        return '''```
❖ ᴄʜσσsє ᴛʜє ᴄᴧᴛєɢσʀʏ ғσʀ ᴡʜɪᴄʜ ʏσυ ᴡᴧηηᴧ ɢєᴛ ʜєʟᴩ```
**ᴧsᴋ ʏσυʀ ᴅσυʙᴛs ᴧᴛ sυᴘᴘσʀᴛ ᴄʜᴧᴛ ᴧʟʟ ᴄσϻϻᴧηᴅs ᴄᴧη ʙє υsєᴅ ᴡɪᴛʜ : /**
'''

    @property
    def HELP_Sona(cls):
        return '''```
❖ ʜєʟᴘ ϻᴧɪη ϻєηυ```
**❖ ᴄʜσσsє ᴛʜє ᴄᴧᴛєɢσʀʏ ғσʀ ᴡʜɪᴄʜ ʏσυ ᴡᴧηηᴧ ɢєᴛ ʜєʟᴩ**
'''

    @property
    def HELP_01(cls):
        return f'''```
❖ ᴄʜᴧᴛɢᴘᴛ ᴄσϻϻᴧηᴅꜱ ❖```
**❖ ᴧɪ|ᴄʜᴧᴛɢᴘᴛ ᴄσϻϻᴧηᴅs

❍ /ask [ǫυєʀʏ] : sєᴧʀᴄʜ ᴛʜє ᴧηʏ ᴛʏᴘє ǫυєsᴛɪση

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_02(cls):
        return f'''```
❖ sєᴧʀᴄʜ ᴄσϻϻᴧηᴅꜱ ❖```
**❍ /google [ǫυєʀʏ] : sєᴧʀᴄʜ ᴛʜє ɢσσɢʟє ғσʀ ᴛʜє ɢɪᴠєη ǫυєʀʏ
❍ /waifu [ǫυєʀʏ] : sєᴧʀᴄʜ ʀᴀɴᴅᴏᴍ ᴡᴧɪғᴜ ғσʀ ᴛʜє ɢɪᴠєη ǫυєʀʏ
❍ /bored [ǫυєʀʏ] : ᴛɪϻєᴅ σᴜᴛ ʙᴏʀɪηɢ ϻσσᴅs ғσʀ ᴛʜє ɢɪᴠєη ǫυєʀʏ
❍ /image [ǫυєʀʏ] : ɢєᴛ ᴛʜє ɪϻᴧɢєs ʀєɢᴧʀᴅɪηɢ ᴛσ ʏσυʀ ǫυєʀʏ
❍ /math [ǫυєʀʏ] : ɢєᴛ sσʟᴠєᴅ ϻᴧᴛʜ ǫᴜєsᴛɪσηs.** `єx - 2 + 2`

```
❖ єxᴧϻᴘʟє : /google ʜɪɴᴅɪ sᴏɴɢs```

**❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_03(cls):
        return f'''```
❖ ᴡʜɪsᴘᴇʀ ❖```
**❖ sᴇɴᴅ ᴡʜɪsᴘᴇʀ ᴍᴇssᴀɢᴇ ❖**

```
 єxᴧϻᴘʟє : @Xbroze I love You 😘
```

<u>**❖ ᴛєxᴛ ᴛσ ᴠσɪᴄє**</u>

**❍ /tts : [ᴛєxᴛ]

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL}) **
'''

    @property
    def HELP_04(cls):
        return f'''```
❖ ɪηꜰσ ᴄσϻϻᴧηᴅꜱ ❖```
**❍ /id : ɢєᴛ ᴛʜє ᴄυʀʀєηᴛ ɢʀσυᴘ ɪᴅ. ɪғ υsєᴅ ʙʏ ʀєᴘʟʏɪηɢ ᴛσ ᴧ ϻєssᴧɢє, ɢєᴛs ᴛʜᴧᴛ υsєʀ's ɪᴅ
❍ /info : ɢєᴛ ɪηғσʀϻᴧᴛɪση ᴧʙσυᴛ ᴧ υsєʀ.
❍ /givelink : ɢєᴛ ɪηғσʀϻᴧᴛɪση ᴧʙσυᴛ ᴧ ɢɪᴛʜυʙ υsєʀ
❍ /groupdata : ɢєᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴀᴛᴀ
❍ /groupinfo : ɢєᴛ ʏσᴜʀ ɢʀσᴜᴘ ɪηғσ `ᴇx :- /groupinfo ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ`
❍ /status : ɢєᴛ ʏσᴜʀ ɢʀσᴜᴘ sᴛᴧᴛᴜs

𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_05(cls):
        return f'''```
❖ ғσηᴛ ❖```
**ʙʏ υsɪηɢ ᴛʜɪs ϻσᴅυʟє ʏσυ ᴄᴧη ᴄʜᴧηɢє ғσηᴛs σғ ᴧηʏ ᴛєxᴛ!

❍ /font [ᴛєxᴛ]**
```
❖ єxᴧϻᴘʟє : /font Baby```

**❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL}) **
'''

    @property
    def HELP_06(cls):
        return f'''```
❖ ϻᴧᴛʜ ǫυᴧᴛɪσηs sσʟᴠє ❖```

**❍ /math ➠ sσʟᴠєs ϻᴧᴛʜєϻᴧᴛɪᴄᴧʟ ᴘʀσʙʟєϻs ᴧηᴅ ǫυᴧᴛɪσηs

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_07(cls):
        return f'''```
❖ ᴛᴧɢ ᴄσϻϻᴧηᴅꜱ ❖```
**✿ ᴄʜσσsє ᴛᴧɢ ɪη ʏσυʀ ᴄʜᴧᴛ ✿

❍ /all ➠ ᴧηʏ ᴡʀɪᴛᴛєη ᴛєxᴛ ᴛᴧɢ
❍ /alloff ➠ sᴛσᴘ ᴛᴧɢ


❍ /shayari ➠ ʀᴧηᴅσϻ sʜᴧʏᴧʀɪ ᴛᴧɢ 
❍ /shstop ⇴ sᴛσᴘ ᴛᴧɢ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_08(cls):
        return f'''```
❖ ᴄᴏᴜᴘʟᴇs ᴄσϻϻᴧηᴅꜱ ❖```
**❍ /couples ➠ ᴜsє ᴛʜɪs ᴄσϻϻᴧηᴅ ᴧηᴅ sєє ɢʀσᴜᴘs ᴄσᴜᴘʟєs.
❍ /wish ➠ ᴜsє ᴛʜɪs ᴄσϻϻᴧηᴅ ᴧηᴅ sєє ɢʀσᴜᴘs ᴄσᴜᴘʟєs.
❍ /cute ➠ ᴄʜєᴄᴋ ʏσυʀ ᴄυᴛєηєss.
❍ /love ➠ ᴧᴅᴅ ᴛᴡᴏ ηᴧϻєs ᴧηᴅ sєє ʟσᴠᴇ ᴘσssɪʙɪʟɪᴛʏ !! `ʟɪᴋᴇ ʀᴧᴊ + priya.`

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_09(cls):
        return f'''```
❖ ʜᴧsᴛᴧɢ ❖```

**ʜєʀє ɪs ᴛʜє ʜєʟᴘ ғσʀ ᴛʜє ʜᴧsᴛᴧɢ ϻσᴅυʟє:

❍ /hastag : [ᴛєxᴛ]

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_10(cls):
        return f'''```
❖ sᴛɪᴄᴋєʀs ᴄσϻϻᴧηᴅꜱ ❖```
**❍ /packkang ➠ ᴄʀєᴧᴛєs ᴧ ᴘᴧᴄᴋ σғ sᴛɪᴄᴋєʀs ғʀσϻ ᴧ σᴛʜєʀ ᴘᴧᴄᴋ
❍ /stickerid ➠ ɢєᴛs ᴛʜє sᴛɪᴄᴋєʀ ɪᴅ σғ ᴧ sᴛɪᴄᴋєʀ
❍ /mmf ➠ ʀєᴘʟʏ ᴧηʏ ᴘɪᴄ & ɢɪᴠє ᴛєxᴛ `єx :- /mmf maxim`
❍ /kang ➠ ʀєᴘʟʏ ᴧηʏ sᴛɪᴄᴋєʀ & ᴄʀєᴀᴛє ʏσᴜʀ sᴛɪᴄᴋєʀ ᴘᴧᴄᴋ
❍ /st ➠ ғɪηᴅ ᴏʀɪɢɪηᴧʟ sᴛɪᴄᴋєʀ.

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_11(cls):
        return f'''```
❖ ғυη ❖```
**ʜєʀє ɪs ᴛʜє ʜєʟᴘ ғσʀ ᴛʜє ғυη ϻσᴅυʟє:

❍ /cute [ᴄʜєᴄᴋ ʏσυʀ ᴄυᴛєηєss]
❍ /horny [ᴄʜєᴄᴋ ʏσυʀ ʜσʀηʏηєss]
❍ /lezbian [ᴄʜєᴄᴋ ʜσᴡ ϻυᴄʜ ʟєᴢʙɪᴧη ʏσυ ᴧʀє]
❍ /gay [ᴄʜєᴄᴋ ʜσᴡ ϻυᴄʜ ɢᴧʏ ʏσυ ᴧʀє]
❍ /rand [ᴄʜєᴄᴋ ʜσᴡ ϻυᴄʜ ʀᴧηᴅ ʏσυ ᴧʀє]
❍ /boob [ᴄʜєᴄᴋ ʏσυʀ ʙσσʙs sɪᴢє]
❍ /cock [ᴄʜєᴄᴋ ʏσυʀ ᴅɪᴄᴋ sɪᴢє]
❍ /truth [sєηᴅs ᴧ ʀᴧηᴅσϻ ᴛʀυᴛʜ sᴛʀɪηɢ]
❍ /dare : [sєηᴅs ᴧ ʀᴧηᴅσϻ ᴅᴧʀє sᴛʀɪηɢ]

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_12(cls):
        return f'''```
❖ ǫυσᴛʟʏ ❖```
**ʜєʀє ɪs ᴛʜє ʜєʟᴘ ғσʀ ᴛʜє ǫυσᴛʟʏ ϻσᴅυʟє:

❍ /q : ᴄʀєᴧᴛє ᴧ ǫυσᴛє ғʀσϻ ᴛʜє ϻєssᴧɢє
❍ /q r : ᴄʀєᴧᴛє ᴧ ǫυσᴛє ғʀσϻ ᴛʜє ϻєssᴧɢє ᴡɪᴛʜ ʀєᴘʟʏ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_13(cls):
        return f'''```
❖ ᴛʀυᴛʜ ᴧηᴅ ᴅᴧʀє ❖```

**❖ ᴛʀυᴛʜ ᴧηᴅ ᴅᴧʀє ᴄσϻϻᴧηᴅ

❍ /truth : sєηᴅs ᴧ ʀᴧηᴅσϻ ᴛʀυᴛʜ sᴛʀɪηɢ
❍ /dare : sєηᴅs ᴧ ʀᴧηᴅσϻ ᴅᴧʀє sᴛʀɪηɢ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_14(cls):
        return f'''```
❖ ᴧᴠᴧɪʟᴧʙʟє ᴄσϻϻᴧηᴅs ꜰσʀ ᴧᴄᴛɪση```
**❖ 𝖠𝖣𝖬𝖨𝖭𝖲 𝖮𝖭𝖫𝖸 :**

<u>**❖ ʙᴧη ᴄσϻϻᴧηᴅꜱ ❖**</u>

**❍ /ban <userhandle> : ʙᴧηs ᴧ υsєʀ. (ᴠɪᴧ ʜᴧηᴅʟє, σʀ ʀєᴘʟʏ)
❍ /sban <userhandle>: sɪʟєηᴛʟʏ ʙᴧη ᴧ υsєʀ ᴅєʟєᴛєs ᴄσϻϻᴧηᴅ, ʀєᴘʟɪєᴅ ϻєssᴧɢє ᴧηᴅ ᴅσєsη'ᴛ ʀєᴘʟʏ (ᴠɪᴧ ʜᴧηᴅʟє, σʀ ʀєᴘʟʏ)
❍ /tban <userhandle> : x(ϻ/ʜ/ᴅ): ʙᴧηs ᴧ υsєʀ ғσʀ x ᴛɪϻє (ᴠɪᴧ ʜᴧηᴅʟє, σʀ ʀєᴘʟʏ) ϻ = ϻɪηυᴛєs, ʜ = ʜσυʀs, ᴅ = ᴅᴧʏs
❍ /unban <userhandle> : υηʙᴧηs ᴧ υsєʀ (ᴠɪᴧ ʜᴧηᴅʟє, σʀ ʀєᴘʟʏ)**

<u>**❖ ᴋɪᴄᴋs ᴄσϻϻᴧηᴅꜱ ❖**</u>

**❍ /kick <userhandle> : ᴋɪᴄᴋs ᴧ υsєʀ συᴛ σғ ᴛʜє ɢʀσυᴘ, (ᴠɪᴧ ʜᴧηᴅʟє, σʀ ʀєᴘʟʏ)
❍ /kickme: ᴋɪᴄᴋs ᴛʜє υsєʀ ᴡʜσ ɪssυєᴅ ᴛʜє ᴄσϻϻᴧηᴅ**

<u>**❖ ϻυᴛє ᴄσϻϻᴧηᴅꜱ ❖**</u>

**❖ ᴧᴠᴧɪʟᴧʙʟє ᴄσϻϻᴧηᴅs ꜰσʀ ϻυᴛє :**

**❖ 𝖠𝖣𝖬𝖨𝖭𝖲 𝖮𝖭𝖫𝖸 :

❍ /mute <userhandle> : sɪʟєηᴄєs ᴧ υsєʀ ᴄᴧη ᴧʟsσ ʙє υsєᴅ ᴧs ᴧ ʀєᴘʟʏ, ϻυᴛɪηɢ ᴛʜє ʀєᴘʟɪєᴅ ᴛσ υsєʀ
❍ /tmute <userhandle> x(ϻ/ʜ/ᴅ): ϻυᴛєs ᴧ υsєʀ ғσʀ x ᴛɪϻє (ᴠɪᴧ ʜᴧηᴅʟє, σʀ ʀєᴘʟʏ). ϻ = ϻɪηυᴛєs, ʜ = ʜσυʀs, ᴅ = ᴅᴧʏs.
❍ /unmute <userhandle>: υηϻυᴛєs ᴧ υsєʀ ᴄᴧη ᴧʟsσ ʙє υsєᴅ ᴧs ᴧ ʀєᴘʟʏ, ϻυᴛɪηɢ ᴛʜє ʀєᴘʟɪєᴅ ᴛσ υsєʀ**

```
ᴛʜɪs ᴄσϻϻᴧηᴅ ᴡɪʟʟ ᴡσʀᴋ σηʟʏ ɪғ ʏσυ ɢɪᴠє ʙᴧη ʀɪɢʜᴛs ᴛσ ᴛʜє ʙσᴛ ᴡɪᴛʜ ᴧᴅϻɪη```


**❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_15(cls):
        return f'''```
❖ ᴋɪᴄᴋs ᴄσϻϻᴧηᴅꜱ ❖```

**❍ /kick <userhandle> : ᴋɪᴄᴋs ᴧ υsєʀ συᴛ σғ ᴛʜє ɢʀσυᴘ, (ᴠɪᴧ ʜᴧηᴅʟє, σʀ ʀєᴘʟʏ)
❍ /kickme: ᴋɪᴄᴋs ᴛʜє υsєʀ ᴡʜσ ɪssυєᴅ ᴛʜє ᴄσϻϻᴧηᴅ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_16(cls):
        return f'''```
❖ ϻυᴛє ᴄσϻϻᴧηᴅꜱ ❖```

**❖ ᴧᴠᴧɪʟᴧʙʟє ᴄσϻϻᴧηᴅs ꜰσʀ ϻυᴛє :

❖ 𝖠𝖣𝖬𝖨𝖭𝖲 𝖮𝖭𝖫𝖸 :

❍ /mute <userhandle> : sɪʟєηᴄєs ᴧ υsєʀ ᴄᴧη ᴧʟsσ ʙє υsєᴅ ᴧs ᴧ ʀєᴘʟʏ, ϻυᴛɪηɢ ᴛʜє ʀєᴘʟɪєᴅ ᴛσ υsєʀ
❍ /tmute <userhandle> x(ϻ/ʜ/ᴅ): ϻυᴛєs ᴧ υsєʀ ғσʀ x ᴛɪϻє (ᴠɪᴧ ʜᴧηᴅʟє, σʀ ʀєᴘʟʏ). ϻ = ϻɪηυᴛєs, ʜ = ʜσυʀs, ᴅ = ᴅᴧʏs.
❍ /unmute <userhandle>: υηϻυᴛєs ᴧ υsєʀ ᴄᴧη ᴧʟsσ ʙє υsєᴅ ᴧs ᴧ ʀєᴘʟʏ, ϻυᴛɪηɢ ᴛʜє ʀєᴘʟɪєᴅ ᴛσ υsєʀ**
```
ᴛʜɪs ᴄσϻϻᴧηᴅ ᴡɪʟʟ ᴡσʀᴋ σηʟʏ ɪғ ʏσυ ɢɪᴠє ʙᴧη ʀɪɢʜᴛs ᴛσ ᴛʜє ʙσᴛ ᴡɪᴛʜ ᴧᴅϻɪη```

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_17(cls):
        return f'''```
❖ ᴛʜєsє ᴧʀє ᴛʜє ᴧᴠᴧɪʟᴧʙʟє ɢʀσυᴘ ϻᴧηᴧɢєϻєηᴛ ᴄσϻϻᴧηᴅs```
**❖ 𝖠𝖣𝖬𝖨𝖭𝖲 𝖮𝖭𝖫𝖸 :**

<u>**❖ ᴘɪη|υηᴘɪη ᴄσϻϻᴧηᴅꜱ ❖**</u>

**❍ /pin ➠ ᴘɪηs ᴧ ϻєssᴧɢє ɪη ᴛʜє ɢʀσυᴘ
❍ /pinned ➠ ᴅɪsᴘʟᴧʏs ᴛʜє ᴘɪηηєᴅ ϻєssᴧɢє ɪη ᴛʜє ɢʀσυᴘ
❍ /unpin ➠ υηᴘɪηs ᴛʜє ᴄυʀʀєηᴛʟʏ ᴘɪηηєᴅ ϻєssᴧɢє**


<u>**❖ sᴛᴧғғ|ʙσᴛs ᴄσϻϻᴧηᴅꜱ ❖**</u>

**❍ /staff ➠ ᴅɪsᴘʟᴧʏs ᴛʜє ʟɪsᴛ σғ sᴛᴧғғ ϻєϻʙєʀs
❍ /bots ➠ ᴅɪsᴘʟᴧʏs ᴛʜє ʟɪsᴛ σғ ʙσᴛs ɪη ᴛʜє ɢʀσυᴘ**

<u>**❖ ɢʀσυᴘ sєᴛ υᴘ ᴄσϻϻᴧηᴅꜱ ❖**</u>

**❍ /settitle ➠ sєᴛs ᴛʜє ᴛɪᴛʟє σғ ᴛʜє ɢʀσυᴘ
❍ /setdiscription ➠ sєᴛs ᴛʜє ᴅєsᴄʀɪᴘᴛɪση σғ ᴛʜє ɢʀσυᴘ
❍ /setphoto ➠ sєᴛs ᴛʜє ɢʀσυᴘ ᴘʜσᴛσ
❍ /removephoto ➠ ʀєϻσᴠєs ᴛʜє ɢʀσυᴘ ᴘʜσᴛσ
❍ /unmuteall ➠ ᴜηϻᴜᴛᴇ ᴧʟʟ ϻᴜᴛᴇ ϻєϻʙєʀs
❍ /unbanall ➠ ᴜηʙᴧη ᴧʟʟ ʙᴧη ϻєϻʙєʀs
❍ /unpinall ➠ ᴜηᴘɪη ᴧʟʟ ᴘɪη ᴍєssᴧɢᴇ**

**❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_18(cls):
        return f'''```
❖ sᴛᴧғғ|ʙσᴛs ᴄσϻϻᴧηᴅꜱ ❖```

**❍ /staff ➠ ᴅɪsᴘʟᴧʏs ᴛʜє ʟɪsᴛ σғ sᴛᴧғғ ϻєϻʙєʀs
❍ /bots ➠ ᴅɪsᴘʟᴧʏs ᴛʜє ʟɪsᴛ σғ ʙσᴛs ɪη ᴛʜє ɢʀσυᴘ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_19(cls):
        return f'''```
❖ ɢʀσυᴘ sєᴛ υᴘ ᴄσϻϻᴧηᴅꜱ ❖```

**❍ /settitle ➠ sєᴛs ᴛʜє ᴛɪᴛʟє σғ ᴛʜє ɢʀσυᴘ
❍ /setdiscription ➠ sєᴛs ᴛʜє ᴅєsᴄʀɪᴘᴛɪση σғ ᴛʜє ɢʀσυᴘ
❍ /setphoto ➠ sєᴛs ᴛʜє ɢʀσυᴘ ᴘʜσᴛσ
❍ /removephoto ➠ ʀєϻσᴠєs ᴛʜє ɢʀσυᴘ ᴘʜσᴛσ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_20(cls):
        return f'''```
❖ ɢʀσυᴘ ᴄσϻϻᴧηᴅꜱ ❖```

**❍ /zombies ➠ ʀєϻσᴠєs ᴧᴄᴄ ᴅєʟєᴛєᴅ ϻєϻʙєʀs ғʀσϻ ᴛʜє ɢʀσυᴘ


❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_21(cls):
        return f'''```
❖ ɢᴧϻє ᴘʟᴧʏ ❖```
**❖ ʜєʀє ᴧʀє sσϻє ϻɪηɪ ɢᴧϻєs :

❍ /dice [ʀσʟʟ ᴧ ᴅɪᴄє]
❍ /dart [ᴛʜʀσᴡ ᴧ ᴅᴧʀᴛ]
❍ /jackpot [ᴊᴧᴄᴋᴘσᴛ ϻᴧᴄʜɪηє]
❍ /ball [ʙσᴡʟɪηɢ ɢᴧϻє]
❍ /basket [ʙᴧsᴋєᴛʙᴧʟʟ ɢᴧϻє]
❍ /football [ғσσᴛʙᴧʟʟ ɢᴧϻє]

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_22(cls):
        return f'''```
❖ ɪϻᴘσsᴛєʀ ❖```
**ʜєʀє ɪs ᴛʜє ʜєʟᴘ ғσʀ ᴛʜє ɪϻᴘσsᴛєʀ ϻσᴅυʟє:

❍ /imposter on
❍ /imposter off

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_23(cls):
        return f'''```
❖ sᴧηɢ ϻᴧᴛᴧ ᴄσϻϻᴧηᴅ ❖```
**❍ /sg ➠ υsєʀ ηᴧϻє ᴧηᴅ υsєʀηᴧϻє ʜɪsᴛσʀʏ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_24(cls):
        return f'''```
❖ ᴛʀᴧηsʟᴧᴛєs ❖```
**❍ /tr ➠ ᴄᴧη ᴛʀᴧηꜱʟᴧᴛє ϻυʟᴛɪᴘʟє ʟᴧηɢυᴧɢєs

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_25(cls):
        return f'''```
❖ ɢɪᴛʜᴜʙ ᴄσϻϻᴧηᴅꜱ ❖```
**❍ /git ➠ ғɪηᴅ ʀєᴘᴏ ɢɪᴛ ᴜsєʀηᴧϻє
❍ /allrepo ➠ sєє ᴧʟʟ ʀєᴘᴏ ᴛʜʀσᴜɢʜ ɢɪᴛ ᴜsєʀηᴧϻє**

`єxᴧϻᴘʟє : /git ABHIPAPA`

**❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_26(cls):
        return f'''```
❖ ᴛєʟєɢʀᴧᴘʜ ❖```
**ᴄʀєᴧᴛє ᴧ ᴛєʟєɢʀᴧᴘʜ ʟɪηᴋ ᴧηʏ ϻєᴅɪᴧ!

❍ /tgm [ʀєᴘʟʏ ᴛσ ᴧηʏ ϻєᴅɪᴧ]
❍ /tgt [ʀєᴘʟʏ ᴛσ ᴧηʏ ϻєᴅɪᴧ]

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})**
'''

    @property
    def HELP_PROMOTION(cls):
        owner = config.OWNER_USERNAME.lstrip("@") if getattr(config, "OWNER_USERNAME", None) else ""
        owner_link = f"https://t.me/{owner}" if owner else config.SUPPORT_CHAT
        return f'''
**───────────────────────
ㅤ❖ ᴘᴧɪᴅ ᴘʀσϻσᴛɪση ᴧᴠᴧɪʟᴧʙʟє ❖
───────────────────────
❍ ᴄʜᴧᴛᴛɪηɢ ɢʀσυᴘ's
❍ ᴄσʟσʀ ᴛʀᴧᴅɪηɢ ɢᴧϻє's
❍ ᴄʜᴧηηєʟ's | ɢʀσυᴘ's .....
❍ ʙєᴛᴛɪηɢ ᴧᴅs σʀ ᴧηʏᴛʜɪηɢ
───────────────────────
● ᴘʀσϻσᴛє ᴧηʏᴛʜɪηɢ ʏσυ ᴡᴧηᴛ ση συʀ ᴘʟᴧᴛғσʀϻ ᴡɪᴛʜ ʙєsᴛ ᴘʟᴧηs ᴧηᴅ ᴘʀσᴘєʀ sєʀᴠɪᴄєs
───────────────────────
● ᴅᴧɪʟʏ, ᴡєєᴋʟʏ ᴧηᴅ ϻσηᴛʜʟʏ ᴘʟᴧη'ꜱ ᴧᴠᴧɪʟᴧʙʟє ꜰσʀ ʙɪɢ ʙυꜱɪηєꜱꜱєꜱ ᴧᴛ ᴛʜє ʙєꜱᴛ ᴘσꜱꜱɪʙʟє ᴄσηᴅɪᴛɪσηꜱ !
───────────────────────
● ʙєsᴛ ᴧηᴅ ᴄʜєᴧᴘ ɪη ᴛєʟєɢʀᴧϻ 400-500+ ϻєϻʙєʀs ɪη σηє ᴘʀσϻσᴛɪση ɢυʀᴧηᴛєє...
───────────────────────
❍ ᴄσηᴛᴧᴄᴛ - [- 𝑶𝑾𝑵𝑬𝑅 !!]({owner_link})
───────────────────────**
'''

    @property
    def HELP_ABOUT(cls):
        bot_name = getattr(config, "BOT_NAME", "Music Bot")
        return f'''
**───────────────────────
 ᴡєʟᴄσϻє ᴛσ ˹[{bot_name}]({config.SUPPORT_CHANNEL})˼ ʙσᴛ sᴛᴧᴛυs
───────────────────────
      ❖ │ ʀєᴧʟ ᴛɪϻє ʙσᴛ's sᴛᴧᴛυs │❖
───────────────────────
╭⎋ [{bot_name}]({config.SUPPORT_CHANNEL}) : ᴧʟɪᴠє
╰⊚ υᴘᴛɪϻє : 12ʜ:58ϻ:20s | ᴄᴘυ : 5.0% | υsᴧɢє : 24 | ᴧssɪsᴛᴧηᴛs : 02
───────────────────────
⊚ ʙσᴛ sᴛᴧᴛυs ᴧηᴅ ϻσʀє ʙσᴛs - [ᴄʟɪᴄᴋ ʜєʀє]({config.SUPPORT_CHANNEL})
───────────────────────
❍ 𝐏ᴏᴡєʀєᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})
───────────────────────**
'''

    @property
    def HELP_ALLBOT(cls):
        owner = config.OWNER_USERNAME.lstrip("@") if getattr(config, "OWNER_USERNAME", None) else ""
        owner_link = f"https://t.me/{owner}" if owner else config.SUPPORT_CHAT
        bot_name = getattr(config, "BOT_NAME", "Music Bot")
        return f'''
**───────────────────────
❖ ᴧ ϻᴜsɪᴄ + ϻᴧηᴧɢєϻєηᴛ ʙσᴛ ғσʀ ᴛєʟєɢʀᴧϻ ɢʀσᴜᴘs / ᴄʜᴧηηєʟs
───────────────────────
● ᴡʀɪᴛᴛєη ɪη ➥ [ᴩʏᴛʜση](https://www.python.org/)
● ᴅᴧᴛᴧʙᴧsє ➥ [ϻᴏηɢᴏ-ᴅʙ](https://www.mongodb.com/)
───────────────────────
● ηᴏ ʟᴀɢ ɪssᴜєs ηᴏ ᴧᴅs ηᴏ ʙᴜɢs.
● sᴜᴘᴘᴏʀᴛ ᴧʟʟ ᴛɪϻє sᴛᴧʏ ᴡɪᴛʜ ᴜs.
● ᴇηᴊᴏʏ ғєєʟ ғʀєє ϻᴜsɪᴄ ᴡɪᴛʜ ˹ {bot_name}˼
● ᴧᴅᴅ ϻє ηᴏᴡ ʙᴧʙʏ ɪɴ ʏᴏᴜʀ ɢʀσᴜᴘs.
───────────────────────
❖ υᴘᴅᴧᴛєs ᴄʜᴧηηєʟ ➥ [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({config.SUPPORT_CHANNEL})
❖ sυᴘᴘσʀᴛ ᴄʜᴧᴛ ➥ [sυᴘᴘσʀᴛ]({config.SUPPORT_CHAT})
❖ ʙᴏᴛ σᴡηєʀ ➥ [σᴡηєʀ]({owner_link})
❖ ʀєᴘσ ʟɪηᴋ ➥ [ᴄʟɪᴄᴋ-ʜєʀє]({config.UPSTREAM_REPO})
───────────────────────
❖ ᴄʟɪᴄᴋ ση ᴛʜє ʜєʟᴘ ʙυᴛᴛση ᴛσ ɢєᴛ ɪηғσ
   ᴧʙσυᴛ ϻʏ ϻσᴅυʟєs ᴧηᴅ ᴄσϻϻᴧηᴅs...!!
───────────────────────**
'''


class Helper(metaclass=HelperMeta):
    fullpromote = {
        'can_change_info': True,
        'can_post_messages': True,
        'can_edit_messages': True,
        'can_delete_messages': True,
        'can_invite_users': True,
        'can_restrict_members': True,
        'can_pin_messages': True,
        'can_promote_members': True,
        'can_manage_chat': True,
    }

    promoteuser = {
        'can_change_info': False,
        'can_post_messages': True,
        'can_edit_messages': True,
        'can_delete_messages': False,
        'can_invite_users': True,
        'can_restrict_members': False,
        'can_pin_messages': False,
        'can_promote_members': False,
        'can_manage_chat': True,
    }
