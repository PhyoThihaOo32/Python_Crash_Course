def show_messages(messages):
    if not messages:
        print('--- No Messages in the Inbox----')
        return # exits the function early
    for message in messages:
        print(f'Here are messages to be send: {message}')

def send_messages(messages,sent_messages = None):
    if sent_messages is None:
        sent_messages = []
    while messages:
         current_message = messages.pop()
         print(f'Sending current message: {current_message}')
         sent_messages.append(current_message)
    return sent_messages
    
 
    

random_messages = [
    "Hello, world!",
    "Python is awesome!",
    "Keep learning every day.",
    "Functions make code reusable.",
    "Debugging is fun!"
]


print("Sending messages: ")
send_messages(random_messages[:])
show_messages(random_messages)