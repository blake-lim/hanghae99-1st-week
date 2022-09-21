from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from bson.objectid import ObjectId
from pymongo import MongoClient
client = MongoClient('mongodb+srv://minhyeonhong:m1245415@cluster0.1xfvvjw.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/users", methods=["POST"])
def get_user():
    user = list(db.users.find({}, {'_id': False}))
    return jsonify({'user': user})

@app.route("/main", methods=["GET"])
def main_get():
    try:
        id = request.args.get('id')  # 'id'라는 key값

        check_list = list(db.check_list.find({'id':id}).sort('day'))
    except Exception as e:
        print(e)

    return render_template('main.html', check_list=check_list)

@app.route("/main/add", methods=["POST"])
def content_post():
    try:
        mywork = request.form['mywork']
        mydate = request.form['mydate']
        user = request.form['user']

        doc = {'id': user, 'work': mywork, 'day': mydate, 'done': 0}
        db.check_list.insert_one(doc)
        msg = '등록 완료!'

        # 같은 날짜 못넣게 하기 (노쓸모)
        # check_list = list(db.check_list.find({'id':user,'day':mydate}, {'_id': False}))
        # if(len(check_list) == 0):
        #      db.check_list.insert_one(doc)
        #      msg = '등록 완료!'
        # else:
        #      msg = '같은 날짜의 할 일이 있네요 ㅠㅠ'
    except Exception as e:
        print(e)
        msg = '등록 실패'

    return jsonify({'msg': msg})

@app.route("/main/modDone", methods=["POST"])
def modDone():
    try:
        userId = request.form['userId']
        _id = request.form['_id']
        done = request.form['done']

        if (int(done) == 1):
            msg = '할 일 완료!'
        elif (int(done) == 0):
            msg = '할 일 취소!'

        db.check_list.update_one({'_id': ObjectId(_id),'id':userId}, {'$set': {'done': int(done)}})

    except Exception as e:
        print(e)
        msg = '에러'

    return jsonify({'msg': msg})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
