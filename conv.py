#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pinyin
import os
import eyed3

rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        # print(fname)
        if fname != "conv.py" and fname != ".DS_Store":
            audiofile = eyed3.load(fname)
            if audiofile is not None:
                if audiofile.tag is not None:
                    if audiofile.tag.title is not None:
                        audiofile.tag.title = unicode(pinyin.get(audiofile.tag.title).encode("utf-8"), "utf-8")
                    if audiofile.tag.album is not None:
                        audiofile.tag.album = unicode(pinyin.get(audiofile.tag.album).encode("utf-8"), "utf-8")
                    if audiofile.tag.artist is not None:
                        audiofile.tag.artist = unicode(pinyin.get(audiofile.tag.artist).encode("utf-8"), "utf-8")
                    if audiofile.tag.album_artist is not None:
                        audiofile.tag.album_artist = unicode(pinyin.get(audiofile.tag.album_artist).encode("utf-8"), "utf-8")
                    audiofile.tag.save()
