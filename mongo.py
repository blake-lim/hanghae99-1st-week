from bson import ObjectId
from pymongo import MongoClient
import datetime
import schedule
import time

def day_re(text):
    print(text)
    client = MongoClient('mongodb+srv://rbqjachl95:*rb3080qja*@Cluster0.0zxvr1x.mongodb.net/?retryWrites=true&w=majority')
    db = client.marry_list

    #필요한 정보만 불러오기
    date = list(db.date_test.find({}, {'_id': 1, 'DATE':1}))
    date_format = "%Y-%m-%d"

    #날짜 수정
    for idx, info in enumerate(date):
        date[idx]['DATE'] = str(datetime.datetime.strptime(info['DATE'], date_format) - datetime.timedelta(days=1)).split(" ")[0]

    #업로드
    [db.date_test.update_one({"_id": info['_id']}, {'$set': {"DATE": info['DATE']}}) for info in date]

schedule.every().day.at("23:59").do(day_re, "하루가 경과함")

while True:
    schedule.run_pending()
    time.sleep(1200)