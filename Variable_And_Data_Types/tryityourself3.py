guest = ['john','amanda','niki']

print(f'Hello! {guest[0].title()}. I would like to invit you to my party.')
print(f'Hello! {guest[1].title()}. I would like to invit you to my party.')
print(f'Hello! {guest[2].title()}. I would like to invit you to my party.')

cant_make_it = guest.pop(0) # popped out john

print(f'Hello Guys! {cant_make_it.title()} won\'t be coming because he has urgent meeting.')

guest.insert(2,'Terry') # adding Terry to list

print(f"Hello {guest[-1].title()} Thank you for coming Today!")

print(f"Guys We have got {guest[-1].title()} coming to party!")

print(f"Hello {guest[0].title()}, {guest[1].title()}, {guest[2].title()}. \nI will be inviting three more guest since i bigger talbe was reserved!")

guest.insert(0,'Miho')
guest.insert(2,'Su')
guest.append('Gaby')

print(f"Here are the list of our new guests:\n\t1:{guest[0]}\n\t2:{guest[2]}\n\t3:{guest[-1]} ")



print(f'Hello! {guest[0].title()}. I would like to invit you to my party.')
print(f'Hello! {guest[2].title()}. I would like to invit you to my party.')
print(f'Hello! {guest[-1].title()}. I would like to invit you to my party.')

for person in guest[:]:  # Loop over a copy for safe removal
    if person != 'Miho' and person != 'Su':
        print(f"Hello {person.title()}, I need to cancel my party because the table didnt arrive on time. So sorry!")
        guest.remove(person)
    else:
        print(f"Hello {person.title()}! The party is still ON! Let Rock")
    

del guest[0]
del guest[0]
print(guest)










  

