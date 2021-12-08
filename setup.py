from setuptools import setup, find_packages

setup(
    name='imread_from_url',
    version='0.1.2',
    license='Apache License, Version 2.0',
    description=
    'Read the image from the specified URL and enable it to be handled by OpenCV',
    author='Kazuhito Takahashi',
    url='https://github.com/Kazuhito00/imread_from_url',
    packages=find_packages(),
    install_requires=[
        'opencv-python>=3.4.2',
        'Pillow>=6.1.0',
        'requests>=2.22.0',
    ],
)
