import config


def _get_channel():
    return getattr(config, "SUPPORT_CHANNEL", "https://t.me/II_SHAYRI_KI_DUNIYA_II")


class HelpersMeta(type):
    @property
    def HELP_1(cls):
        return f"""```
❖ ᴧᴅϻɪη ᴄσϻϻᴧηᴅs ❖```
**ᴊυsᴛ ᴧᴅᴅ ᴄ ɪη ᴛʜє sᴛᴧʀᴛɪηɢ σғ ᴛʜє ᴄσϻϻᴧηᴅs ᴛσ υsє ᴛʜєϻ ғσʀ ᴄʜᴧηηєʟ

❍ /pause : ᴩᴧυsє ᴛʜє ᴄυʀʀєηᴛ ᴩʟᴧʏɪηɢ sᴛʀєᴧϻ
❍ /resume : ʀєsυϻє ᴛʜє ᴩᴧυsєᴅ sᴛʀєᴧϻ
❍ /skip : sᴋɪᴩ ᴛʜє ᴄυʀʀєηᴛ ᴩʟᴧʏɪηɢ sᴛʀєᴧϻ ᴧηᴅ sᴛᴧʀᴛ sᴛʀєᴧϻɪηɢ ᴛʜє ηєxᴛ ᴛʀᴧᴄᴋ ɪη ǫυєυє
❍ /end σʀ /stop : ᴄʟєᴧʀs ᴛʜє ǫυєυє ᴧηᴅ єηᴅ ᴛʜє ᴄυʀʀєηᴛ ᴩʟᴧʏɪηɢ sᴛʀєᴧϻ
❍ /player : ɢєᴛ ᴧ ɪηᴛєʀᴧᴄᴛɪᴠє ᴩʟᴧʏєʀ ᴩᴧηєʟ
❍ /queue : sʜσᴡs ᴛʜє ǫυєυєᴅ ᴛʀᴧᴄᴋs ʟɪsᴛ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹  ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ  ˼]({_get_channel()})**
"""

    @property
    def HELP_2(cls):
        return f"""```
❖ ᴧυᴛʜ υsєʀs ❖```
**ᴧυᴛʜ υsєʀs ᴄᴧη υsє ᴧᴅϻɪη ʀɪɢʜᴛs ɪη ᴛʜє ʙσᴛ ᴡɪᴛʜσυᴛ ᴧᴅϻɪη ʀɪɢʜᴛs ɪη ᴛʜє ᴄʜᴧᴛ

❍ /auth [υsєʀηᴧϻє/υsєʀ_ɪᴅ] : ᴧᴅᴅ ᴧ υsєʀ ᴛσ ᴧυᴛʜ ʟɪsᴛ σғ ᴛʜє ʙσᴛ
❍ /unauth [υsєʀηᴧϻє/υsєʀ_ɪᴅ] : ʀєϻσᴠє ᴧ ᴧυᴛʜ υsєʀs ғʀσϻ ᴛʜє ᴧυᴛʜ υsєʀs ʟɪsᴛ
❍ /authusers : sʜσᴡs ᴛʜє ʟɪsᴛ σғ ᴧυᴛʜ υsєʀs σғ ᴛʜє ɢʀσυᴩ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼ ]({_get_channel()})**
"""

    @property
    def HELP_3(cls):
        return f"""```
❖ ʙʀσᴧᴅᴄᴧsᴛ ғєᴧᴛυʀє [σηʟʏ ғσʀ sυᴅσєʀs] ❖```
**/broadcast [ϻєssᴧɢє σʀ ʀєᴩʟʏ ᴛσ ᴧ ϻєssᴧɢє] : ʙʀσᴧᴅᴄᴧsᴛ ᴧ ϻєssᴧɢє ᴛσ sєʀᴠєᴅ ᴄʜᴧᴛs σғ ᴛʜє ʙσᴛ
```
❖ ʙʀσᴧᴅᴄᴧsᴛɪηɢ ϻσᴅєs ❖

❍ -pin : ᴩɪηs ʏσυʀ ʙʀσᴧᴅᴄᴧsᴛєᴅ ϻєssᴧɢєs ɪη sєʀᴠєᴅ ᴄʜᴧᴛs
❍ -pinloud : ᴩɪηs ʏσυʀ ʙʀσᴧᴅᴄᴧsᴛєᴅ ϻєssᴧɢє ɪη sєʀᴠєᴅ ᴄʜᴧᴛs ᴧηᴅ sєηᴅ ησᴛɪғɪᴄᴧᴛɪση ᴛσ ᴛʜє ϻєϻʙєʀs
❍ -user : ʙʀσᴧᴅᴄᴧsᴛs ᴛʜє ϻєssᴧɢє ᴛσ ᴛʜє υsєʀs ᴡʜσ ʜᴧᴠє sᴛᴧʀᴛєᴅ ʏσυʀ ʙσᴛ
❍ -assistant : ʙʀσᴧᴅᴄᴧsᴛ ʏσυʀ ϻєssᴧɢє ғʀσϻ ᴛʜє ᴧssɪᴛᴧηᴛ ᴧᴄᴄσυηᴛ σғ ᴛʜє ʙσᴛ
❍ -nobot : ғσʀᴄєs ᴛʜє ʙσᴛ ᴛσ ησᴛ ʙʀσᴧᴅᴄᴧsᴛ ᴛʜє ϻєssᴧɢє```

❖ єxᴧϻᴩʟє:</b> <code>/broadcast -user -assistant -pin ᴛєsᴛɪηɢ ʙʀσᴧᴅᴄᴧsᴛ</code>

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ  ˼]({_get_channel()})**
"""

    @property
    def HELP_4(cls):
        return f"""```
❖ ᴄʜᴧᴛ ʙʟᴧᴄᴋʟɪsᴛ ғєᴧᴛυʀє ❖```
**ʀєsᴛʀɪᴄᴛ sʜɪᴛ ᴄʜᴧᴛs ᴛσ υsє συʀ ᴘʀєᴄɪσυs ʙσᴛ

❍ /blacklistchat [ᴄʜᴧᴛ ɪᴅ] : ʙʟᴧᴄᴋʟɪsᴛ ᴧ ᴄʜᴧᴛ ғʀσϻ υsɪηɢ ᴛʜє ʙσᴛ
❍ /whitelistchat [ᴄʜᴧᴛ ɪᴅ] : ᴡʜɪᴛєʟɪsᴛ ᴛʜє ʙʟᴧᴄᴋʟɪsᴛєᴅ ᴄʜᴧᴛ
❍ /blacklistedchat : sʜσᴡs ᴛʜє ʟɪsᴛ σғ ʙʟᴧᴄᴋʟɪsᴛєᴅ ᴄʜᴧᴛs

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""

    @property
    def HELP_5(cls):
        return f"""```
❖ ʙʟσᴄᴋ υsєʀs ❖```
**sᴛᴧʀᴛs ɪɢησʀɪηɢ ᴛʜє ʙʟᴧᴄᴋʟɪsᴛєᴅ υsєʀ, sσ ᴛʜᴧᴛ ʜє ᴄᴧη'ᴛ υsє ʙσᴛ ᴄσϻϻᴧηᴅs

❍ /block [υsєʀηᴧϻє σʀ ʀєᴩʟʏ ᴛσ ᴧ υsєʀ] : ʙʟσᴄᴋ ᴛʜє υsєʀ ғʀσϻ συʀ ʙσᴛ
❍ /unblock [υsєʀηᴧϻє σʀ ʀєᴩʟʏ ᴛσ ᴧ υsєʀ] : υηʙʟσᴄᴋs ᴛʜє ʙʟσᴄᴋєᴅ υsєʀ
❍ /blockedusers : sʜσᴡs ᴛʜє ʟɪsᴛ σғ ʙʟσᴄᴋєᴅ υsєʀs.

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""

    @property
    def HELP_6(cls):
        return f"""```
❖ ᴄʜᴧηηєʟ ᴩʟᴧʏ ᴄσϻϻᴧηᴅs ❖```
**ʏσυ ᴄᴧη sᴛʀєᴧϻ ᴧυᴅɪσ/ᴠɪᴅєσ ɪη ᴄʜᴧηηєʟ

❍ /cplay : sᴛᴧʀᴛs sᴛʀєᴧϻɪηɢ ᴛʜє ʀєǫυєsᴛєᴅ ᴧυᴅɪσ ᴛʀᴧᴄᴋ ση ᴄʜᴧηηєʟ's ᴠɪᴅєσᴄʜᴧᴛ
❍ /cvplay : sᴛᴧʀᴛs sᴛʀєᴧϻɪηɢ ᴛʜє ʀєǫυєsᴛєᴅ ᴠɪᴅєσ ᴛʀᴧᴄᴋ ση ᴄʜᴧηηєʟ's ᴠɪᴅєσᴄʜᴧᴛ
❍ /cplayforce or /cvplayforce : sᴛσᴩs ᴛʜє σηɢσɪηɢ sᴛʀєᴧϻ ᴧηᴅ sᴛᴧʀᴛs sᴛʀєᴧϻɪηɢ ᴛʜє ʀєǫυєsᴛєᴅ ᴛʀᴧᴄᴋ
❍ /channelplay [ᴄʜᴧᴛ υsєʀηᴧϻє σʀ ɪᴅ] σʀ [ᴅɪsᴧʙʟє] : ᴄσηηєᴄᴛ ᴄʜᴧηηєʟ ᴛσ ᴧ ɢʀσυᴘ ᴧηᴅ sᴛᴧʀᴛs sᴛʀєᴧϻɪηɢ ᴛʀᴧᴄᴋs ʙʏ ᴛʜє ʜєʟᴩ σғ ᴄσϻϻᴧηᴅs sєηᴛ ɪη ɢʀσυᴘ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""

    @property
    def HELP_7(cls):
        return f"""```
❖ ɢʟσʙᴧʟ ʙᴧη ғєᴧᴛυʀє ❖```
**❍ /gban [υsєʀηᴧϻє σʀ ʀєᴩʟʏ ᴛσ ᴧ υsєʀ] : ɢʟσʙᴧʟʟʏ ʙᴧηs ᴛʜє ᴄʜυᴛɪʏᴧ ғʀσϻ ᴧʟʟ ᴛʜє sєʀᴠєᴅ ᴄʜᴧᴛs ᴧηᴅ ʙʟᴧᴄᴋʟɪsᴛ ʜɪϻ ғʀσϻ υsɪηɢ ᴛʜє ʙσᴛ
❍ /ungban [υsєʀηᴧϻє σʀ ʀєᴩʟʏ ᴛσ ᴧ υsєʀ] : ɢʟσʙᴧʟʟʏ υηʙᴧηs ᴛʜє ɢʟσʙᴧʟʟʏ ʙᴧηηєᴅ υsєʀ
❍ /gbannedusers : sʜσᴡs ᴛʜє ʟɪsᴛ σғ ɢʟσʙᴧʟʟʏ ʙᴧηηєᴅ υsєʀs

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""

    @property
    def HELP_8(cls):
        return f"""```
❖ ʟσσᴘ sᴛʀєᴧϻ ❖```
**sᴛᴧʀᴛs sᴛʀєᴧϻɪηɢ ᴛʜє σηɢσɪηɢ sᴛʀєᴧϻ ɪη ʟσσᴘ

❍ /loop [enable/disable] : єηᴧʙʟєs/ᴅɪsᴧʙʟєs ʟσσᴘ ғσʀ ᴛʜє σηɢσɪηɢ sᴛʀєᴧϻ
❍ /loop [1, 2, 3, ...] : єηᴧʙʟєs ᴛʜє ʟσσᴘ ғσʀ ᴛʜє ɢɪᴠєη ᴠᴧʟυє

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""

    @property
    def HELP_9(cls):
        return f"""```
❖ ϻᴧɪηᴛєηᴧηᴄє ϻσᴅє ❖```
**❍ /logs : ɢєᴛ ʟσɢs σғ ᴛʜє ʙσᴛ
❍ /logger [єηᴧʙʟє/ᴅɪsᴧʙʟє] : ʙσᴛ ᴡɪʟʟ sᴛᴧʀᴛ ʟσɢɢɪηɢ ᴛʜє ᴧᴄᴛɪᴠɪᴛɪєs ʜᴧᴩᴩєη ση ʙσᴛ
❍ /maintenance [єηᴧʙʟє/ᴅɪsᴧʙʟє] : єηᴧʙʟє σʀ ᴅɪsᴧʙʟє ᴛʜє ϻᴧɪηᴛєηᴧηᴄє ϻσᴅє σғ ʏσυʀ ʙσᴛ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""

    @property
    def HELP_10(cls):
        return f"""```
❖ ᴘɪηɢ & sᴛᴧᴛs ❖```
**❍ /start : sᴛᴧʀᴛs ᴛʜє ϻυsɪᴄ ʙσᴛ
❍ /help : ᴛᴧʙ ᴛσ sєє ʜєʟᴘ ϻєηυ
❍ /ping : sʜσᴡs ᴛʜє ᴩɪηɢ ᴧηᴅ sʏsᴛєϻ sᴛᴧᴛs σғ ᴛʜє ʙσᴛ
❍ /stats : sʜσᴡs ᴛʜє σᴠєʀᴧʟʟ sᴛᴧᴛs σғ ᴛʜє ʙσᴛ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""

    @property
    def HELP_11(cls):
        return f"""```
❖ ᴩʟᴧʏ ᴄσϻϻᴧηᴅs ❖```
```
V : sᴛᴧηᴅs ғσʀ ᴠɪᴅєσ ᴩʟᴧʏ
FORCE : sᴛᴧηᴅs ғσʀ ғσʀᴄє ᴩʟᴧʏ```
**❍ /play σʀ /vplay : sᴛᴧʀᴛs sᴛʀєᴧϻɪηɢ ᴛʜє ʀєǫυєsᴛєᴅ ᴛʀᴧᴄᴋ ση ᴠɪᴅєσᴄʜᴧᴛ
❍ /playforce σʀ /vplayforce : sᴛσᴩs ᴛʜє σηɢσɪηɢ sᴛʀєᴧϻ ᴧηᴅ sᴛᴧʀᴛs sᴛʀєᴧϻɪηɢ ᴛʜє ʀєǫυєsᴛєᴅ ᴛʀᴧᴄᴋ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""

    @property
    def HELP_12(cls):
        return f"""```
❖ sʜυғғʟє σ̨υєυє ❖```
**❍ /shuffle : sʜυғғʟє's ᴛʜє σ̨υєυє.
❍ /queue : sʜσᴡs ᴛʜє sʜυғғʟєᴅ σ̨υєυє

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""

    @property
    def HELP_13(cls):
        return f"""```
❖ sєєᴋ sᴛʀєᴧϻ ❖```
**❍ /seek [ᴅυʀᴧᴛɪση ɪη sєᴄσηᴅs] : sєєᴋ ᴛʜє sᴛʀєᴧϻ ᴛσ ᴛʜє ɢɪᴠєη ᴅυʀᴧᴛɪση
❍ /seekback [ᴅυʀᴧᴛɪση ɪη sєᴄσηᴅs] : ʙᴧᴄᴋᴡᴧʀᴅ sєєᴋ ᴛʜє sᴛʀєᴧϻ ᴛσ ᴛʜє ᴛʜє ɢɪᴠєη ᴅυʀᴧᴛɪση

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""

    @property
    def HELP_14(cls):
        return f"""```
❖ sηɢ ᴅσᴡηʟσᴧᴅ ❖```
**❍ /song [sηɢ ηᴧϻє/ʏᴛ υʀʟ] : ᴅσᴡηʟσᴧᴅ ᴧηʏ ᴛʀᴧᴄᴋ ғʀσϻ ʏσυᴛυʙє ɪη ϻᴘ3 σʀ ϻᴘ4 ғσʀϻᴧᴛs

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""

    @property
    def HELP_15(cls):
        return f"""```
❖ sᴘєєᴅ ᴄσϻϻᴧηᴅs ❖```
**ʏσυ ᴄᴧη ᴄσηᴛʀσʟ ᴛʜє ᴘʟᴧʏʙᴧᴄᴋ sᴘєєᴅ σғ ᴛʜє σηɢσɪηɢ sᴛʀєᴧϻ. [ᴧᴅϻɪηs σηʟʏ]

❍ /speed or /playback : ғσʀ ᴧᴅᴊυsᴛɪηɢ ᴛʜє ᴧυᴅɪσ ᴘʟᴧʏʙᴧᴄᴋ sᴘєєᴅ ɪη ɢʀσυᴘ
❍ /cspeed or /cplayback : ғσʀ ᴧᴅᴊυsᴛɪηɢ ᴛʜє ᴧυᴅɪσ ᴘʟᴧʏʙᴧᴄᴋ sᴘєєᴅ ɪη ᴄʜᴧηηєʟ

❖ 𝐏ᴏᴡᴇʀᴇᴅ 𝖡ʏ » [˹ ғᴀɪʀʏᴛᴀʟᴇ ꭙ ɴᴇᴛᴡᴏʀᴋ ˼]({_get_channel()})**
"""


class Helpers(metaclass=HelpersMeta):
    pass


# For backwards compatibility with code importing HELP_1 ... HELP_15 directly
HELP_1 = Helpers.HELP_1
HELP_2 = Helpers.HELP_2
HELP_3 = Helpers.HELP_3
HELP_4 = Helpers.HELP_4
HELP_5 = Helpers.HELP_5
HELP_6 = Helpers.HELP_6
HELP_7 = Helpers.HELP_7
HELP_8 = Helpers.HELP_8
HELP_9 = Helpers.HELP_9
HELP_10 = Helpers.HELP_10
HELP_11 = Helpers.HELP_11
HELP_12 = Helpers.HELP_12
HELP_13 = Helpers.HELP_13
HELP_14 = Helpers.HELP_14
HELP_15 = Helpers.HELP_15
