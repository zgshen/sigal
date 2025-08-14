Sigal - Simple Static Gallery Generator
=======================================

Fork by Sigal_

- 新增主题 moments；
- 新增插件 media_metadata，用于设置相册和图片信息；
- 部署仓库 https://github.com/zgshen/gallery
- moments 主题下的相册和图片信息可以通过 media_metadata 插件设置，每个相册下可以用 json 文件设置一些信息：
  ```
  {
    "title": "相册名",
    "description": "相册描述",
    "custom_thumbnail": "相册封面",
    "datetime": "202508080000",
    "images": {
      "test.jpg": {
        "description": "图片描述",
      }
    }
  }  
  ```
.. _Sigal: https://github.com/saimn/sigal/
