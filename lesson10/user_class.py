def send(chat_id, text):
    pass

class User:

    def __init__(self, chat_id, name=None, age=None):
        self.__chat_id = chat_id
        self.__name = name
        self.__age = age

    def send_message(self, text):
        send(self.__chat_id, text)
    

user_list = [
    User(3333, name='Jack'),
    User(231242, name='Olo'),
    User(215213, name='Quack')
]

text = 'Something changed'

for user in user_list:
    user.send_message(text)