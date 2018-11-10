功能描述： 
将sourcefold文件夹下的所有文件放到targetfold文件夹中 
重复的文件名前面加前缀:copy_
```
tuples=os.walk(fin_path) #返回生成器
for tup in tuples:
  print tup
```
输出:
('E:\\extract-files\\sourcefold', ['smallfold_1', 'smallfold_2', 'smallfold_3'], ['file.txt', 'file_1-1.txt'])
('E:\\extract-files\\sourcefold\\smallfold_1', ['tinyfold_1-1'], ['file_1-1.txt', 'file_1-2.txt'])
('E:\\extract-files\\sourcefold\\smallfold_1\\tinyfold_1-1', [], ['file_1-1-1.txt'])
('E:\\extract-files\\sourcefold\\smallfold_2', [], ['file_1-1.txt', 'file_2-1.txt'])
('E:\\extract-files\\sourcefold\\smallfold_3', [], [])

注:tup[2]为tup[0]目录下的文件列表
