from config import TOKEN, CHANNELID
from db import Sqlite
import datetime
import time
import requests
import schedule  

db = Sqlite('db.db')

time1 = datetime.time(10, 00, 00)
time2 = datetime.time(20,00,00)

def send():


    while True:
        current_date_time = datetime.datetime.now()
        # current_time = current_date_time.time().strftime('%H:%M:%S')
        stringus = current_date_time.strftime('%H:%M:%S')
        now = datetime.datetime.strptime(stringus, '%H:%M:%S').time()
        if now >= time1 and now <= time2:
            photo_id = db.get_first()[0]  
            
            for user_id in db.get_user():
                print(0)
                # print(user_id)
                response = requests.post(
        url=f'https://api.telegram.org/bot{TOKEN}/forwardMessage',
        data={f'chat_id': {user_id[0]}, 'from_chat_id': {CHANNELID}, 'message_id': {photo_id}}
    ).json()
            db.delete(photo_id)   

        
def main():
    schedule.every().hour.do(send)
    while True:
        time.sleep(1)
        schedule.run_pending()


if __name__ == '__main__':
    main()
