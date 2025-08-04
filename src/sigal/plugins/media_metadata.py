# media_metadata.py
import os
import json
from sigal import signals

def load_media_json(album):
    json_path = os.path.join(album.src_path, "media.json")
    if not os.path.exists(json_path):
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 设置 album.title 和 album.description
    album.title = data.get("title", album.title)
    album.description = data.get("description", album.description)
    # 设置 album.custom_thumbnail
    thumb = data.get("custom_thumbnail")
    if thumb:
      album.custom_thumbnail = os.path.join(album.url, "thumbnails/", thumb)

    # 设置每张图片的 title 和 description
    images_meta = data.get("images", {})
    for media in album.medias:
        filename = os.path.basename(media.url)
        meta = images_meta.get(filename)
        if meta:
            # title 默认是文件名
            title = meta.get("title", "")
            if title:
                media.title = title
            media.description = meta.get("description", "")
            #print(f"Metadata set for {media.description}")
        #else:
            #print(f"No metadata for {filename} in media.json")


def register(settings):
    #signals.gallery_build.connect(load_media_json)
    signals.album_initialized.connect(load_media_json)