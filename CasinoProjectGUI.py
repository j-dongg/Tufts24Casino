import pygame
import time
import emoji
import random
import os


SCREEN_W = 750  # width of screen
SCREEN_H = 600 # height of screen


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)


# Input box settings
input_box = pygame.Rect(100, 100, 140, 32)
color_inactive = GRAY
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
done = False


# these are the images that we have for the slot machine; some variables are used for scaling
moneypic = pygame.image.load('moneymouthtongue.png')
moneypicfirstdimen = (moneypic.get_width() * 0.5,moneypic.get_height() * 0.5)
moneypic = pygame.transform.scale(moneypic, moneypicfirstdimen)
diamondpic = pygame.image.load('diamond.png')
moneypicdimensions = (moneypic.get_width(), moneypic.get_height())
diamondpic = pygame.transform.scale(diamondpic, moneypicdimensions)
rubypic = pygame.image.load('ruby.png')
rubypic = pygame.transform.scale(rubypic, moneypicdimensions)
cashpic = pygame.image.load('cash.png')
cashpic = pygame.transform.scale(cashpic, moneypicdimensions)
pics = [moneypic, diamondpic, rubypic, cashpic]
pics_str = ['money', 'diamond', 'ruby', 'cash']




def checkmatches(emojilist): # this checks to see if our three chosen pics have matches
    var = 0
    for elements in pics_str:
        count = emojilist.count(elements)
        if count == 3:
            var += 2
        elif count == 2:
            var += 1
    return var




def main():
    fontpath = os.path.join('pixelfont.ttf')
    balance = 10000
    bet_bool = False
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = GRAY
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    t_ext = ''
    deal_cards = False
    sm_rect = None  # defines these as none --- we need these to avoid a local variable error later on
    bj_rect = None
    pygame.init() # creates game window
    clock = pygame.time.Clock() # creates needed clock object
    bg = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.SRCALPHA, 32) # creates specific sized screen
    font = pygame.font.Font(fontpath, 25)
    font_sml = pygame.font.Font(fontpath, 15)
    state = 'starting' # sets the mode to starting so we can make a starting screen
    bg_color = (139, 0, 0)
    blink = 0
    lever = 'up'
    ChosenPics = ''
    switchscreen = 0
    bet = '0'
    add_bet = True
    cards = 'pre-deal'
    extracard_ypos = 170
        # list of chosen emojis
    #game loop
    while True: # game runs until user decides to end it
        clock.tick(30)  # set FPS
        for event in pygame.event.get(): # check for input
            match event.type:
                case pygame.QUIT: # closes program if X in top right clicked
                    pygame.quit()
                    exit() # this function call closes the program
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_RETURN:
                            if state == 'starting':
                                state = 'choosemode'
                            if state == 'slot machine' and active:
                                print(t_ext)
                                bet = t_ext
                                t_ext = ''
                                if bet.isdigit() and int(bet)<= balance:
                                    bet_bool = True
                            if state == 'blackjack' and active:
                                print(t_ext)
                                bet = t_ext
                               # t_ext = ''
                                if bet.isdigit() and int(bet)<= balance:
                                    bet_bool = True
                            if state == 'blackjack' and cards == 'dealing':
                                cards = 'dealt'
                                bet_bool = False
                        case pygame.K_BACKSPACE:
                            if state == 'slot machine' and active:
                                t_ext = t_ext[:-1]
                            if state == 'blackjack' and active:
                                t_ext = t_ext[:-1]
                        case pygame.K_ESCAPE:
                            if state == 'slot machine' or 'blackjack':
                                state = 'choosemode'
                        case _:
                            if state == 'slot machine' and active:
                                t_ext += event.unicode
                            if state == 'blackjack' and active:
                                t_ext += event.unicode

                case pygame.KEYUP:
                    match event.key:
                        case pygame.K_RETURN:
                            if state == 'slot machine' and bet_bool:
                                lever = 'down'
                            if state == 'blackjack' and bet_bool:
                                cards = 'dealing'
                                deal_cards = True
                        case pygame.K_y:
                            if state == 'slot machine' and lever == 'selected':
                                bg.fill(bg_color)
                                lever = 'up'
                                add_bet = True
                                bet_bool = False
                                t_ext = ''
                            if state == 'blackjack' and (cards == 'lose' or cards == 'win' or cards == 'bust'):
                                bg.fill(bg_color)
                                cards = 'pre-deal'
                                add_bet = True
                                bet_bool = False
                                t_ext = ''
                        case pygame.K_h:
                            if state == 'blackjack' and (cards == 'dealt' or cards == 'hit'):
                                cards = 'hit'
                                deal_cards = True
                        case pygame.K_s:
                            if state == 'blackjack' and (cards == 'dealt' or cards == 'hit'):
                                cards = 'stand'
                                dealer_choose = True
                                add_bet = True


                case pygame.MOUSEBUTTONDOWN:
                    if state == 'choosemode' and sm_rect and bj_rect:
                        mbd_x, mbd_y = event.pos
                        if sm_rect.collidepoint((mbd_x, mbd_y)):
                            state = 'slot machine'
                        if bj_rect.collidepoint((mbd_x, mbd_y)):
                            state = 'blackjack'
                    if state == 'slot machine':
                        if input_box.collidepoint(event.pos):
                             active = not active
                        else:
                            active = False
                        color = color_active if active else color_inactive
                    if state == 'blackjack':
                        if input_box.collidepoint(event.pos):
                             active = not active
                        else:
                            active = False
                        color = color_active if active else color_inactive
                    #if state == 'slot machine' and leverup_rect:
                        #mbd_x, mbd_y = event.pos
                        #if leverup_rect.collidepoint((mbd_x, mbd_y)):
                            #lever = 'down'





        match state:
            case 'starting':
                img = pygame.image.load('startingscreen.png')
                bg.blit(img, (0,0)) # puts it on the screen
                text = font.render('PRESS ENTER TO PLAY', 1, BLACK)
                blink += 1
                blink %= 30
                if blink >= 15:
                    bg.blit(text, (40, 300))
            case 'choosemode':
                img = pygame.image.load('choosemode.png')
                bg.blit(img, (0,0))
                bal_text = font_sml.render(f"Balance: ${balance}", 1, BLACK)
                bg.blit(bal_text, (10,30))
                sm_img = pygame.image.load('slotmachinepic.png')
                newh = sm_img.get_height() * 0.25
                neww = sm_img.get_width() * 0.25
                sm_img = pygame.transform.scale(sm_img, (neww, newh))
                bg.blit(sm_img, (125, 60))
                sm_rect = pygame.Rect((125, 60), (neww, newh))
                sm_text = font_sml.render('CLICK FOR SLOT MACHINE', 1, (0,0,0))
                bj_img = pygame.image.load('blackjackpic.png')
                h = bj_img.get_height() * 0.3
                w = bj_img.get_width() * 0.3
                bj_img = pygame.transform.scale(bj_img, (w, h))
                bg.blit(bj_img, (550, 260))
                bj_rect = pygame.Rect((550,260), (w, h))
                bj_text = font_sml.render('CLICK FOR BLACKJACK', 1, (0,0,0))
                blink += 1
                blink %= 30
                if blink >= 15:
                    bg.blit(sm_text, (260, 120))
                    bg.blit(bj_text, (225, 310))



# SLOT MACHINE GAME


            case 'slot machine':
                bal_text = font.render(f"Balance: ${balance}", 1, BLACK)
                bg.fill(bg_color)
                text = font.render('SLOT MACHINE', 1, (0,0,0))
                bg.blit(bal_text, (0,30))
                bg.blit(text, (0,0))
                questionmark = pygame.image.load('questionmark.png')
                questionmark_xcoord = 30
                questionmark_ycoord = 150
                het = questionmark.get_height() * 0.5
                wid = questionmark.get_width() * 0.5
                questionmark = pygame.transform.scale(questionmark, (wid, het))
                for i in range (0,3):
                    questionmarkpos = (questionmark_xcoord, questionmark_ycoord)
                    bg.blit(questionmark, questionmarkpos)
                    questionmark_xcoord += 120
                #pygame.draw.rect(bg, (0,0,0), leverup_rect) # can draw the rectangle of the button for troubleshooting issues
                if lever == 'up':

                    text = font.render('PLACE BET,', 1, (0,0,0))
                    teeext = font.render('THEN PRESS ENTER TO SPIN', 1, (0,0,0))
                    blink += 1
                    blink %= 20
                    if blink >= 10:
                        bg.blit(teeext, (100, 450))
                        bg.blit(text, (100, 400))
                  #  askforbet = font_sml.render('How much would you like to bet?', 1, (0,0,0))
                #    bg.blit(askforbet, (100,200))
                    switchscreen = 0
                    # Render the current text.
                    txt_surface = font.render(t_ext, True, BLACK)
                    # Resize the box if the text is too long.
                    width = max(200, txt_surface.get_width()+10)
                    input_box.w = width
                    # Blit the text.
                    bg.blit(txt_surface, (input_box.x+5, input_box.y+5))
                    # Blit the input_box rect.
                    pygame.draw.rect(bg, color, input_box, 2)
                    if bet.isdigit() == False:
                        command = font_sml.render('Positive integers only, please.', 1, BLACK)
                        bg.blit(command, (100,75))
                    elif int(bet)>balance:
                        command = font_sml.render("You can't bet more than you have!", 1, BLACK)
                        bg.blit(command, (100,75))


            #while bet.isdigit() == False or int(bet)>balance:
       # if bet.isdigit() == False:
        ##    print('Positive integers only, please.')
          #  bet = input("How much would you like to bet? ")
      #  elif int(bet)>balance:
       #     print("You can't bet more than you have!")
        #    bet = input("How much would you like to bet? ")

                if lever == 'down':
                    bg.blit(bal_text, (0,30))
                    bg.fill(bg_color)
                    text = font.render('SLOT MACHINE', 1, (0,0,0))
                    bg.blit(text, (0,0))

                    text = font.render('SPINNING', 1, (0,0,0))
                    bg.blit(text, (520,150))
                    ChosenPics = ''

                   # rnge = (10, random.randint(15,25))
                    #for i in range (10, random.randint(15,25)):
                    pic_x = 30
                    for i in range (0,3):
                        pic_y = 150
                        pic_coords = (pic_x, pic_y)
                        chosen_pic = random.choice(pics)
                        bg.blit(chosen_pic, pic_coords)
                        pic_x += 120
                        time.sleep(0.08)
                        switchscreen += 1
                        print(switchscreen)
                    if switchscreen >= random.randint(50,80):
                        lever = 'stop'
                if lever == 'stop':
                    bg.fill(bg_color)
                    bg.blit(bal_text, (0,30))
                    text = font.render('stop screen', 1, (0,0,0))
                    bg.blit(text, (0,0))
                    questionmark_xcoord = 30
                    chosenpic1 = random.choice(pics)
                    if chosenpic1 == moneypic:
                        ChosenPics += 'money'
                    elif chosenpic1 == rubypic:
                        ChosenPics += 'ruby'
                    elif chosenpic1 == diamondpic:
                        ChosenPics += 'diamond'
                    elif chosenpic1 == cashpic:
                        ChosenPics += 'cash'
                    #questionmarkpos = (questionmark_xcoord, questionmark_ycoord)
                    #bg.blit(chosenpic1, questionmarkpos)
                    #questionmark_xcoord += 120
                    chosenpic2 = random.choice(pics)
                    if chosenpic2 == moneypic:
                        ChosenPics += 'money'
                    elif chosenpic2 == rubypic:
                        ChosenPics += 'ruby'
                    elif chosenpic2 == diamondpic:
                        ChosenPics += 'diamond'
                    elif chosenpic2 == cashpic:
                        ChosenPics += 'cash'
                    #questionmarkpos = (questionmark_xcoord, questionmark_ycoord)
                    #bg.blit(chosenpic2, questionmarkpos)
                    #questionmark_xcoord += 120
                    chosenpic3 = random.choice(pics)
                    if chosenpic3 == moneypic:
                        ChosenPics += 'money'
                    elif chosenpic3 == rubypic:
                        ChosenPics += 'ruby'
                    elif chosenpic3 == diamondpic:
                        ChosenPics += 'diamond'
                    elif chosenpic3 == cashpic:
                        ChosenPics += 'cash'
                    print(ChosenPics)
                    #questionmarkpos = (questionmark_xcoord, questionmark_ycoord)
                    #bg.blit(chosenpic3, questionmarkpos)
                    lever = 'selected'
                if lever == 'selected':
                    bg.fill(bg_color)
                    bg.blit(bal_text, (0,30))
                    text = font.render('SLOT MACHINE', 1, (0,0,0))
                    bg.blit(text, (0,0))
                    bg.blit(chosenpic1, (30, 150))
                    bg.blit(chosenpic2, (150, 150))
                    bg.blit(chosenpic3, (270, 150))
                    if checkmatches(ChosenPics) == 2:
                        text2 = font_sml.render('Triple Match!', 1, (0,0,0))
                        bg.blit(text2, (400,150))
                        if add_bet:
                            balance += int(bet) * 2
                        youwin = font_sml.render("JACKPOT!! We've DOUBLED your bet!", 1, (0,0,0))
                        winwithbal = font_sml.render(f"You won: ${int(bet)*2}",1, (0,0,0))
                        bg.blit(youwin, (400, 200))
                        bg.blit(winwithbal, (400, 250))
                        updatedbal = font_sml.render(f"Your balance: ${balance}", 1, (0,0,0))
                        bg.blit(updatedbal, (400,300))
                        add_bet = False
                    elif checkmatches(ChosenPics) == 1:
                        if add_bet:
                            balance += int(bet)*0.8
                        text2 = font_sml.render('Double Match!', 1, (0,0,0))
                        bg.blit(text2, (400,150))
                        youwin = font_sml.render("We'll give you some winnings.", 1, (0,0,0))
                        winwithbal = font_sml.render(f"You won:{(int(bet)*0.8)//1} dollars",1, (0,0,0))
                        bg.blit(youwin, (400, 200))
                        bg.blit(winwithbal, (400, 250))
                        updatedbal = font_sml.render(f"Your balance: ${balance}", 1, (0,0,0))
                        bg.blit(updatedbal, (400,300))
                        add_bet = False
                    else:
                        text2 = font_sml.render('No matches!', 1, (0,0,0))
                        text3 = font_sml.render('You lose!', 1, (0,0,0))
                        if add_bet:
                            balance -= int(bet)
                        bg.blit(text3, (400, 200))
                        bg.blit(text2, (400,150))
                        updatedbal = font_sml.render(f"Your balance: ${balance}", 1, (0,0,0))
                        bg.blit(updatedbal, (400,300))
                        add_bet = False






# BLACKJACK GAME
            case 'blackjack':
                extracard_ypos = 170

                match cards:
                    case 'pre-deal':
                        bg.fill(bg_color)
                        text = font.render('BLACKJACK', 1, (0,0,0))
                        bg.blit(text, (0,0))
                        bal_text = font.render(f"Balance: ${balance}", 1, BLACK)
                        bg.blit(bal_text, (0,30))
                        asktodeal = font_sml.render('PLACE BET, THEN PRESS ENTER TO DEAL', 1, (0,0,0))
                        blink += 1
                        blink %= 30
                        if blink >= 15:
                            bg.blit(asktodeal, (100,400))
                    # Render the current text.
                        txt_surface = font.render(t_ext, True, BLACK)
                    # Resize the box if the text is too long.
                        width = max(200, txt_surface.get_width()+10)
                        input_box.w = width
                    # Blit the text.
                        bg.blit(txt_surface, (input_box.x+5, input_box.y+5))
                    # Blit the input_box rect.
                        pygame.draw.rect(bg, color, input_box, 2)
                        if bet.isdigit() == False:
                            command = font_sml.render('Positive integers only, please.', 1, BLACK)
                            bg.blit(command, (100,75))
                        elif int(bet)>balance:
                            command = font_sml.render("You can't bet more than you have!", 1, BLACK)
                            bg.blit(command, (100,75))
                    case 'dealing':
                        bg.fill(bg_color)
                        text = font.render('dealing cards', 1, (0,0,0))
                        bg.blit(text, (0,0))
                        cardtext1 = font.render('FIRST CARD: ??', 1, (0,0,0))
                        bg.blit(cardtext1, (10,50))
                        cardtext2 = font.render('SECOND CARD: ??', 1, (0,0,0))
                        bg.blit(cardtext2, (10,80))
                        dealertext = font.render('DEALER CARD: ??', 1, (0,0,0))
                        bg.blit(dealertext, (10, 140))
                        command = font.render('PRESS ENTER TO REVEAL', 1, (0,0,0))
                        blink+=1
                        blink%=30
                        if blink<=15:
                            bg.blit(command, (100,300))
                    case 'dealt':
                        bg.fill(bg_color)
                        text = font.render('BLACKJACK', 1, (0,0,0))
                        bg.blit(text, (0,0))
                        if deal_cards:
                            card1 = random.randint(1,11)
                            card2 = random.randint(1,11)
                            dealercard1 = random.randint(1,11)
                            deal_cards = False
                        cardtextone = font.render(f'FIRST CARD: {card1}', 1, (0,0,0))
                        bg.blit(cardtextone, (10,50))
                        cardtexttwo = font.render(f'SECOND CARD: {card2}', 1, (0,0,0))
                        bg.blit(cardtexttwo, (10,80))
                        dealer_text = font.render(f'DEALER CARD: {dealercard1}', 1, (0,0,0))
                        bg.blit(dealer_text, (10,140))
                        total = card1+card2
                        dealertotal = dealercard1
                        totaltxt = font.render(f'TOTAL: {total}', 1, (0,0,0))
                        bg.blit(totaltxt, (10,110))
                        hit_cmd = font.render('PRESS H TO HIT', 1, (0,0,0))
                        stand_cmd = font.render('PRESS S TO STAND', 1, (0,0,0))
                        blink += 1
                        blink %= 30
                        if blink <= 15:
                            bg.blit(hit_cmd,(100,300))
                            bg.blit(stand_cmd, (100,350))
                    case 'hit':
                        bg.fill(bg_color)
                        text = font.render('BLACKJACK', 1, (0,0,0))
                        bg.blit(text, (0,0))
                        cardtextone = font.render(f'FIRST CARD: {card1}', 1, (0,0,0))
                        bg.blit(cardtextone, (10,50))
                        cardtexttwo = font.render(f'SECOND CARD: {card2}', 1, (0,0,0))
                        bg.blit(cardtexttwo, (10,80))
                        dealer_text = font.render(f'DEALER CARD: {dealercard1}', 1, (0,0,0))
                        bg.blit(dealer_text, (10,140))
                        if deal_cards:
                            extra_card = random.randint(1,11)
                            total += extra_card
                            deal_cards = False
                        extracardtext = font.render(f'EXTRA CARD: {extra_card}', 1, (0,0,0))
                        bg.blit(extracardtext, (50, extracard_ypos))
                        total_text = font.render(f'TOTAL: {total}', 1, (0,0,0))
                        bg.blit(total_text, (10,110))
                        if total>21:
                            cards = 'bust'
                        else:
                            hit_cmd = font.render('PRESS H TO HIT', 1, (0,0,0))
                            stand_cmd = font.render('PRESS S TO STAND', 1, (0,0,0))
                            blink += 1
                            blink %= 30
                            if blink <= 15:
                                bg.blit(hit_cmd,(100,300))
                                bg.blit(stand_cmd, (100,350))

                    case 'stand':
                        bg.fill(bg_color)
                        text = font.render('BLACKJACK', 1, (0,0,0))
                        bg.blit(text, (0,0))
                        cardtextone = font.render(f'FIRST CARD: {card1}', 1, (0,0,0))
                        bg.blit(cardtextone, (10,50))
                        cardtexttwo = font.render(f'SECOND CARD: {card2}', 1, (0,0,0))
                        bg.blit(cardtexttwo, (10,80))
                        dealer_text = font.render(f'DEALER CARD: {dealercard1}', 1, (0,0,0))
                        bg.blit(dealer_text, (10,140))
                        total_text = font.render(f'TOTAL: {total}', 1, (0,0,0))
                        bg.blit(total_text, (10,110))
                        if dealertotal<=total:
                            dealerchoicetxt = font.render('dealer hits', 1, (0,0,0))
                            bg.blit(dealerchoicetxt, (random.randint(150,250), random.randint(350,450)))
                            dealerextracard = random.randint(1,11)
                            dealertotal += dealerextracard
                            print(dealertotal)
                            dealertotaltxt = font.render(f'DEALER TOTAL: {dealertotal}', 1, (0,0,0))
                            bg.blit(dealertotaltxt, (30,170))
                            dealer_extra_text = font.render(f'DEALER DRAWS: {dealerextracard}', 1, (0,0,0))
                            bg.blit(dealer_extra_text, (50,200))
                            time.sleep(2)
                        elif dealertotal>21:
                            time.sleep(2)
                            cards = 'win'
                        elif dealertotal>total:
                            dealerchoicetxt = font.render('dealer stands', 1, (0,0,0))
                            bg.blit(dealerchoicetxt, (200,400))
                            dealertotaltxt = font.render(f'DEALER TOTAL: {dealertotal}', 1, (0,0,0))
                            bg.blit(dealertotaltxt, (30,170))
                            cards = 'lose'
                            time.sleep(2)


                    case 'lose':
                        bg.fill(bg_color)
                        total_text = font.render(f'TOTAL: {total}', 1, (0,0,0))
                        bg.blit(total_text, (10,110))
                        dealertotaltxt = font.render(f'DEALER TOTAL: {dealertotal}', 1, (0,0,0))
                        bg.blit(dealertotaltxt, (10,80))
                        text = font.render('BLACKJACK', 1, (0,0,0))
                        bg.blit(text, (0,0))
                        statement = font.render('YOU LOST.', 1, (0,0,0))
                        bg.blit(statement, (10,150))
                        if add_bet:
                            balance -= int(bet)
                        updatedbal = font_sml.render(f"Your balance: ${balance}", 1, (0,0,0))
                        bg.blit(updatedbal, (400,300))
                        add_bet = False
                        play_again = font.render('PRESS Y TO PLAY AGAIN', 1, (0,0,0))
                        bg.blit(play_again, (150, 400))
                    case 'win':
                        bg.fill(bg_color)
                        total_text = font.render(f'TOTAL: {total}', 1, (0,0,0))
                        bg.blit(total_text, (10,110))
                        dealertotaltxt = font.render(f'DEALER TOTAL: {dealertotal}', 1, (0,0,0))
                        bg.blit(dealertotaltxt, (10,80))
                        text = font.render('BLACKJACK', 1, (0,0,0))
                        bg.blit(text, (0,0))
                        statement = font.render('YOU WON.', 1, (0,0,0))
                        bg.blit(statement, (10,150))
                        if add_bet:
                            balance += int(bet)
                        updatedbal = font_sml.render(f"Your balance: ${balance}", 1, (0,0,0))
                        bg.blit(updatedbal, (400,300))
                        add_bet = False
                        play_again = font.render('PRESS Y TO PLAY AGAIN', 1, (0,0,0))
                        bg.blit(play_again, (150, 400))
                    case 'bust':
                        bg.fill(bg_color)
                        total_text = font.render(f'TOTAL: {total}', 1, (0,0,0))
                        bg.blit(total_text, (10,110))
                        text = font.render('BLACKJACK', 1, (0,0,0))
                        bg.blit(text, (0,0))
                        statement = font.render('YOU BUSTED.', 1, (0,0,0))
                        bg.blit(statement, (10,150))
                        if add_bet:
                            balance -= int(bet)
                        updatedbal = font_sml.render(f"Your balance: ${balance}", 1, (0,0,0))
                        bg.blit(updatedbal, (400,300))
                        add_bet = False
                        play_again = font.render('PRESS Y TO PLAY AGAIN', 1, (0,0,0))
                        bg.blit(play_again, (150, 400))




        # ======================
        # game stuff goes here!
        # ======================

        pygame.display.update()  # update screen


if __name__ == '__main__':
    main()
