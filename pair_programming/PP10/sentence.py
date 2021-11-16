#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File : sentence.py
Created : Tue Nov 9 2021
Coder : Ling Feng
Listener : Ivy Yao,Selina Qian
"""
import reprlib

class Sentence: # An iterable
    def __init__(self, text):
        self.text = text
        self.words = text.split()

    def __iter__(self):
        for i in range(len(self.words)):
            yield self.words[i]

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

#demos
def main():
    s = Sentence("This is a demo sentence")
    for i in s:
        print(i)

if __name__ == "__main__":
    main()
