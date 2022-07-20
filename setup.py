# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='youtube_dl_server',
    version='0.4',
    description='Api server to get youtube data',
    long_description='Used with youtube unity plugin',
    author='Kelvin Rosa and Jaime Marquínez',
    author_email='kelvinparkour@gmail.com',
    url='lightshaft facebook',
    packages=['youtube_dl_server'],
    entry_points={
        'console_scripts': [
            'youtube-dl-server = youtube_dl_server.server:main',
        ],
    },

    install_requires=[
        'Flask',
        'Flask-Limiter',
        'git+git://github.com/yt-dlp/yt-dlp.git',
        'pycryptodomex',
    ],

    classifiers=[
        'Topic :: Multimedia :: Video',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: Public Domain',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
