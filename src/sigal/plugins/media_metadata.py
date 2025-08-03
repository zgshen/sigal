# media_metadata.py
import os
import json
from sigal import signals

def load_media_json(album):
    """读取相册目录下的 media.json 文件，并设置 media.title / media.description。"""
    json_path = os.path.join(album.src_path, "media.json")
    
    if not os.path.isfile(json_path):
        # 没有 media.json 就跳过
        #print(json_path, "does not exist, skipping.")
        return
    print(json_path)
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            metadata = json.load(f)
    except Exception as e:
        print(f"Failed to load media.json in {album.src_path}: {e}")
        return

    for media in album.medias:
        filename = os.path.basename(media.url)
        meta = metadata.get(filename)
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