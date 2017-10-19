#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
import os
import shutil
'''
将sourcefold文件夹下的所有文件放到targetfold文件夹中
重复的文件名前面加前缀:copy_
'''
fin_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'sourcefold')
fout_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'targetfold')

tuples=os.walk(fin_path) #返回生成器
for tup in tuples:
  #tup=(dirpath,dirnames,filename)
  #dirpath:是一个字符串,该目录的路径;
  #dirnames:是dirpath子目录的名称列表;
  #filename:是dirpath中的非目录的名称列表.
  # print tup
  files=tup[2] #tup[2]为tup[0]目录下的文件列表
  if files: #不为[]
    for file in files:
      sourcefile_path=os.path.join(tup[0], file)
      targetfile_path=os.path.join(fout_path, file)
      while True: #防止重名文件
        if os.path.exists(targetfile_path): #判断文件是否已存在
          head,tail=os.path.split(targetfile_path)
          targetfile_path=os.path.join(head, 'copy_'+tail)
        else:
          break
      shutil.copyfile(sourcefile_path,targetfile_path)
      #注:若目标文件夹下已存在该文件名,则将会覆盖
