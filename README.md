# imread_from_url
指定されたURLから画像を読み取り、OpenCV形式で返す関数です。<Br>
Read the image from the specified URL and enable it to be handled by OpenCV.
 
# Note(2022年1月21日追記)
実行時に以下のようなエラーが発生するケースがあります。<br>
その場合、もう一度`imread_from_url()`を実行するか`!pip install imread_from_url==0.1.2`で旧バージョンをインストールしてください。
```
Error occurred during loading data. Trying to use cache server https://fake-useragent.herokuapp.com/browsers/0.1.11
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/dist-packages/fake_useragent/utils.py", line 154, in load
    for item in get_browsers(verify_ssl=verify_ssl):
  File "/usr/local/lib/python3.7/dist-packages/fake_useragent/utils.py", line 99, in get_browsers
    html = html.split('<table class="w3-table-all notranslate">')[1]
IndexError: list index out of range
```
 
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

