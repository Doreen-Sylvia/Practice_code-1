fp=open('note.txt','w')#打开文件  w->write
print('北京欢迎你',file=fp)#输入到文件中
fp.close()#关闭文件

fp=open('text.txt','w')
print('人生苦短，我用python',file=fp)
fp.close()