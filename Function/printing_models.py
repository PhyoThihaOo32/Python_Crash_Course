#starts with some design that need to be printed
unprinted_designs = ['robot', 'spaceship', 'vase', 'phone case', 'keychain']
completed_models = []

def print_model(unprinted_designs, completed_models):

    while unprinted_designs:
         currrent_design = unprinted_designs.pop()
         print(f'Now printing the model: {currrent_design}')
         completed_models.append(currrent_design)

# display all completed models

def show_completed_model(completed_models):
    print('The Following models have been printed successfully.')
    for index, completed_model in enumerate(completed_models, start=1):
         print(f'{index}: {completed_model}')


print_model(unprinted_designs, completed_models)
show_completed_model(completed_models)
