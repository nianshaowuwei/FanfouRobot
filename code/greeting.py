import time
import random
import shelve
import datetime
import fanfou

# 请修改为你的 Consumer
consumer = {'key': 'consumer key', 'secret': 'consumer secret'}
# 请修改为你的 ID 和密码
client = fanfou.XAuth(consumer, 'username', 'password')
fanfou.bound(client)
