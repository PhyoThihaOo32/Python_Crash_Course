import random

class Lottery:
    def __init__(self):
        self.winning_ticket = []
        self.player_ticket = []

    def generate_winning_ticket(self):
        self.winning_ticket = [random.randint(0, 9) for _ in range(4)]
        print(f'Winning Ticket: {self.winning_ticket}')

    def randomly_generate_player_ticket(self):
        self.player_ticket = [random.randint(0, 9) for _ in range(4)]
        print(f'Your random ticket: {self.player_ticket}')

    def user_manually_generate_ticket(self):
        print('Enter 4 digits (0-9) for your lottery ticket:')
        self.player_ticket = []
        for i in range(4):
            while True:
                try:
                    num = int(input(f'Digit {i+1}: '))
                    if 0 <= num <= 9:
                        self.player_ticket.append(num)
                        break
                    else:
                        print('Please enter a digit between 0 and 9.')
                except ValueError:
                    print('Please enter a valid number.')

    def check_ticket(self):
        if self.player_ticket == self.winning_ticket:
            print("🎉 Congratulations! You won the lottery!")
        else:
            print("😢 Better luck next time.")
            self.generate_winning_ticket()
            

# ==== MAIN PROGRAM ====
my_lottery = Lottery()

choice = input("Do you want to pick numbers yourself? (y/n): ").lower()

if choice == 'y':
    my_lottery.user_manually_generate_ticket()
else:
    my_lottery.randomly_generate_player_ticket()

my_lottery.check_ticket()
