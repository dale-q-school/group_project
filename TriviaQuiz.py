import os
from threading import Thread
import random
from time import sleep
from playsound import playsound
from gtts import gTTS
from pygame import mixer

def triviaGame():


    # constants
    # blocks, lines, boxes
    # double lines
    # corners
    CORNER_TOP_LEFT_DOUBLELINE = '\u2554'
    CORNER_TOP_RIGHT_DOUBLELINE = '\u2557'
    CORNER_BOTTOM_RIGHT_DOUBLELINE = '\u255d'
    CORNER_BOTTOM_LEFT_DOUBLELINE = '\u255a'
    # straight segments
    LINE_HORIZONTAL_DOUBLELINE = '\u2550'
    LINE_VERTICAL_DOUBLELINE = '\u2551'
    # Ts
    TEE_TOP_DOUBLELINE = '\u2566'
    TEE_BOTTOM_DOUBLELINE = '\u2569'
    TEE_RIGHT_DOUBLELINE = '\u2563'
    TEE_LEFT_DOUBLELINE = '\u2560'

    # single lines
    # corners
    CORNER_TOP_LEFT_SINGLELINE = '\u250C'
    CORNER_TOP_RIGHT_SINGLELINE = '\u2510'
    CORNER_BOTTOM_LEFT_SINGLELINE = '\u2514'
    CORNER_BOTTOM_RIGHT_SINGLELINE = '\u2518'
    # straight lines
    LINE_VERTICAL_SINGLELINE = '\u2502'
    LINE_HORIZONTAL_SINGLELINE = '\u2500'
    # ts
    TEE_TOP_SINGLELINE = '\u252C'
    TEE_BOTTOM_SINGLELINE = '\u253B'
    TEE_RIGHT_SINGLELINE = '\u2524'
    TEE_LEFT_SINGLELINE = '\u251C'
    # cross
    PLUS_SINGLELINE = '\u253C'

    # triangle
    TRIANGLE_BOTTOM_BLACK = '\u25BC'
    TRIANGLE_BOTTOM_WHITE = '\u25BD'
    TRIANGLE_TOP_BLACK = '\u25B2'
    TRIANGLE_TOP_WHITE = '\u25B3'
    TRIANGLE_LEFT_WHITE = '\u25C1'
    TRIANGLE_RIGHT_WHITE = '\u25B7'

    DIAMOND_BLACK = '\u25c6'
    TRIANGLE1 = '\u25ba'
    CIRCLE1 = '\u25cf'
    BLACKBOX = '\u2587'
    GREYBOX_1 = '\u2591'
    GREYBOX2 = '\u2592'
    GREYBOX3 = '\u2593'
    BOX1 = '\u2580'
    WIDTH = 80

    # stars
    STAR1 = '\u272B'
    STAR_BLACK = '\u2605'
    STAR_WHITE = '\u2606'
    STAR_CIRCLE = '\u272A'
    STAR_FRAME = '\u269D'

    # arrows
    ARROW_RIGHT = '\u2192'
    ARROW_UP = '\u2191'
    ARROW_RIGHT = '\u2190'
    ARROW_DOWN = '\u2193'

    # letters
    CIRCLE_A = '\u24B6'
    CIRCLE_B = '\u24B7'
    CIRCLE_C = '\u24B8'
    CIRCLE_D = '\u24B9'
    CIRCLE_E = '\u24BA'
    CIRCLE_F = '\u24BB'
    CIRCLE_M = '\u24C2'
    LETTER_Q = '\u0051'
    CIRCLE_S = '\u24C8'
    CIRCLE_X = '\u24CD'

    # numbers
    CIRCLE_1 = '\u2460'
    CIRCLE_2 = '\u2461'
    CIRCLE_3 = '\u2462'
    CIRCLE_4 = '\u2463'
    CIRCLE_5 = '\u2464'
    ONE_POINT = '\u2488'
    TWO_POINT = '\u2489'
    THREE_POINT = '\u248A'
    FOUR_POINT = '\u248B'
    FIVE_POINT = '\u248C'

    # hearts
    HEART_WHITE = '\u2661'
    HEART_BLACK = '\u2764'

    # punctuation
    MARK_LEFT = '\u276E'
    MARK_RIGHT = '\u276F'
    QUESTION_MARK = '\u003F'

    # miscellaneous
    CLOCK = '\u231B'
    WATCH = '\u231A'
    SETUP = '\u2692'
    CHECK = '\u2714'
    CROSS = '\u2718'
    CROSS_RED = '\u274C'

    WRONG_CHOICE = "Sorry, that's not an option. Please try again!"
    PLAYERNAME = "John Doe"

    # temporary data
    # TODO: store in data file
    sets = ["NUMBERS", "FRUITS", "VEGETABLES", "ANIMALS", "NATURE", "GREETINGS","ADJECTIVES","VERBS","PRONOUNS","ADVERBS"]

    categories = [
                [0,"Numbers", "Japanese Numbers","What is","in Japanese numbers?"],
                [1,"Fruits","Fruits are awesome", "Do you know what fruit is","?"],
                [2,"Vegetables","Do you like healthy foods?","Do you what know what","is?"],
                [3,"Animals","Animal Lover","Do you know who is","?"],
                [4,"Nature","Planet Earth", "What do you think", "is in English?"],
                [5,"Greetings","Greeting Someone","How would you say","in English?"],
                [6,"Adjectives","Describe Something","What does","mean in English?"],
                [7,"Verbs","No Verbs, No Actions!","The Japanese verb","English equivalent is?"],
                [8,"Pronouns","Who?","Who would be","?"],
                [9,"Adverbs","The what, when, why, and who","Can you guess the adverb","?"],]

    deck = {
        0: [
            [0,"one","ichi","Everything starts with One"],
            [1,"two","ni","Two is better than One"],
            [2,"three","san","There were three musketeers"],[3,"four","shi","There are four wheels in a car"],
            [4,"five","go","Five fingers in a hand"],[5,"six","roku","Six Six Six is the number of the devil"],[6,"seven","shichi","Seven Samurai"],
            [7,"eight","hachi","Eight looks like infinity"],
            [8,"nine","kyuu","Nine "],[9,"ten","juu","We have ten fingers"]
        ],
        1: [[0,"ringo","apple","Fuji is a kind of Japanese apple."],[1,"ichigo","strawberry","Ichigo is the Japanese word for strawberry"],
            [2,"mikan","mandarin","Mandarin oranges are native to the Philippines and southeastern Asia"],
            [3,"momo","peach","Momotaro is a popular hero of Japanese folklore"],[4,"suika","watermelon","In Japan there are squared watermelons"],
            [5,"budou","grape","Japanese grapes are some of the most expensive grapes in the world"],[6,"nashi","pear","Japanese pears have round apple-like shape."],
            [7,"sakuranbo","cherry","Cherry blossoms are called Sakura."],[8,"anzu","apricot","Apricot jam is superb"],[9,"kaki","persimmon","I love kaki"]],
        2:[[0,"kyuuri","cucumber","Japanese cucumbers are smaller"],
           [1,"toumorokoshi","corn","Japanese corns are sweet"],
           [2,"nasu","eggplant","Japanese eggplants are small"],[3,"ninniku","garlic","China produces 76% of the world's supply of garlic."],
           [4,"kyabetsu","cabbage","Cabbages has lots of vitamine C"],[5,"ninjin","carot","Bunnies love carots"],
           [6,"jagaimo","potato","Idaho is coined as the Potato State."],[7,"tamanegi","onion","The most popular onions in Japan is yellow"],
           [8,"hourensou","spinach","Spinach is native to Persia"],[9,"satsumaimo","sweet potato","Sweet potatoes are high in beta carotene"]],
        3:[[0,"inu","dog","I love dogs"],[1,"neko","cat","Cats are independent"],[2,"zou","elephant","Elephants are smart"],
           [3,"uma","horse","Horses are beautiful"],[4,"buta","pig","Pigs are cute"],[5,"kuma","bear","Bears are big"],
           [6,"tora","tiger","Tigers has stripes"],[7,"tori","bird","Birds fly in the sky"],
           [8,"iruka","dolphin","Dolphins have healing power"],[9,"saru","monkey","Japanese monkeys like to taking baths"]],
        4:[[0,"ki","tree","big tree is \"Ookii ki\""],
           [1,"hana","flower","beautiful flower is \"kireina hana\""],
           [2,"tsuki","moon","Michael Jackson's moonwalk "],
           [3,"taiyou","sun","The sun is the closest star to our planet"],
           [4,"umi","ocean","Japan is surrounded by the oceans"],
           [5,"yama","mountain","The highest mountain in Japan is Mt. Fuji"],
           [6,"kawa","river","The longest river in the world is Nile river"],
           [7,"hoshi","star","The sun is a star"],
           [8,"kumo","cloud","Clouds are heavy"],
           [9,"niji","rainbow","You can never get to the end of a rainbow"]
           ],
        5:[[0,"Ohayou","Good morning.","In the morning, we say \"Ohayou\""],
           [1,"Konnichiwa","Good afternoon.","Konnichiwa also means \"hello\""],
           [2,"Konbanwa","Good evening.","In the evening, we say \"Konbanwa\""],
           [3,"Oyasumi","Good night.","Before go to bed, we say \"Oyasumi\""],
           [4,"Arigatou","Thank you.","Thank you everyone"],
           [5,"Sumimasen","I am sorry.","\"Sumimasen\" also means \"Excuse me\"."],
           [6,"Omedetou","Congratulations.","Omedetou! You made it!"],
           [7,"Hajimemashite","Nice to meet you.","\"Hajime\" means first"],
           [8,"Sayounara","Good bye.","Could be Sayonara"],
           [9,"Youkoso","Welcome.","Welcome to the world!"]
           ],
        6:[[0,"kawaii","cute","Dogs are cute"],[1,"tanoshii","fun","This game is fun"],[2,"kanashii","sad","It is a sad story"],
           [3,"hayai","fast","This computer is fast"],[4,"osoi","slow","I am slow"],[5,"takai","high","High buildings"],[6,"hikui","low","Low trees"],
           [7,"nagai","long","Long river"],[8,"mijikai","short","Short hair"],[9,"atarashii","new","New book"]
           ],
        7:[[0,"taberu","eat","I eat bread"],[1,"nomu","drink","I drink coffee"],[2,"hashiru","run","He runs"],[3,"kaku","write","She writes a letter"],
           [4,"hanasu","talk","I talk slow"],[5,"yomu","read","I read a book"],[6,"kiku","hear","I hear you"],[7,"miru","see","I see you"],
           [8,"aruku","walk","I walk in the park"],[9,"aisuru","love","I love you"]],
        8:[[0,"watashi","I","I eat bread"],[1,"anata","You","You drink milk"],[2,"kare","He","He runs"],[3,"kanojo","She","She writes a letter"],
           [4,"watashitachi","We","We are friends"],[5,"watashino","my","My book"],[6,"anatano","your","Your voice"],[7,"kareno","his","His girlfriend"],
           [8,"kanojono","her","Her boyfriend"],[9,"watashitachino","our","Our friends"]],
        9:[[0,"Nani","what","What is this?"],[1,"Doko","where","Where are you?"],[2,"Itsu","when","When is it?"],[3,"Dare","who","Who are you?"],
           [4,"Dore","which","Which one?"],[5,"Kore","this ","This is a pen"],[6,"Sore","it","It is a book"],[7,"Are","that ","That is a star"],
           [8,"Ikura","How much","How much?"],[9,"Naze","why","Why?"]]}


    # This function displays the title of the game
    def titleHeadMaker(str_title, level):
        title = str_title
        # level 1 use doublelines, level 2 use singlelines

        if level == 1:
            COR_TL = CORNER_TOP_LEFT_DOUBLELINE
            COR_TR = CORNER_TOP_RIGHT_DOUBLELINE
            COR_BL = CORNER_BOTTOM_LEFT_DOUBLELINE
            COR_BR = CORNER_BOTTOM_RIGHT_DOUBLELINE
            LIN_V = LINE_VERTICAL_DOUBLELINE
            LIN_H = LINE_HORIZONTAL_DOUBLELINE
            TEE_T = TEE_TOP_DOUBLELINE
            TEE_B = TEE_BOTTOM_DOUBLELINE
            TEE_L = TEE_LEFT_DOUBLELINE
            TEE_R = TEE_RIGHT_DOUBLELINE
        if level == 2:
            COR_TL = CORNER_TOP_LEFT_SINGLELINE
            COR_TR = CORNER_TOP_RIGHT_SINGLELINE
            COR_BL = CORNER_BOTTOM_LEFT_SINGLELINE
            COR_BR = CORNER_BOTTOM_RIGHT_SINGLELINE
            LIN_V = LINE_VERTICAL_SINGLELINE
            LIN_H = LINE_HORIZONTAL_SINGLELINE
            TEE_T = TEE_TOP_SINGLELINE
            TEE_B = TEE_BOTTOM_SINGLELINE
            TEE_L = TEE_LEFT_SINGLELINE
            TEE_R = TEE_RIGHT_SINGLELINE

        print(COR_TL, end="")
        for x in range(WIDTH - 2):
            print(LIN_H, end="")
        print(COR_TR)
        print(LIN_V, end="")
        for x in range(int((WIDTH - 2 - len(title)) / 2)):
            print(" ", end="")
        print(title, end="")
        for x in range(int((WIDTH - 1 - len(title)) / 2)):
            print(" ", end="")
        print(LIN_V)
        print(COR_BL, end="")
        for x in range(WIDTH - 2):
            print(LIN_H, end="")
        print(COR_BR)


    def chooseTriviaSet(sets):
        str_title = "CATEGORIES"
        level = 2
        titleHeadMaker(str_title, level)

        if AUDIOON == 1:
            phrase = "Categories"
            thread_3 = Thread(target=Text2speech, args=(phrase, 2))
            thread_3.start()

        # to know the number of game sets
        numberOfSets = len(sets)

        i = 0
        flag = 1
        gameset = 0

        # display game menu
        for x in sets:
            print(str(i + 1) + " " + x)
            i += 1

        print(DIAMOND_BLACK+ " Choose a game set: ", end=" ")

        for i in range(0, numberOfSets):
            print((i + 1), end=" ")
        print(DIAMOND_BLACK + " or M to return to Game Menu "+TRIANGLE_RIGHT_WHITE, end=" ")

        gameset = input()

        if gameset == "M" or gameset == "m":
            optionsMenu()

        gameset = int(gameset) - 1

        sleep(1)
        return categories[gameset]


    def triviaGame(set, deck):
        #setup variables
        numWins = 0
        numLosses = 0
        score = 0

        # deckNo chosen
        deckNo = set[0]

        cards = deck[deckNo]

        # number of cards in the deck?
        deckLen = len(cards)

        level = 2
        str_title = set[2]
        playAgain = 1

        while playAgain == 1:
            # title of question category
            titleHeadMaker(str_title, level)

            if AUDIOON == 1:
                phrase = str_title
                thread_03 = Thread(target=Text2speech, args=(phrase, 3))
                thread_03.start()

            # generate random number
            randQuestion = random.randint(0, deckLen - 1)

            # copyoriginalDeck into a "working" deck
            categoryDeck = cards.copy()

            # shuffle cards in deck everytime because the player may play consecutive games
            # with little time difference and our random generator is time based so in that
            # case the random number may repeat
            random.shuffle(categoryDeck)

            # save question-answer entry in a separate array
            categoryQA = categoryDeck[randQuestion]

            # lets get the question and answer
            question = categoryQA[1]
            answer = categoryQA[2]

            # print the question
            print(set[3] + " " + question + " " + set[4])
            question_word = set[3] + " " + question + " " + set[4]

            # now that we have a separate array for Q&A, drop the question card
            categoryDeck.pop(randQuestion)

            # generate a random number between 0 and 4, where the right answer will be placed,
            # now lets add question to specific randomly generated
            answerPos = random.randint(0, 4)

            # shuffle our deck again
            random.shuffle(categoryDeck)

            # temp:
            optionsToDisplay = 5

            # options to display
            options = optionsToDisplay - 1
            # array is shuffled, just drop unneeded (by slicing)
            categoryDeck = categoryDeck[0:options]

            categoryDeck.insert(answerPos, categoryQA)
            i = 0

            while i < 5:
                print(str(i + 1) + "." + str(categoryDeck[i][2]))
                i += 1

            if AUDIOON == 1:
                phrase = question_word
                thread_4 = Thread(target=Text2speech, args=(phrase, 6))
                sleep(2)
                thread_4.start()

            choiceBad = 0
            # now lets get the answer
            while choiceBad == 0:
                choice = int(input(DIAMOND_BLACK + " Choose 1, 2, 3, 4, or 5 " + TRIANGLE_RIGHT_WHITE + " "))
                if choice > 5 or choice < 1:
                    print(ARROW_RIGHT + " " + WRONG_CHOICE + " " + CIRCLE1)
                    choiceBad = 0

                else:
                    choiceBad = 1

            yourAnswer = categoryDeck[int(choice - 1)][2]
            print(STAR_WHITE + " Your answer is: " + yourAnswer + STAR_WHITE)

            # compare to right answer
            if yourAnswer == answer:
                numWins +=1
                if AUDIOON == 1:
                    snd = 2
                    thread_5 = Thread(target=sounds, args=(snd,))
                    thread_5.start()

                    phrase = PLAYERNAME+"You are right!"
                    thread_6 = Thread(target=Text2speech, args=(phrase, 4))
                    thread_6.start()
                for n in range(0, WIDTH - 2):
                    print(GREYBOX3, end="")
                print("\n" + CHECK + " That's correct! " + STAR_FRAME + " Congratulations "+PLAYERNAME+ "!! " + STAR_FRAME)
                for n in range(0, WIDTH - 2):
                    print(GREYBOX3, end="")
                score += 1
                print("\n" + HEART_WHITE + " Fact " + HEART_WHITE)

                print(categoryDeck[answerPos][3])

            if yourAnswer != answer:
                numLosses += 1
                for n in range(0, WIDTH - 2):
                    print(GREYBOX3, end="")
                print("\n" + CROSS_RED + " I am sorry, "+PLAYERNAME+" that is not the correct answer " + CROSS_RED)
                for n in range(0, WIDTH - 2):
                    print(GREYBOX3, end="")

                if AUDIOON == 1:
                    snd = 3
                    thread_05 = Thread(target=sounds, args=(snd,))
                    thread_05.start()
                    phrase = PLAYERNAME+"That's wrong!"

                    thread_06 = Thread(target=Text2speech, args=(phrase, 5))
                    thread_06.start()
            print("\n" + STAR1 + " Your overall score is " + str(score) + STAR1)

            statSaveFile(score,numWins, numLosses)

            wrongChoice = 1

            while wrongChoice == 1:
                choice = input(
                    DIAMOND_BLACK + " Play again? (Y/N), Other Category (C), Game Menu (M) " + TRIANGLE_RIGHT_WHITE + " ")
                if choice == 'Y' or choice == 'y':
                    playAgain = 1
                    wrongChoice = 0
                elif choice == 'N' or choice == 'n':
                    playAgain = 0
                    wrongChoice = 0
                    optionsMenu()
                elif choice == 'C' or choice == 'c':
                    playAgain = 0
                    wrongChoice = 0
                    game(sets, deck)
                elif choice == 'M' or choice == 'm':
                    playAgain = 0
                    wrongChoice = 0
                    optionsMenu()
                else:
                    wrongChoice = 1

        # do something


    def statSaveFile(score, wins, losses):

        # read file
        with open('setupinfo.dat', 'r') as file:
            data = file.read().splitlines()
        file.close()

        data[0]= AUDIOON
        data[1]= MUSICON
        data[2]= MUSICVOL
        data[3]= PLAYERNAME
        data[4]= score
        data[5]= wins
        data[6]= losses

        with open("setupinfo.dat", "w") as file:
            file.writelines([str(data[0])+"\n",str(data[1])+"\n",str(data[2])+"\n",str(data[3])+"\n",str(data[4])+"\n",str(data[5])+"\n",str(data[6])+"\n"])
            file.close()


    def game(sets, deck):
        set = chooseTriviaSet(sets)
        triviaGame(set, deck)


    def audioONOFF(soundmusic):
        global MUSICON
        global AUDIOON
        global MUSICVOL

        level = 2
        with open('setupinfo.dat', 'r') as file:
            data = file.read().splitlines()
        file.close()

        if soundmusic == 1:
            str_title = "TURN SOUND ON - OFF"
        else:
            str_title = "TURN MUSIC ON - OFF AND CHANGE VOLUME"

        titleHeadMaker(str_title, level)

        if soundmusic == 1:
            flag = 0
            if AUDIOON == 0:
                while flag == 0:
                    choice = input(DIAMOND_BLACK+" Press 1 to turn audio ON, C to return to Configuration Menu "+TRIANGLE_RIGHT_WHITE+" ")[0]

                    if choice[0] == "1":  # turn ON audio
                        AUDIOON = 1  # change to ON
                        print("Audio has been turned ON. Turn it OFF in the Configuration Menu.")
                        flag = 1
                        sleep(1)

                    elif choice[0] == "c" or choice[0] == "C":
                        flag = 1
                        setup()
                    else:
                        print("Sorry, That's not a correct option. Please try again.")
                        flag = 0

            elif AUDIOON == 1:
                while flag == 0:
                    choice = input(DIAMOND_BLACK+" Press 0 to turn audio OFF, C to return to Configuration Menu "+TRIANGLE_RIGHT_WHITE+" ")[0]

                    if choice[0] == "0":  # turn OFF audio
                        AUDIOON = 0  # change to OFF
                        print("Audio has been turned OFF. Turn it ON in the Configuration Menu.")
                        flag = 1
                        sleep(1)

                    elif choice[0] == "c" or choice[0]== "C":
                        flag = 1
                        setup()
                    else:
                        print("Sorry, That's not a correct option. Please try again.")
                        flag = 0

            data[0] = AUDIOON
            with open("setupinfo.dat", "w") as file:
                file.writelines([str(data[0]) + "\n", str(data[1]) + "\n", str(data[2]) + "\n", str(data[3]) + "\n",
                                     str(data[4]) + "\n", str(data[5]) + "\n", str(data[6]) + "\n"])
                file.close()
            setup()


        elif soundmusic == 2:  # for MUSIC
            print(CIRCLE_1+" TURN MUSIC ON/OFF")
            print(CIRCLE_2+" CHANGE MUSIC VOLUME")

            flag = 0
            while flag == 0:
                choice = input(DIAMOND_BLACK+ " Choose 1 or 2, or C to Configuration Menu "+TRIANGLE_RIGHT_WHITE+" ")[0]
                if choice[0] == "1":
                    if MUSICON == 0:
                        flag1 = 0
                        while flag1 == 0:
                            choice1 = input(DIAMOND_BLACK+" Press 1 to turn music ON, or C to Configuration Menu "+TRIANGLE_RIGHT_WHITE+" ")[0]
                            if choice1[0] == "1":  # turn ON music
                                snd=4
                                sounds(snd)
                                musicon = 1
                                print("Music has started playing. To stop music, turn it on in the Configuration Menu")
                                flag1 = 1
                                sleep(1)

                            elif choice1[0] == "C" or choice1[0] == "c":
                                flag1 = 1
                                setup()
                            else:
                                print("Sorry, That's not a correct option. Please try again.")
                                flag1 = 0

                    elif MUSICON == 1 :
                        flag1 = 0
                        while flag1 == 0:
                            choice2 = input(DIAMOND_BLACK+" Press 0 to turn music OFF, or C to Configuration Menu "+TRIANGLE_RIGHT_WHITE+" ")[0]
                            if choice2[0] == "0":  # turn ON music
                                musicon = 0
                                mixer.music.stop()
                                print("Music has stopped playing. To play music, turn it ON in the Configuration Menu")
                                flag1 = 1
                                sleep(1)
                            elif choice2[0] == "C" or choice1[0] == "c":
                                flag1 = 1
                                setup()
                            else:
                                print("Sorry, That's not a correct option. Please try again.")
                                flag1 = 0

                    flag = 1
                    MUSICON = musicon
                    data[1] = musicon
                    with open("setupinfo.dat", "w") as file:
                        file.writelines([str(data[0]) + "\n", str(data[1]) + "\n", str(data[2]) + "\n", str(data[3]) + "\n",
                                         str(data[4]) + "\n", str(data[5]) + "\n", str(data[6]) + "\n"])
                        file.close()


                elif choice[0] == "2":

                    print(CIRCLE_1+" MUSIC VOLUME LOUD")
                    print(CIRCLE_2+" MUSIC VOLUME MEDIUM")
                    print(CIRCLE_3+" MUSIC VOLUME SOFT")

                    flag1 = 0
                    while flag1 == 0:
                        choice1 = input(DIAMOND_BLACK+" Choose 1, 2, or 3, or C to Configuration Menu "+TRIANGLE_RIGHT_WHITE+" ")[0]

                        if choice1[0] == "1":
                            MUSICVOL_LOUD = 0.6
                            mixer.music.set_volume(MUSICVOL_LOUD)
                            print("Music set to LOUD")
                            data[2]=MUSICVOL_LOUD
                            flag1 = 1
                        elif choice1[0] == "2":
                            MUSICVOL_MED = 0.3
                            mixer.music.set_volume(MUSICVOL_MED)
                            print("Music set to MEDIUM")
                            data[2]=MUSICVOL_MED
                            flag1 = 1
                        elif choice1[0] == "3":
                            MUSICVOL_SOFT = 0.1
                            mixer.music.set_volume(MUSICVOL_SOFT)
                            print("Music set to SOFT")
                            data[2]=MUSICVOL_SOFT
                            flag1 = 1
                        elif choice1[0] == "c" or choice1[0] == "C":
                            flag1 = 1
                            setup()
                        else:
                            print("Sorry, That's not a correct option. Please try again.")
                            flag1 = 0

                    flag = 1

                else:
                    print("Sorry, That's not a correct option. Please try again.")
                    flag = 0

            with open("setupinfo.dat", "w") as file:
                file.writelines([str(data[0]) + "\n", str(data[1]) + "\n", str(data[2]) + "\n", str(data[3]) + "\n",
                                     str(data[4]) + "\n", str(data[5]) + "\n", str(data[6]) + "\n"])
                file.close()

            setup()


    def setup():
        str_title = "CONFIGURATION"
        level = 2

        titleHeadMaker(str_title, level)
        print(CIRCLE_1+ " AUDIO ON/OFF")
        print(CIRCLE_2+ " MUSIC ON/OFF + VOLUME")
        print(CIRCLE_3+ " RESET PLAYER "+PLAYERNAME+" AND SCORE")
        print(CIRCLE_4+ " FACTORY RESET")
        print(CIRCLE_M+ " RETURN TO GAME MENU")
        flag = 0
        while flag == 0:
            choice = input(DIAMOND_BLACK + " Choose an option: " + TRIANGLE_RIGHT_WHITE + " ")[0]
            if choice[0] == "1":
                audioONOFF(int(choice[0]))
                flag = 1
            elif choice[0] == "2":
                audioONOFF(int(choice[0]))
                flag = 1
            elif choice[0] == "3":
                flag = 1
                resetScore()
            elif choice[0] == "4":
                flag = 1
                resetFactory()
            elif choice[0] == "M" or choice[0] == "m":
                optionsMenu()
                flag = 1
            else:
                print(ARROW_RIGHT + " " + WRONG_CHOICE + " " + CIRCLE1)
                flag = 0

    #this function resets the player overall score

    def resetFactory():
        global PLAYERNAME,AUDION, MUSICON, MUSICVOL
        with open('setupinfo.dat', 'r') as file:
            data = file.read().splitlines()
        file.close()

        data[0] = 1 # default SOUNDS ON
        data[1] = 1 # default: MUSIC ON
        data[2] = 0.5  # default music level
        data[3] = "PLAYERONE" # default name is John Doe
        data[4] = 0 # score
        data[5] = 0 # wins
        data[6] = 0 # loses

        PLAYERNAME = data[3]

        flag = 0
        while flag == 0:
            choice = input(DIAMOND_BLACK+" Are you sure to factory reset? Press Y or N "+TRIANGLE_RIGHT_WHITE+ " ")[0]
            if choice[0] == "Y" or choice[0] == "y":
                data[0] = 1
                data[1] = 1
                data[2] = 0.3
                data[3] = "PLAYERONE"
                with open("setupinfo.dat", "w") as file:
                    file.writelines([str(data[0]) + "\n", str(data[1]) + "\n", str(data[2]) + "\n", str(data[3]) + "\n", str(data[4]) + "\n",
                 str(data[5]) + "\n", str(data[6]) + "\n"])
                file.close()
                print("Game was reset to factory default values and Game will restart")
                sleep(1)
                flag = 1
                beginGame(1)

            elif choice[0] == "N" or choice[0] == 'n':
                print("No changes were made to configuration values")
                sleep(1)
                flag = 0
                setup()
            else:
                print("Sorry, That's not a correct option. Please try again.")
                flag = 0

    def resetScore():
    #do something

        with open('setupinfo.dat', 'r') as file:
            data = file.read().splitlines()
        file.close()

        data[4] = 0 # score
        data[5] = 0 # wins
        data[6] = 0 # loses

        flag = 0
        while flag == 0:
            choice= input(DIAMOND_BLACK+" Are you sure to reset "+PLAYERNAME+" and scores to zero? Press Y or N "+TRIANGLE_RIGHT_WHITE+ " ")[0]
            if choice[0] == "Y" or choice[0] == "y":
                with open("setupinfo.dat", "w") as file:
                    file.writelines([str(data[0]) + "\n", str(data[1]) + "\n", str(data[2]) + "\n", str(data[3]) + "\n",
                                     str(data[4]) + "\n",
                                     str(data[5]) + "\n", str(data[6]) + "\n"])
                file.close()

                print(PLAYERNAME+"'s scores were reset to zero")
                sleep(1)
                flag = 1
                setup()
            elif choice[0] == "N" or choice[0] == 'n':
                print("Scores were not reset.")
                sleep(1)
                flag = 1
                setup()
            else:
                print("Sorry, That's not a correct option. Please try again.")
                flag = 0


    #function shows total wins, losses
    def statistics():
        with open('setupinfo.dat', 'r') as file:
            data = file.read().splitlines()
        file.close()

        score = data[4]
        wins = data[5]
        losses = data[6]

        print("\n")
        for n in range(0, WIDTH - 2):
            print(GREYBOX3, end="")

        print("\n")
        print("Last player      : "+ data[3])
        print("Cumulative Score : "+ data[4])
        print("Number of Wins   : "+ data[5])
        print("Number of Losses : "+ data[6])

        totalPlays = int(data[5]) + int(data[6])

        print("Number of Plays  : "+ str(totalPlays))

        if totalPlays == 0:
            percentageWins = "NA"
        else:
            percentageWins = (int(data[5])/totalPlays)*100

        print("Win Percentage   : "+ str(percentageWins) + "%")
        for n in range(0, WIDTH - 2):
            print(GREYBOX3, end="")
        print("\n")

        flag = 0
        while flag == 0:
            choice = input(DIAMOND_BLACK + " Enter M to return to Game Menu " + TRIANGLE_RIGHT_WHITE + " ")[0]

            if choice[0] == "M" or choice[0] == "m":
                flag = 1
                optionsMenu()
            else:
                print("Sorry, That is not a right choice. Try again")
                flag = 0


    # Function: OptionsMenu()
    # Displays the main menu of the game
    def optionsMenu():
        str_title = "MAIN MENU"
        level = 1
        titleHeadMaker(str_title, level)
        menuOption1 = "PLAY GAME"
        menuOption2 = "STATISTICS"
        menuOption3 = "SETUP"
        menuOption4 = "RETURN TO MAIN MENU"

        print(CIRCLE_1 + " " + menuOption1)
        print(CIRCLE_2 + " " + menuOption2)
        print(CIRCLE_3 + " " + menuOption3)
        print(CIRCLE_M + " " + menuOption4)

        flag = 0
        # make sure what we return is a valid option
        while flag == 0:
            choice = input(DIAMOND_BLACK + " Enter your choice 1, 2, 3, or M " + TRIANGLE_RIGHT_WHITE + " ")[0]
            if choice[0] == "1":
                flag = 1
                game(sets, deck)
            elif choice[0] == "2":
                flag = 1
                statistics()
            elif choice[0] == "3":
                flag = 1
                setup()
            elif choice[0] == "M" or choice == "m":  # to exit this game
                flag = 1
                print("Thank you for Playing. Returning to MAIN MENU")
                print("Play again soon "+PLAYERNAME+"!!")
                sleep(1)
                exit(0)
            else:
                print("Sorry, That is not a right choice. Try again")
                flag = 0


    #Function that retrieves user name
    def userName():
        global PLAYERNAME

        with open('setupinfo.dat', 'r') as file:
            data = file.read().splitlines()
        file.close()

        PLAYERNAME = data[3]
        wins= int(data[5])
        losses= int(data[6])

        if wins == 0 and losses == 0:
            print("WELCOME NEW PLAYER!\n")
            pName = input(DIAMOND_BLACK+ " Please enter your name " + TRIANGLE_RIGHT_WHITE + " ")
            flag=0
            while flag == 0:
                if pName is None:
                    print("Your name can't be empty. Please try again.")
                    flag = 0
                else:
                    PLAYERNAME = pName
                    data[3] = PLAYERNAME
                    flag = 1
        else:
            print("WELCOME BACK"+", "+PLAYERNAME + "!!")

        with open("setupinfo.dat", "w") as file:
            file.writelines([str(data[0])+"\n",str(data[1])+"\n",str(data[2])+"\n",str(data[3])+"\n",str(data[4])+"\n",str(data[5])+"\n",str(data[6])+"\n"])
            file.close()


    #beginGame is only called once.
    def beginGame(LEVEL):

        if AUDIOON == 1:
            thread_1 = Thread(target=sounds, args=(LEVEL,))
            thread_1.start()
        str_title = "WORD GUESSING GAME"

        level = LEVEL
        titleHeadMaker(str_title, level)

        userName()
        phrase = PLAYERNAME + ","+"Welcome to the" + str_title
        print("Please wait, Game is Loading...")
        sleep(1.2)

        if AUDIOON == 1:
            thread_02 = Thread(target=Text2speech, args=(phrase, 1))
            thread_02.start()

        sleep(1)
        if MUSICON == 1:
            snd = 4
            thread_0 = Thread(target=sounds, args=(snd,))
            thread_0.start()


    #Function sounds
    def sounds(snd):
        if snd == 1:  # game starts
            playsound("game_start.mp3")
        elif snd == 2:  # win ping
            playsound("win_ping.wav")
        elif snd == 3:  # lose ping
            playsound("lose_ping.wav")
        elif snd == 4:  # music 1
            mixer.init()
            mixer.music.load("music_2.mp3")
            mixer.music.set_volume(MUSICVOL)
            mixer.music.play(-1)
        else:
            print("You shouldn't be here")

    # function converts text to speech. Implemented different files to avoid any future file permission issues.
    def Text2speech(phrase, audioContent):
        tts = gTTS(text=phrase, lang='en', slow=False)
        if audioContent == 1:  # exclusive for player name
            tts.save('tts_cont_1.mp3')   # Saving the converted audio in a mp3 file.
            playsound('tts_cont_1.mp3')  # Playing that file
            os.remove('tts_cont_1.mp3')  # Removing that file
        elif audioContent == 2:  # exclusive for titles
            tts.save('tts_cont_2.mp3')
            playsound('tts_cont_2.mp3')
            os.remove('tts_cont_2.mp3')
        elif audioContent == 3:  # exclusive for categores
            tts.save('tts_cont_3.mp3')
            playsound('tts_cont_3.mp3')
            os.remove('tts_cont_3.mp3')
        elif audioContent == 4:  # exclusive for youwin
            tts.save('tts_cont_4.mp3')
            playsound('tts_cont_4.mp3')
            os.remove('tts_cont_4.mp3')
        elif audioContent == 5:  # exclusive for youlose
            tts.save('tts_cont_5.mp3')
            playsound('tts_cont_5.mp3')
            os.remove('tts_cont_5.mp3')
        elif audioContent == 6:  # exclusive for questions
            tts.save('tts_cont_6.mp3')
            playsound('tts_cont_6.mp3')
            os.remove('tts_cont_6.mp3')

    def beforeAnything():

        with open('setupinfo.dat', 'r') as file:
            data = file.read().splitlines()
        file.close()

        print("v0.9")
        return data


    myPrefs = beforeAnything()
    #initial global variables
    AUDIOON = int(myPrefs[0])
    MUSICON = int(myPrefs[1])
    MUSICVOL= float(myPrefs[2])

    LEVEL = 1
    beginGame(LEVEL)
    optionsMenu()
