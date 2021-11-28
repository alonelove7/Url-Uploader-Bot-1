from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Scripted (object):

    START_TEXT = """
<html>Hey {} <html></html>

<html>I am Telegram Most Powerful Url Uploader Bot.</html>

<html>I can Upload Any Link in File or Video.</html>

<html>Use Help Command to Know How to Use me.</html>

<html>Made With 💕 By</html><html> @Tellybots_4u.</html>
"""
    HELP_TEXT = """
<html>Link to Media or File</html>
➠ <html>Send a link for upload to telegram file or media.</html>

<html>Set Thumbnail</html>
➠ <b>Send a photo to make it as permanent thumbnail.</html>

<html>Deleting Thumbnail</html>
➠ Send /delthumb to delete thumbnail.

<html>Show Thumbnail</html>
➠ Send /showthumb to view custom thumbnail.</html>

<html>Made With 💕 By</html><html> @Tellybots_4u</html>
"""
    ABOUT_TEXT = """
 **🤖 <html>Bot :** URL Uploader</html>\n
 **👲 <html>Developer :** [Tellybots_4u](https://telegram.me/tellybots_4u)</html>\n
 **👥 <html>Channel :** [Fayas Noushad](https://telegram.me/tellybots_4u)</html>\n
 **❄️ <html>Credits :** Everyone in this journey</html>\n
 **🍴 <html>Source :** [Click here](https://t.me/tellybots_digital)</html>\n
 **📝 <html>Language :** [Python3](https://python.org)</html>\n
 **📚 <html>Library :** [Pyrogram v1.2.0](https://pyrogram.org)</html>\n
 **🌟 <html>Server :** [Heroku](https://heroku.com)</html>\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    PROGRESS_DIS = """\n
╭───[**🔅Progress Bar🔅**]───⍟
│<b>📁 : {1} | {2}</b>\n
├<b>🚀 : {0}%</b>\n
├<b>⚡ : {3}/s</b>\n
├<b>⏱️ : {4}</b>\n
╰───────────────⍟"""



    CUSTOM_CAPTION = "<i>{}</i>"
    ACCESS_DENIED = "<b>¥ou Are Banned 🚫</b>"
    BANNED_USER_TEXT = "<i>¥ou are Banned 🚫</i>"
    TRYING_TO_UPLOAD = "<i>Trying to Upload.....</i>"
    CURRENT_THUMBNAIL = "<i>𝐘𝐨𝐮𝐫 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 🎭</i>"
    THUMBNAIL_SAVED = "<i>𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐒𝐚𝐯𝐞𝐝 ✅</i>"
    THUMBNAIL_DELETED = "<i>𝐘𝐨𝐮𝐫 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 ✅</i>"
    NO_THUMBNAIL_FOUND = "<i>𝐍𝐨 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐅𝐨𝐮𝐧𝐝 (𝐊𝐨𝐧𝐬𝐢 𝐆𝐚𝐚𝐥𝐢 𝐂𝐡𝐚𝐡𝐢𝐲𝐞)😔</i>"
    TRYING_TO_DOWNLOAD = "<i>𝐓𝐫𝐲𝐢𝐧𝐠 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝....</i>"
    UPLOAD_SUCCESS = "<u><i>Tʜᴀɴᴋᴀ Fᴏʀ Usɪɴɢ ᴍᴇ❤ @TheTeleRoid</i></u>"
    REPLY_TO_MEDIA = "<i>𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐌𝐞𝐝𝐢𝐚 𝐰𝐢𝐭𝐡 /convert</i>"
    UPLOAD_START = "<i>📤 𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐟𝐢𝐥𝐞 𝐩𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭...</i>\n"
    DOWNLOAD_START = "<i>📥 𝐃𝐨𝐰𝐧𝐥𝐨𝐝𝐢𝐧𝐠 𝐲𝐨𝐮𝐫 𝐟𝐢𝐥𝐞 𝐩𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭...</i>\n"
    JOIN_NOW_TEXT = "<code>𝕱𝖎𝖗𝖘𝖙 𝕵𝖔𝖎𝖓 𝕸𝖞 𝖀𝖕𝖉𝖆𝖙𝖊𝖘 𝕮𝖍𝖆𝖓𝖓𝖊𝖑 𝕿𝖔 𝖀𝖘𝖊 𝕸𝖊𝖍</code>"
    REPLY_TO_FILE = "<i>𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐭𝐡𝐚𝐭 𝐟𝐢𝐥𝐞 𝐰𝐢𝐭𝐡 /rename 𝐧𝐞𝐰 𝐧𝐚𝐦𝐞 .𝐞𝐱𝐭</i>"
    CONTACT_MY_DEVELOPER = "<i>Something Wrong Contact in Support Group @TeleRoid14 😑</i>"

    UPGRADE_TEXT = "<b>To upgrade your subscription <a href='https://t.me/TeleRoid14'>[ 𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞 ]</a></b>"
