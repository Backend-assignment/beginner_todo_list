from flask import Flask, request
from todo_list import TodoList

app = Flask(__name__)
todoList = TodoList('todo_list.json')

@app.route('/')
def home():
    return "Welcome to the home page. Check your tasks through the api."

@app.route('/api/tasks',methods=["GET"])
def tasks():
    return todoList.get_plan()

@app.route('/api/addText', methods=['POST'])
def addText():
    if request.method=="POST":
        data = request.get_json()
        message_id=data['message_id']
        text_id = data['text_id']
        text = data['text']
        todoList.add_plan(message_id=message_id, text_id=text_id, text=text)
    return {"statust":"OK"}

@app.route('/api/addDone', methods=["POST"])
def addDone():
    if request.method=="POST":
        data = request.get_json()
        message_id = data['message_id']
        text_id = data['text_id']
        todoList.add_done(message_id=message_id, text_id=text_id)
    return {'statusts':"OK"}

@app.route('/api/addFailed', methods=["POST"])
def addFailed():
    if request.method=="POST":
        data = request.get_json()
        message_id = data['message_id']
        text_id = data['text_id']
        todoList.add_failed(message_id=message_id, text_id=text_id)
    return {"statust":"OK"}

@app.route('/api/getDoneFailed', methods=['POST'])
def get_done_failed():
    if request.method=="POST":
        data = request.get_json()
        text_id = data['text_id']
        return todoList.get_done_failed(text_id=text_id)
     

@app.route("/api/alldonefailed", methods=["POST"])
def all_done_failed():
    data = todoList.all_done_failed()
    return {
        "dones":data[0],
        "faileds":data[-1]
    }

if __name__ == "__main__":
    app.run(debug=True, port=8000)
