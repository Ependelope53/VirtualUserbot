# By @HeisenbergTheDanger and @xditya

from telethon import *

from virtualuserbot import CMD_HELP

from ..utils import admin_cmd


# Fixed by @NOOBGeng Second Member
@borg.on(admin_cmd(pattern="dm ?(.*)"))
async def _(dc):

    d = dc.pattern_match.group(1)

    c = d.split(" ")  # hehe

    chat_id = c[0]
    try:  # dc hehe
        chat_id = int(chat_id)
    # hmm 🤔🤔🤔🤔
    except BaseException:  # lalalala

        pass

    msg = ""
    masg = await dc.get_reply_message()  # ghanta😒😒
    if dc.reply_to_msg_id:
        await borg.send_message(chat_id, masg)
        await dc.edit("Pesan sudah terkirim!")
    for i in c[1:]:
        msg += i + " "  # Fixed by @NOOBGeng Second Member
    if msg == "":  # hoho
        return
    try:
        await borg.send_message(chat_id, msg)
        await dc.edit("`Pesan sudah terkirim!`")
    except BaseException:  # hmmmmmmmmm🤔🤔
        await dc.edit(".dm (username/id) (text)")


CMD_HELP.update(
    {
        "dm": ".dm (username/id) (text) atau \n.dm (username/id)(reply to msg)\n Direct Message the user"
    }
)
