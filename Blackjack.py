import pygame
import random
import math
import time

SCREEN_W = 500
SCREEN_H = 500
running = True
balance = 10000
balance = int(balance)
loop = True

def cards():
    print("dealing cards...")
    time.sleep(1)
    card1 = random.randint(1,11)
    print(card1)
    time.sleep(1)
    card2 = random.randint(1,11)
    print(card2)
    time.sleep(1)
    total = card1 + card2
    if total > 21:
        total = 12
    if total == 21:
        print("blackjack! You win")
    else:
        print("your total is", total)
        dealercard1 = random.randint(1,11)
        dealercard2 = random.randint(1,11)
        print("one of the dealer cards is", dealercard1)
        choice1 = input("would you like to hit or stand?")
        while choice1.strip() == "hit" or choice1.strip() == "Hit":
            card3 = random.randint(1,11)
            print(card3)
            time.sleep(1)
            total = card3+total
            if total > 21:
                print("your total is",total)
                print("oops you busted!")
                print("dealer wins!")
                print("you lost", bet1)
                break
            else:
                print("your new total is", total)
            choice1 = input("would you like to hit or stand?")
            if choice1.lower() == 'stand':
                break
        while choice1.strip() == "stand" or choice1.strip() == "Stand":
                time.sleep(1)
                print("your final total is", total)
                break
        dealertotal = dealercard1+dealercard2
        if total <=21:
            print("the dealer has", dealertotal)
            while dealertotal < total:
                print("dealer hits")
                time.sleep(1)
                dealercard3 = random.randint(1,11)
                time.sleep(1)
                print(dealercard3)
                dealertotal = dealertotal+dealercard3

                if dealertotal > 21:
                    print("dealers total...", dealertotal)
                    print("dealer busted")
                    print("you win!!", bet1)
                    print("your new balance is $",balance+int(bet1))
            if dealertotal >= total and dealertotal <= 21:
                print("the dealer has", dealertotal)
                print("you lose! $",bet1)


while loop == True:
    while balance > 0:
        bet1 = input("how much would you like to bet?")
        bet1 = int(bet1)
        while bet1 > balance:
            print("you can't bet more than you have!")
            bet1 = int(input("how much would you like to bet?"))
        else:
            balance = balance - bet1
            print("your new balance is $",balance)
            break



    cards()

    if balance < 1:
        print('you lost all your money')
        loop = False
    else:
        playagain = input("wanna play again? ")
        if playagain.lower().startswith('n'):
            print('pleasure playing with you!')
            print('Your final balance: ...$',balance)
            loop = False
        elif playagain.lower().startswith('y'):
            print('glad to hear!')
        else:
            while playagain.lower().startswith('n') == False and playagain.lower().startswith('y') == False:
                print("i don't understand")
                time.sleep(0.5)
                playagain = input("wanna play again?")
                if playagain.lower().startswith('n'):
                    running = False
                    print('okay bye')
                    print('Your final balance: $',balance)
                    loop = False
                elif playagain.lower().startswith('y'):
                    print('glad!')
                    break


import random
import time

class Roulette:
    def __init__(self):
        self.wheel = [i for i in range(37)] + [00]


         # American Roulette has numbers 0-36 and a 00


    def spin(self):
        return random.choice(self.wheel)

    def bet_number(self, number, bet_amount):
        print("Spinning the wheel...")
        time.sleep(5)
        result = self.spin()
        print(f"The ball landed on: {result}")
        if result == number:
            return bet_amount * 35
        else:
            return -bet_amount

    def bet_color(self, color, bet_amount):
        red_numbers = set([1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36])
        black_numbers = set([2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35])
        print("Spinning the wheel...")
        time.sleep(5)
        result = self.spin()
        print(f"The ball landed on: {result}")
        if (color == "red" and result in red_numbers) or (color == "black" and result in black_numbers):
            return bet_amount
        else:
            return -bet_amount

    def bet_odd_even(self, bet, bet_amount):
        print("Spinning the wheel...")
        time.sleep(5)
        result = self.spin()
        print(f"The ball landed on: {result}")
        if (bet == "odd" and result % 2 != 0) or (bet == "even" and result % 2 == 0):
            return bet_amount
        else:
            return -bet_amount

    def bet_high_low(self, bet, bet_amount):
        print("Spinning the wheel...")
        time.sleep(5)
        result = self.spin()
        print(f"The ball landed on: {result}")
        if (bet == "high" and 19 <= result <= 36) or (bet == "low" and 1 <= result <= 18):
            return bet_amount
        else:
            return -bet_amount

def main():
    game = Roulette()
    balance = 10000
    # Starting balance

    while True:
        print(f"Current balance: ${balance}")
        print("Choose your bet:")
        print("1: Bet on a specific number (payout 35:1)")
        print("2: Bet on red or black (payout 1:1)")
        print("3: Bet on odd or even (payout 1:1)")
        print("4: Bet on high (19-36) or low (1-18) (payout 1:1)")
        print("5: Quit")
        choice = int(input("Enter your choice: "))

        if choice == 5:
            break

        bet_amount = int(input("Enter your bet amount: "))
        if bet_amount > balance:
            print("Insufficient balance, you're broke!!")
            continue

        if choice == 1:
            number = int(input("Enter the number you want to bet on (0-36 or 00): "))
            winnings = game.bet_number(number, bet_amount)
        elif choice == 2:
            color = input("Enter the color you want to bet on (red/black): ").lower()
            winnings = game.bet_color(color, bet_amount)
        elif choice == 3:
            bet = input("Enter your bet (odd/even): ").lower()
            winnings = game.bet_odd_even(bet, bet_amount)
        elif choice == 4:
            bet = input("Enter your bet (high/low): ").lower()
            winnings = game.bet_high_low(bet, bet_amount)
        else:
            print("Invalid choice!")
            continue

        balance += winnings
        if winnings > 0:
            print(f"You won ${winnings}!")
        else:
            print(f"You lost ${-winnings}.")

        if balance <= 0:
            print("You have run out of money!")
            break

    print(f"Game over! Your final balance is ${balance}.")

if __name__ == "__main__":
    main()
