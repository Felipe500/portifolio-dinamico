from datetime import date
import locale
import os
from io import BytesIO
from pathlib import Path


from ipware import get_client_ip
from PIL import Image as Img

from django.http import HttpRequest
from django.core.files import File
from django.core.files.base import ContentFile


def get_ip_and_agent(request: HttpRequest) -> dict:
    try:
        agent = request.META.get("HTTP_USER_AGENT") or ""
        client_ip, _ = get_client_ip(request)
        return {"ip": client_ip, "agent": agent[:499]}
    except AttributeError:
        return {}


def get_message_of_day():
    locale.setlocale(locale.LC_ALL, locale.getlocale())
    today = date.today()
    msg = "um bom" if today.weekday() in (5, 6) else "uma boa"
    return f"Tenha {msg} {today.strftime('%A, %B %Y').title()} =D"


def generator_stars(time_experience_skill: str):
    years = int(time_experience_skill.split('_')[1])
    months = int(time_experience_skill.split('_')[3])
    html = ""

    for year in range(years):
        html += """<li><i class="fa-sharp fa-solid fa-star"></i></li>"""
    if months != 0 or months == 0 and years == 0:
        html += """<li><i class="fa-solid fa-star-half-stroke"></i></li>"""
    return html


IMAGE_EXTENSIONS = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
}


def image_resize(field_img, size=(1280, 720)):
    with Img.open(field_img) as img:
        if img.width > size[0] or img.height > size[1]:
            output_size = size
            img.thumbnail(output_size, Img.LANCZOS)
            img_filename = Path(field_img.file.name).name
            img_suffix = Path(field_img.file.name).name.split(".")[-1]
            img_format = IMAGE_EXTENSIONS[img_suffix]
            buffer = BytesIO()
            img.save(buffer, format=img_format)
            file_object = File(buffer)
            field_img.save(img_filename, file_object)


def make_thumbnail(instance, field_img: str, field_thumbnail: str, size=(80, 80)):
    image = Img.open(getattr(instance, field_img))

    image.thumbnail(size, Img.ANTIALIAS)
    thumbnail_name, thumbnail_extension = os.path.splitext(getattr(instance, field_img).name)
    thumbnail_file = thumbnail_name + '_thumbnail' + thumbnail_extension

    extension = IMAGE_EXTENSIONS[thumbnail_extension[1:]]

    temp_thumb = BytesIO()
    image.save(temp_thumb, extension)
    temp_thumb.seek(0)

    getattr(instance, field_thumbnail).save(thumbnail_file, ContentFile(temp_thumb.read()), save=False)
    temp_thumb.close()
    return True
