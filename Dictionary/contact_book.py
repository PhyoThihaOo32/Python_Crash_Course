contacts = {}

def add_contact():
    name = input('Enter contact name: ').strip().title()
    if name in contacts:
        print('This contact already exists')
    else:
        phone = input('Enter phone number: ').strip()
        email = input('Enter email address: ').strip().lower()
        contacts[name] = {'Phone' : phone, 'Email': email}
        print(f'Contact {name} added.')

def search_contact():
    name = input('Enter name to search: ').strip().title()
    if name in contacts:
        print(f'Found contact: {name}')
        for key, value in contacts[name].items():
            print(f'    {key}: {value}')
    else:
        print('Contact not found.')

def delete_contact():
    name = input('Enter name to delete: ').strip().title()
    if name in contacts:
        del contacts[name]
        print(f'Contact {name}, deleted.')
    else:
        print('Contact not found')

def show_all_contacts():
    if contacts:
        print(f'\n\tContacts Lists:')
        for name, info in contacts.items():
            print(f'\n{name} ') # {info} 
            for key, value in info.items():
                print(f'{key}: {value}')
    else:
        print('Your contact book is empty')

#Menu Loop
while True:
    print('''
Contact Book Operation Menu:
          1. Add Contact
          2. Search Contact
          3. Delete Contact
          4. Show All Contact
          5. Exit
''')
    
    choice = (input('Choose an option 1-5: '))

    if choice == '1':
      add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        show_all_contacts()
    elif choice == '5':
        print('Closing the Contact Book...')
        break
    else:
        print('Invalid option. Please try again.')
