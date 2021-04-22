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
Mən @tag1y3v tərəfindən yaradılmış 𝐊 𝐇 𝐀 𝐍    𝐌 𝐔 𝐒 𝐈 𝐂    𝐁 𝐎 𝐓 musiqi botuyam ♥️
Məi qrupunuza əlavə edərək musiqilərdən zövq alın.
Use the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Command", url="https://telegra.ph/%F0%9D%97%96%F0%9D%97%B5%F0%9D%97%BC%F0%9D%97%B0%F0%9D%97%BC%F0%9D%97%B9%F0%9D%97%AE%F0%9D%98%81%F0%9D%98%86%F0%9D%97%A4%F0%9D%98%82%F0%9D%97%B2%F0%9D%97%B2%F0%9D%97%BB%F0%9D%97%95%F0%9D%97%BC%F0%9D%98%81-04-03",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="https://t.me/balw0ysohbet"
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
