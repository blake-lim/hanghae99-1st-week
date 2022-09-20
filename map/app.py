from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import datetime

app = Flask(__name__)
client = MongoClient('mongodb+srv://rbqjachl95:*rb3080qja*@Cluster0.0zxvr1x.mongodb.net/?retryWrites=true&w=majority')
db = client.marry_list


@app.route('/')
def home():
   return render_template('index2.html')

@app.route('/addr', methods=['POST'])
def mongo_save():
   doc = {
      'ID': "최규범",
      'PW': "123456",
      'D_Day': datetime.datetime(2019, 1, 1,1),
      'PX': request.form['PX'],
      'PY': request.form['PY'],
      'PNAME': request.form['PNAME']
   }
   db.user_info.insert_one(doc)
   return jsonify({'msg': '회원가입 완료'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=80, debug=True)
