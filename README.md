# imread_from_url
指定されたURLから画像を読み取り、OpenCV形式で返す関数です。<Br>
Read the image from the specified URL and enable it to be handled by OpenCV.
 
# Requirement
* OpenCV 3.4.2 or later
* Pillow 6.1.0 or later
 
# Installation
以下のいずれかの方法をご利用ください。
* 利用したいPythonプログラムと同階層にimread_from_urlディレクトリをコピーする。<br>
* GitHub URLを指定しpipインストールする。<Br>
```bash
pip install git+https://github.com/Kazuhito00/imread_from_url
```
* PyPIからインストールする。<Br>
```bash
pip install imread-from-url
```
 
# Usage
使用例は以下です。
 
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

