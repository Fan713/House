#! /usr/bin/env python
#coding=gbk
from docx import Document
from docx.shared import Inches
import re,os
# import SendKeys
#ģ�����Ctrl+A
# import win32api
# import win32con
# def full_cho():
#     win32api.keybd_event(17, 0, 0, 0)
#     win32api.keybd_event(65, 0, 0, 0)
#     win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
#     win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
#     
t1=r'C:\Users\KLJS154\Desktop\testwe.docx'
document = Document(t1)
for paragraph in document.paragraphs:
#     print(paragraph.text)
#     SendKeys.Sendkeys('A')
#     del(paragraph)
#     full_cho()
    paragraph.clear()
#���벻ͬ�ȼ��ı���
document.add_heading(u'MS WORDд�����',0)
document.add_heading(u'��������23',1)
document.add_heading(u'�������23',2)
#����ı�
document.add_paragraph('���Թ���')
document.save(r'C:\Users\KLJS154\Desktop\testwe.docx')




