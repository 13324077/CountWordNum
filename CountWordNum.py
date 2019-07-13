#!/usr/bin/env python
# coding: utf-8
'''
Created on July 05, 2019
Update  on 2019-07-05
Author: Jackle
'''

# for line in open("/Users/macos/Desktop/deep-learning-in-digital-pathology-analysis.pdf"):
#     print(line, end='')

from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
import re

def read_pdf(pdf):
    # resource manager
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    # device
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdf)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    # 获取所有行
    lines = str(content).split("\n")

    word_lst = []
    for stri in lines:

        match_pattern = re.findall(r'\b[a-z]{3,15}\b', stri)

        for word in match_pattern:
            # count = frequency.get(word, 0)
            # frequency[word] = count + 1
            word_lst.append(word)

        # print(word_lst)
    return word_lst


if __name__ == '__main__':
    with open('Detecting Cancer Metastases on Gigapixel Pathology Images.pdf', "rb") as my_pdf:
        wordList = read_pdf(my_pdf)
        print(wordList)
        print(len(wordList))