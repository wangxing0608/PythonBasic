# _*_ coding:utf-8 _*_
from nntplib import NNTP
from time import strftime
from time import time
from time import localtime


day = 24*60*60   # 一天的秒数

yesterday = localtime(time() - day)
date = strftime('%y%m%d', yesterday)
hour = strftime('%H%M%S', yesterday)

servername = 'news.gmane.org'    # 替换为网上
group = 'gmane.comp.python.apple'
server = NNTP(servername)

ids = server.newnews(group, date, hour)[2]

for id in ids:
    head = server.head(id)[3]
    for line in head:
        if line.lower().startwith('subject'):
            subject = line[9:]
            break
    body = server.body(id)[3]
    print subject
    print '-'*len(subject)
    print '\n'.join(body)

server.quit()
