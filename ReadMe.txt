��sourcefold�ļ����µ������ļ��ŵ�targetfold�ļ�����
�ظ����ļ���ǰ���ǰ׺:copy_


tuples=os.walk(fin_path) #����������
for tup in tuples:
  print tup

���:
('E:\\extract-files\\sourcefold', ['smallfold_1', 'smallfold_2', 'smallfold_3'], ['file.txt', 'file_1-1.txt'])
('E:\\extract-files\\sourcefold\\smallfold_1', ['tinyfold_1-1'], ['file_1-1.txt', 'file_1-2.txt'])
('E:\\extract-files\\sourcefold\\smallfold_1\\tinyfold_1-1', [], ['file_1-1-1.txt'])
('E:\\extract-files\\sourcefold\\smallfold_2', [], ['file_1-1.txt', 'file_2-1.txt'])
('E:\\extract-files\\sourcefold\\smallfold_3', [], [])

ע:tup[2]Ϊtup[0]Ŀ¼��զ�ļ��б�