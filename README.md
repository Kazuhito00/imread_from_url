# imread_from_url
 cvoverlayimgはOpenCVで透過PNGを画像の上に重ね合わせるクラスです。
 
# Requirement
* OpenCV 3.4.2 or later
* Pillow 6.1.0 or later
 
# Installation
利用したいPythonプログラムと同階層にimread_from_urlディレクトリをコピーしてください。<Br>

# Usage
サンプルの実行方法は以下です。
 
```python
import cv2

from imread_from_url import imread_from_url

image = imread_from_url(
    'https://github.com/Kazuhito00/Kazuhito00/blob/master/image/icon350.jpg?raw=true'
)

if image is not None:
    cv2.imshow('Sample', image)
    cv2.waitKey(-1)

```

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
imread_from_url is under [Apache-2.0 License](LICENSE).

