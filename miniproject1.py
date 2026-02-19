class user:
    def __init__(self , name):
        self.name = name

class message:
    def __init__(self , sender, content):
        self.sender = sender
        self.content = content  

class chatroom():
    def __init__(self):
      self.member_list = []
      self.message_list = []
    def join (self , person):
        self.member_list.append(person)
        print(self.member_list)
        print(person.name ,"joined the chatroom")

    def leave(self , person):
        if person in self.member_list:
            self.member_list.remove(person)
            print(person.name ,"left the chatroom")
    def send_message(self , person , text):  
        if person in self.member_list:
            msg = message(person.name , text)
            self.message_list.append(msg)
            print(person.name ,"sent a message :", text)
        else:
            print(person.name ,"is not a member of the chatroom")  
    def view_chat_history(self):
        for msg in self.chat_messages:
            print(msg.sender_name + ":", msg.message_text)    


user1 = user("Alice")
user2 = user("Bob")     
chatroom1 = chatroom()  
chatroom1.join(user1)
chatroom1.send_message(user1 , "Hello, everyone!")
chatroom1.join(user2)

chatroom1.send_message(user2 , "Hi, Alice!")