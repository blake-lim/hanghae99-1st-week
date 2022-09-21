from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://rbqjachl95:*rb3080qja*@Cluster0.0zxvr1x.mongodb.net/?retryWrites=true&w=majority')
db = client.marry_list


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/addr', methods=['POST'])
def mongo_save():
   doc = {
      'ID': "진",
      'PW': "123456",
      'D_Day': "2019-01-01",
      'PX': request.form['PX'],
      'PY': request.form['PY'],
      'PNAME': request.form['PNAME']
   }
   db.user_info.insert_one(doc)
   return jsonify({'msg': '회원가입 완료'})

#로그인 완료후#
#POST를 통해 ID를 가져옴
ID = "진"

#GET으로 좌표 및 주소 이름을 전달해줌
@app.route('/map')
def map():
   return render_template('map.html')

@app.route('/pos', methods=['GET'])
def mongo_pos():
   #받은 ID에 대한 데이터를 가져옴
   position_dict = list(db.user_info.find({'ID':ID},{'_id':False}))
   print(position_dict)
   return jsonify({'position_info': position_dict})

if __name__ == '__main__':
   app.run('0.0.0.0', port=80, debug=True)
