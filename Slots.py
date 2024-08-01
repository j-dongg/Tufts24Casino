import random
import emoji
import time

balance = 10000

print("Welcome to the casino!")
time.sleep(1.25)
print("We've started you with", balance, "dollars.")
time.sleep(1.25)

emojis = [emoji.emojize(":spade_suit:"), emoji.emojize(":club_suit:"), emoji.emojize(":heart_suit:"), emoji.emojize(":diamond_suit:")]
#  emoji choices

# rest of emojis here (paste in later):



def loading(repetition):    # this function makes a little loading effect in the terminal
    for i in range (1,repetition+1):
        print("...")    
        time.sleep(0.75)

def checkmatches(emojilist): # this checks to see if our chosen emojis have matches
    var = 0
    for elements in emojis:
        count = emojilist.count(elements)
        if count == 3:
            var += 2
        elif count == 2:
            var += 1
    return var
running = True

while running:

    bet = input("How much would you like to bet? ")


    while bet.isdigit() == False or int(bet)>balance:
        if bet.isdigit() == False:
            print('Positive integers only, please.')
            bet = input("How much would you like to bet? ")
        elif int(bet)>balance:
            print("You can't bet more than you have!")
            bet = input("How much would you like to bet? ")


    loading(3)

    chosen_emojis = ""
    for i in range (0, 3):
        chosen_emojis += random.choice(emojis)
        print(chosen_emojis, end="\r")
        time.sleep(1)
    print(chosen_emojis)
    if checkmatches(chosen_emojis) == 2:
        print("Triple match!")
        print("Jackpot!")
        balance += int(bet) * 2
        print("We've DOUBLED your bet! Your winnings:", int(bet)*2)
        print("Your updated balance:", balance//1)
        var = 0
    elif checkmatches(chosen_emojis) == 1:
        print("Double match!")
        print("We'll reward you with a percentange of the", bet, 'dollars you bet.')
        balance += int(bet) * 0.80
        print("Your updated balance:", balance//1)
        var = 0
    else:
        print("No match!")
        print("You lose!")
        balance -= int(bet)
        print("Your updated balance:", balance//1)



    if balance <1:
        print("You lost all your money. Pleasure playing with you!")
        running = False
    else:
        play_again = input("Play again? ")
        if play_again.lower().startswith("n"):
            print("Pleasure playing with you!")
            time.sleep(0.75)
            print("Your final balance:", balance//1)
            running = False
            break
        elif play_again.lower().startswith('y'):
            print("Glad to hear!")
            time.sleep(0.75)
        else:
            while play_again.lower().startswith('y') == False and play_again.lower().startswith('n') == False:
                print("Sorry, but I don't understand.")
                time.sleep(0.75)
                play_again = input("Play again? ")
                if play_again.lower().startswith("n"):
                    print("Pleasure playing with you!")
                    time.sleep(0.75)
                    print("Your final balance:", balance//1)
                    running = False
                    break
                elif play_again.lower().startswith('y'):
                    print("Glad to hear!")
                    time.sleep(0.75)
                    break
