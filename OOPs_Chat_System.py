class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def __str__(self):
        return f"{self.sender.username}: {self.text}"


class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def join(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"{user.username} joined the chat room.")
        else:
            print(f"{user.username} is already in the chat room.")

    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.username} left the chat room.")
        else:
            print(f"{user.username} is not in the chat room.")

    def send_message(self, user, text):
        if user in self.users:
            message = Message(user, text)
            self.messages.append(message)
            print(f"Message sent by {user.username}")
        else:
            print(f"{user.username} must join the chat room first.")

    def show_history(self):
        print("\n--- Chat History ---")

        if not self.messages:
            print("No messages yet.")
            return

        for message in self.messages:
            print(message)

    def show_users(self):
        print("\n--- Users in Chat Room ---")

        if not self.users:
            print("No users in the chat room.")
            return

        for user in self.users:
            print(user.username)


# Creating users
user1 = User("Chandan")
user2 = User("Rahul")
user3 = User("Amit")


# Creating chat room
room = ChatRoom("Python Developers")


# Users joining
room.join(user1)
room.join(user2)
room.join(user3)


# Sending messages
room.send_message(user1, "Hello everyone!")
room.send_message(user2, "Hello Chandan!")
room.send_message(user3, "How are you all?")


# Display users
room.show_users()


# Display chat history
room.show_history()


# User leaving
room.leave(user2)


# Display users again
room.show_users()