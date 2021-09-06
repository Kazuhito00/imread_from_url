#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from io import BytesIO

import cv2
import numpy as np
from PIL import Image


def imread_from_url(url, seek_index=0, debug=False):
    image = None

    # URLから画像を取得
    response = requests.get(url)

    # PILでURLの画像を読み込み
    try:
        image = Image.open(BytesIO(response.content))
    except Exception as e:
        print(e)
        return None

    if debug:
        print(image)
        print(image.size)
        print(dir(image))

    # アニメーションGIF等の複数枚ある画像はシーク
    if 'n_frames' in dir(image):
        if image.n_frames > 1:
            if debug:
                print('n_frames', image.n_frames)
                print('seek_index', seek_index)
            image.seek(seek_index)
        else:
            image.seek(0)

    # RGB -> BGR
    image = cv2.cvtColor(np.array(image, dtype=np.uint8), cv2.COLOR_RGB2BGR)

    return image


if __name__ == '__main__':
    image = imread_from_url(
        'https://github.com/Kazuhito00/Kazuhito00/blob/master/image/icon350.jpg?raw=true',
        debug=True,
    )

    cv2.imshow('Sample', image)
    cv2.waitKey(-1)
