# enumerate - use when you need both index and value while looping through a list (or any iterable)

# syntax: for index, value in enumerate(iterable, start=0):

# items = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# for index, value in enumerate(items, start=0):
#     print(f'{index + 1}: {value}')


# 🎯 Building a to-do list app with numbered tasks

def daily_task_checker():
    tasks = [
        "Buy groceries",
        "Call Alice",
        "Finish Python project",
        "Read a book",
        "Go for a walk"
    ]
    
    print('\n📝 "Things to do 😃"\n')
    for index, task in enumerate(tasks, start=1):
        print(f'{index}: {task}')

    try:
        task_number = int(input('\n🔢 Enter a number to mark it done: '))
        if 1 <= task_number <= len(tasks):
            print(f'✅ Task completed: {tasks[task_number - 1]}')
        else:
            print("⚠️ Invalid input 😒")
    except ValueError:
        print("❌ Please enter a valid number 🤖")

daily_task_checker()
