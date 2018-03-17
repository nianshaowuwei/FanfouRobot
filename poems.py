import time
import random
import fanfou
import datetime
import shelve



#请修改为你的consumer
consumer = {'key':'consumer key', 'secret':'consumer secret'}
## 请修改为你的 ID 和密码
client = fanfou.XAuth(consumer, 'username', 'password')
fanfou.bound(client)


with open('poems.txt', encoding='utf8') as f:
    poems = f.readlines()

def check():
    try:
        resp = client.statuses.mentions()


if __name__ == '__main__':
  while True
      now = datatime.datetime.now()
      if now.hour == 8 and now.minute < 1:
        send()
      elif now.hour == 4 and now.minute < 1:
        update()
      elif now.hour %15 == 0:
        check()
        
