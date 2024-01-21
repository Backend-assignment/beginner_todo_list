from tinydb import TinyDB, Query
from tinydb.table import Document

class TodoList:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = TinyDB(db_path, indent=4)
        self.texts = self.db.table('texts')
        self.users = self.db.table('users')

    def add_plan(self, message_id: str, text_id: str, text: str):
        messages = Document({'text_id': text_id, 'text': text}, doc_id=message_id)
        self.texts.insert(messages)

    def get_plan(self):
        return self.texts.all()

    def add_done(self, message_id: str, text_id: str):
        if self.users.contains(doc_id=message_id):
            user_doc = self.users.get(doc_id=message_id)
            user_doc[text_id] = {'done':True, 'failed': False}
        else:
            user_doc = {text_id: {'done': True, 'failed': False}}
        user_text = Document(user_doc, doc_id=message_id)
        self.users.insert(user_text)

    def add_failed(self, message_id: str, text_id: str):
        if self.users.contains(doc_id=message_id):
            user_doc = self.users.get(doc_id=message_id)
            user_doc[text_id] = {'done': False, 'failed': True}
        else:
            user_doc = {text_id: {'done': False, 'failed': True}}
        user_text = Document(user_doc, doc_id=message_id)
        self.users.insert(user_text)

    def get_done_failed(self, text_id: str):
        dones = 0
        faileds = 0
        for user in self.users:
            data = user.get(text_id)
            if data!=None:
                if data['done']:
                    dones+=1
                else:
                    faileds+=1
        return [dones, faileds]
    
    def all_done_failed(self):
        dones = 0
        faileds = 0
        for user in self.users:
            for item in user.values():
                if item['done']:
                    dones+=1
                else:
                    faileds+=1
        return [dones, faileds]
    
# db = TodoList('todo_list.json')
# print(db.add_plan(message_id='2', text_id='0605', text='Salom dunyo'))
# print(db.add_done(message_id='1', text_id='2806'))
# print(db.get_plan())