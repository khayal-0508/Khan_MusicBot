from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Salam {message.from_user.first_name}!
Mən @tag1y3v tərəfindən yaradılmış 𝐊𝐇𝐀𝐍  𝐌𝐔𝐒𝐈𝐂  𝐁𝐎𝐓 musiqi botuyam ♥️
Məi qrupunuza əlavə edərək adminlik verin və playerim olan @KhanMusicAssistant -ı qrupa əlavə edərək musiqilərdən zövq alın.
Haqqımda daha çox məlumat əldə etmək üçün aşağıdakı düymələrdən istifadə edin.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sahibim✔️", url="https://t.me/tag1y3v",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Əmrlər✔️", url="https://telegra.ph/Khan-MusicBot-05-11",
                    )
                ],
               [
                    InlineKeyboardButton(
                        "📺Rəsmi Kanal✔️", url="https://t.me/KhanVlog",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Rəsmi Qrup", url="https://t.me/KhanChat"
                    ),
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ YouTube videosunu axtarmaq istəyirsiniz?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
