from tinydb import TinyDB, Query
from tinydb.table import Document
from datetime import datetime
q = Query()
class TodoList:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = TinyDB(db_path, indent=4)
        self.tasks = self.db.table('tasks')

    def add_tasks(self, id: int, task: str, description: str, completed: bool):
        date = datetime.now()
        f = "%Y-%m-%d %H:%M:%S"
        date = date.strftime(f)
        message = Document({'id': id, "task": task, "description": description, "completed": completed, "created_at": date, "update_at": date}, doc_id=id)
        self.tasks.insert(message)

    def get_id(self, id: int):
        task_id = self.tasks.search(q.id==id)
        return task_id
    
    def get_tasks_all(self):
        task_all = self.tasks.all()
        return task_all
    
    def tasks_delete(self, id: int):
        self.tasks.remove(q.id==id)

    def tasks_complated(self):
        completed = self.tasks.search(q.completed==True)
        return completed
    
    def tasks_incompleted(self):
        incompleted = self.tasks.search(q.completed==False)
        return incompleted
    
    def id_complete(self, id: int):
        comp = self.tasks.search(q.id ==id)
        if comp[0]['completed']==True:
            return "Vazifa to'liq bajarilgan"
        else:
            return "Vazifa to'liq bajarilmagan"
        

if __name__=="__main__":
    db = TodoList('todo_list_main.json')
    # print(db.get_id(1))
    # print(db.get_tasks_all())
    # print(db.tasks_delete(3))
    # print(db.tasks_incompleted())
    # print(db.id_complete(1))

