from config import TOKEN, CHANNELID
from db import Sqlite
import datetime
import time
import requests

db = Sqlite('db.db')

time1 = datetime.time(10, 00, 00)
time2 = datetime.time(20,00,00)

def send():
    while True:
        photo_id = db.get_first()[0]    
        current_date_time = datetime.datetime.now()
        # current_time = current_date_time.time().strftime('%H:%M:%S')
        stringus = current_date_time.strftime('%H:%M:%S')
        now = datetime.datetime.strptime(stringus, '%H:%M:%S').time()
        if now >= time1 and now <= time2:
            for user_id in db.get_user():
                response = requests.post(
        url=f'https://api.telegram.org/bot{TOKEN}/forwardMessage',
        data={f'chat_id': {user_id}, 'from_chat_id': {CHANNELID}, 'message_id': {photo_id}}
    ).json()
        db.delete(photo_id)   
        time.sleep(3600)
        
if __name__ == '__main__':
    send()
