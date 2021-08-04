from youtube_dl import YoutubeDL

from config import DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"✯𝗞𝗵𝗮𝗻 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁✯= {DURATION_LIMIT} dəqiqədən böyük fayllara icazə verilmir, seçdiyiniz musiqi faylı {duration} dəqiqədir"
        )

    ydl.download([url])
    return f"downloads/{info['id']}.{info['ext']}"
