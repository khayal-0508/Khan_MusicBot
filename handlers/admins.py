from pyrogram import Client, filters
from pyrogram.types import Message
import tgcalls
import sira
from config import SUDO_USERS
from cache.admins import set
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("pause")
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def pause(client: Client, message: Message):
    tgcalls.pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("𝗞𝗵𝗮𝗻 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁=⏸ Pauza.")


@Client.on_message(
    filters.command("resume")
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def resume(client: Client, message: Message):
    tgcalls.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("𝗞𝗵𝗮𝗻 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁=▶️ Davam edir.")


@Client.on_message(
    filters.command(["stop", "end"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def stop(client: Client, message: Message):
    try:
        sira.clear(message.chat.id)
    except:
        pass

    tgcalls.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("𝗞𝗵𝗮𝗻 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁=⏹ Bot dayandırıldı.")


@Client.on_message(
    filters.command(["skip", "next"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def skip(client: Client, message: Message):
    chat_id = message.chat.id

    sira.task_done(chat_id)
    await message.reply_text("Processing")
    if sira.is_empty(chat_id):
        tgcalls.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("nothing in queue")
    else:
        tgcalls.pytgcalls.change_stream(
            chat_id, sira.get(chat_id)["file_path"]
        )

        await message.reply_text("𝗞𝗵𝗮𝗻 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁=⏩ Cari mahnı dəyişdirildi.")


@Client.on_message(
    filters.command("admincache")
)
@errors
@admins_only
async def admincache(client, message: Message):
    set(message.chat.id, [member.user for member in await message.chat.get_members(filter="administrators")])
    await message.reply_text("𝗞𝗵𝗮𝗻 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁=❇️ Admin listi yeniləndi!")

@Client.on_message(
    filters.command("help") 
    & filters.group
    & ~ filters.edited
)
async def helper(client , message:Message):
     await message.reply_text("Burada əmrlər və necə istifadəsi izah olunur-: \n `/saavn` Mahnını Saavn-da axtarmaq və ilk nəticəni oxutmaq üçün \n `/deezer` Mahnını Deezer-də axtarmaq və keyfiyyətli musiqi əldə etmək üçün \n `/song` Youtube-da mahnını axtarmaq və ilk uyğun nəticəni çalmaq üçün üçün \n '/play` Bir linkə və ya hər hansı bir telegram səs sənədinə yanıt olaraq bu əmri yazın \n `/skip` Cari musiqini dəyişdirmək üçün \n `/stop or /kill` Mahnı botunu səsli söhbətdən kənarlaşdırmaq üçün \n `/pause` Oxunan cari musiqiyə pauza vermək üçün \n `/resume` Pauza verilən musiqini davam elətdirmək üçün. \n Inline axtarış da dəstəklənir. \n Daha çox məlumat üçün @KhanVlog kanalına qoşulun və ya @tag1y3v -ə müraciət edin")
