import random
import sys

"""
Created on Web Oct 16 18:26:06 2018
@author: Pradeep Narayan
"""
"""
    DocString:

    A) Introduction:
        'QuizTime has 4 categories to choose from.'
        'Each category has 3 randomly selected questions to choose from. The question are of varying difficulty levels - Easy, Medium & Hard.'
        'Easy questions are scored less and Hard questions are worth more. You need to score 1000 or more to win a trip to Bahamas for 2 people.'

    B) Known Bugs and/or Errors:
    Questions repeat within the same category
"""

def initGame():
    printline()
    print("""Welcome to QuizTime! QuizTime has 4 categories to choose from.'
          'Each category has 3 randomly selected questions to choose from. The question are of varying difficulty levels - Easy, Medium & Hard.'
          'Easy questions are scored less and Hard questions are worth more. You need to score 1000 or more to win a trip to Bahamas for 2 people.'""")
    printline()
    input('Press Enter to begin the Quiz!\n')
    initInstructions()

def initInstructions():
    printline()
    pointsAcquired = gameStages()
    print("-----------------------")
    print(f"  PointsAquired={pointsAcquired}")
    print("-----------------------\n")
    if (pointsAcquired >= 1000):
        print("Congratulations!! You have Won a trip Bahamas!!!")
    else:
        print(f"Insufficient points! Please try again!")

def printCategory(categories):
    strCat = 'Choose from the following categories\n'
    for cat in categories:
        if cat == 1:
            strCat += '\tCategory 1 : History\n'
        elif cat == 2:
            strCat += '\tCategory 2 : General Knowledge\n'
        elif cat == 3:
            strCat += '\tCategory 3 : Sports\n'
        elif cat == 4:
            strCat += '\tCategory 4 : Movies\n'
    print(strCat);

def gameStages():
    pointsAcquired = 0
    easyPoints, mediumPoints, hardPoints = 50, 75, 150
    historyQuestionsList = [['Who was the first president of the United States of America?\n\tA. Thomas Jefferson\n\tB. George Washington\n\tC. Abraham Lincoln\n\tD. John Quincy Adams',
                                'B', easyPoints],
                            ['When did French Revolution began?\n\tA. 1785\n\tB. 1789\n\tC. 1795\n\tD. 1799', 'B',
                                 mediumPoints], ['When did World War 1 finish?\n\tA. 1917\n\tB. 1919 \n\tC. 1918\n\tD. 1920', 'B',
                                 easyPoints],
                            ['Who was the president of the United States duing Civil War?\n\tA. Adam Smith\n\tB. Abraham Lincoln \n\tC. Andrew Johnson\n\tD. James Buchanan',
                                'B', mediumPoints],
                            ['When did India became Independent from British Rule?\n\tA. 1934\n\tB. 1945\n\tC. 1947 \n\tD. 1948',
                                'C', mediumPoints],
                            ['Who wrote the book Das Capital?\n\tA. Vladimie Lenin\n\tB. Adam Smith\n\tC. Karl Marx \n\tD. Max Mueller',
                                'C', hardPoints],
                            ['When was Germany Unified by Bismarck?\n\tA. 1874\n\tB. 1871 \n\tC. 1878\n\tD. 1875',
                             'B', hardPoints]]

    moviesQuestionsList = [['Which movie has won the maximum number of Oscars?\n\tA. Avataar\n\tB. Schindlers List\n\tC. Ben-hur \n\tD. Jurassic Park',
                               'C', hardPoints],
                           ['Who amoongst the following has the higher number of Oscar Wins?\n\tA.Jack Nicholson\n\tB.Meryl Streep\n\tC.Ingrid Bergmann\n\tD.Katharine Hepburn ',
                               'D', hardPoints],
                           ['Who is the director of the movie Jurassic Park?\n\tA. Richard Attenborough\n\tB. Steven Spielberg \n\tC. James Cameron\n\tD. Manoj Night Shymalan',
                               'B', easyPoints],
                           ['Where is Hollywood Located?\n\tA. New York\n\tB. Los Angeles \n\tC. Florida\n\tD. Washington',
                               'B', easyPoints],
                           ['In which Country the Film Industry is known as Bollywood\n\tA. Iran\n\tB. Bangladesh\n\tC. Sri Lanka\n\tD. India ',
                               'D', mediumPoints],
                           ['Who directed the Avataar?\n\tA. Michael Caine\n\tB. Steven Spielberg\n\tC. James Cameron \n\tD. Jeff Goldblum',
                               'C', mediumPoints]]

    genknowQuestionsList = [['Who is the current CEO of Google\n\tA. Sundar Pichai\n\tB. Sheryl Sandberg\n\tC. Satya Nadella\n\tD. Sundar Rajan',
                                'A', mediumPoints],
                            ['Who is the current secretary general of the United Nations?\n\tA. Ban Ki Moon\n\tB. António Guterres \n\tC  Ki Ban Mooon\n\tD. Kofi Annan',
                                'B', hardPoints],
                            ['In which state is Harvard Business School located?\n\tA. MASSACHUSSETS \n\tB. CONNECTICUT\n\tC. BOSTON\n\tD. NEW JERSEY',
                                'A', mediumPoints],
                            ['On which day is American Independence Day Celebrated?\n\tA. 4th Aug\n\tB. 3rd July\n\tC. 4th July \n\tD. 3rd Sep',
                                'C', easyPoints],
                            ['Which is most spoken language in the world\n\tA. Mandarin \n\tC. Arabic\n\tB. English\n\tD. Spanish',
                                'A', easyPoints],
                            ['Who invented Python language?\n\tA. Guido van Rossum \n\tB. Dennis Ritchie\n\tC. Bill Gates\n\tD. Kai Fu',
                                'A', easyPoints]]

    sportsQuestionsList = [['Who is the current 100 meters world record holder?\n\tA. Usain Bolt\n\tB. Christian Coleman\n\tC. Tyson Gay\n\tD. Asafa Powell',
                               'A', easyPoints],
                           ['Who won the Women Wimbeldon Championship in 2019\n\tA. Venus Williams\n\tB. Serena William\n\tC. Simona Halep\n\tD. Ashleigh Barty',
                               'C', mediumPoints],
                           ['Which Country did France defeat in the FIFA World cup semifinal in 2018?\n\tA. England\n\tB. Belgium\n\tC. Croatia\n\tD. Brazil',
                               'B', hardPoints],
                           ['Where will the next FIFA world cup in 2022 be held?\n\tA. India\n\tB. UAE\n\tC. Saudi Arabia\n\tD. Qatar',
                               'D', mediumPoints],
                           ['Where will the Summer Olympics be held in 2020?\n\tA. USA\n\tB. Germany\n\tC. England\n\tD. Japan',
                               'D', easyPoints]]

    catsUnSelected = ["1", "2", "3", "4"]
    countOfCategories, invalidChoiceCount = 1, 0;

    while countOfCategories <= 4:
        printCategory(catsUnSelected)
        categoryChoice = input(f'Please choose Category {catsUnSelected} > ')
        if categoryChoice in catsUnSelected:
            catsUnSelected.remove(categoryChoice)
        elif invalidChoiceCount == 2:
            print("\nYou exceeded maximum amount of wrong inputs, Game Over!!!")
            input("Press Enter to exit...")
            sys.exit()
        else:
            invalidChoiceCount +=1;
            print(f"\n> Wrong choice, Please select the valid category again! {3 - invalidChoiceCount} try left\n")
            continue

        countOfCategories += 1

        if categoryChoice == "1":
            print('\nYou have chosen General History Category\n')
            questionsCount = 0
            while questionsCount < 3:
                questionItem = random.choice(historyQuestionsList)
                question, answer, ansPoints = questionItem[0], questionItem[1], questionItem[2]
                print(question)
                userAns = input('Please enter your choice>')
                if (userAns.lower() == answer.lower()):
                    pointsAcquired = pointsAcquired + ansPoints;
                    print(f"\nCorrect Answer!!!\nTotal Points: {pointsAcquired}")
                questionsCount = questionsCount + 1

        elif categoryChoice == "2":
            print('\nYou have chosen General Knowledge Category\n')
            questionsCount = 0
            while questionsCount < 3:
                questionItem = random.choice(genknowQuestionsList)
                question, answer, ansPoints = questionItem[0], questionItem[1], questionItem[2]
                print(question)
                userAns = input('Please enter your choice>')
                if (userAns.lower() == answer.lower()):
                    pointsAcquired = pointsAcquired + ansPoints;
                    print(f"\nCorrect Answer!!!\nTotal Points: {pointsAcquired}")
                questionsCount = questionsCount + 1

        elif categoryChoice == "3":
            print('\nYou have chosen Sports Category\n')
            questionsCount = 0
            while questionsCount < 3:
                questionItem = random.choice(sportsQuestionsList)
                question, answer, ansPoints = questionItem[0], questionItem[1], questionItem[2]
                print(question)
                userAns = input('Please enter your choice>')
                if (userAns.lower() == answer.lower()):
                    pointsAcquired = pointsAcquired + ansPoints;
                    print(f"\nCorrect Answer!!!\nTotal Points: {pointsAcquired}")

                questionsCount += 1

        elif categoryChoice == "4":
            print('\nYou have chosen Movies Category\n')
            questionsCount = 0
            while questionsCount < 3:
                questionItem = random.choice(moviesQuestionsList)
                question, answer, ansPoints = questionItem[0], questionItem[1], questionItem[2]
                print(question)
                userAns = input('Please enter your choice>')
                if (userAns.lower() == answer.lower()):
                    pointsAcquired = pointsAcquired + ansPoints;
                    print(f"\nCorrect Answer!!!\nTotal Points: {pointsAcquired}")

                questionsCount += 1

        if countOfCategories < 4:
            print("\nLet's go to next round...\n")

    return pointsAcquired;

def printline():
    print('*' * 100 + "\n")

initGame()
