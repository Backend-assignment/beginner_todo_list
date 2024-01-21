from flask import Flask, request
from todo_list_main import TodoList

app = Flask(__name__)
todolist = TodoList('todo_list_main.json')

@app.route('/')
def home():
    return "Welcome to the home page. Check your tasks through the api."

@app.route('/api/create-tasks', methods=["POST"])
def addtasks():
    if request.method == "POST":
        data = request.get_json()
        id = data['id']
        task = data['task']
        description = data['description']
        completed = data['completed']
        todolist.add_tasks(id=id, task=task, description=description, completed=completed)
    return {"statust":"OK"}

@app.route('/api/tasks/<int:id>')
def tasks_id(id: str):
    return todolist.get_id(id)

@app.route('/api/get-tasks')
def get_tasks():
    return todolist.get_tasks_all()

@app.route('/api/tasks/<int:id>/delete')
def taskid_delete(id: int):
    todolist.tasks_delete(id)
    return {'statust':"ok"}

@app.route('/api/tasks/completed')
def get_completed():
    return todolist.tasks_complated()

@app.route('/api/tasks/incompleted')
def get_incompleted():
    return todolist.tasks_incompleted()

@app.route('/api/tasks/<int:id>/complete')
def get_id_complete(id: int):
    return todolist.id_complete(id)

if __name__=="__main__":
    app.run(debug=True)

