from flask import Flask, jsonify, redirect, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongofirst:27017,mongosecond:27017,mongothird:27017/?replicaSet=r$db = client.mymongodb
tasks_collection = db.task
initial_tasks = [task for task in tasks_collection.find()]

if (len(initial_tasks)) < 6:
    tasks_collection.insert({
        'title': 'Hi!'
    })
    tasks_collection.insert({
        'title': 'Hey!'
    })

    tasks_collection.insert({
        'title': 'How are you?'
    })
    tasks_collection.insert({
        'title': 'Good, thanks!'
    })
    tasks_collection.insert({
        'title': 'Cool. Bye.'
    })


@ app.route('/', methods=['GET'])


def get_tasks():
    all_tasks = tasks_collection.find()
    task_list = []
    for task in all_tasks:
        task_list.append({'title': task['title']})
    return render_template('index.html', task_list=task_list)


@app.route('/send/<string:task>', methods=['GET'])
def create_task(task):
    new_task = {"title": task}
    tasks_collection.insert(new_task)
    return redirect('/')


@app.route('/test', methods=['GET'])
def test():
    return render_template('index.html', task_list=task_list)
    # return jsonify({'msg': 'This is a Test'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)