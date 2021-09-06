#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2

from imread_from_url import imread_from_url

image = imread_from_url(
    'https://github.com/Kazuhito00/Kazuhito00/blob/master/image/icon350.jpg?raw=true'
)

if image is not None:
    cv2.imshow('Sample', image)
    cv2.waitKey(-1)
