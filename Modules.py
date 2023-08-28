import time
from random import *
import requests
import bs4
from translate import Translator
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pyttsx3
from os import system, name
from time import sleep
from plyer import notification
import mysql.connector as cn


# Connection

db=cn.connect(host='localhost',user='root',passwd='1234',database='Riley',
              charset='utf8')
cur=db.cursor()



class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
def reminder(ch,di,t,mess):
    if ch==1:
        if t in di:
            print('Reminder for the entered time is already set.')
        else:
            di[t]=mess
    # time.sleep(t)
    # print(mess)
    start_time=time.time()
    if time.time()==start_time+t:
        print(mess)

def time_checker():
    start_time = time.time()
    if time.time() == start_time + t:
        print(mess)

def quiz():
    cur.execute('select * from leaderboard where username=username')
    recs=cur.fetchall()
    games=recs[0][4]
    rating=recs[0][5]
    while True:
        print('1. To see the full leaderboard')
        print('2. To continue with quiz')
        print('3. Exit')
        user_choice3=int(input('Enter your choice: '))
        if user_choice3==1:
            cur.execute('select * from leaderboard')
            recs=cur.fetchall()
            print(recs)
        elif user_choice3==3:
            break
        elif user_choice3==2:
            print('Lets start')
            print('RULES OF THE QUIZ:- ')
            print('1. The quiz consists of 3 questions from each category-')
            print('Sports, Movies and Cartoons')
            quiz_dic={}
            q1='Who becomes the first cricketer to hit six sixes in an over in ' \
                     'one-day international cricket?\n 1. Yuvraj Singh\n 2. Kieron Pollard\n 3. Herschelle Gibs' \
                     '\n 4 Viv Richards'
            q2='Which Country won the first FIFA World Cup?\n1. Argentina' \
                     '\n2. Uruguay\n3. Italy\n4. Brazil'
            q3='Who is the first and currently the only batsman to score ' \
                 'double hundreds in four consecutive test series?\n1. Virat Kohli' \
                 '\n 2. Rohit Sharma\n 3. A.B. de Villiers\n4. Brian Lara'
            q4='Which of the following footballers has a world record' \
                 ' of highest goal score for a single club?\n1. Lionel Messi (Barcelona FC)\n' \
                 '2. Pele (Santos FC)\n' \
                 '3. Gerd Muller (Bayern Munich)\n' \
                 '4. Fernando Peyrotes (Sporting CP)'
            q5='Neeraj Chopra win the first ever olympic gold medal for India in which of the following sports\n' \
                 '1. 400 m hurdles\n2. Javelin Throw\n' \
                 '3. High Jump\n4. Long Jump'
            q6='Who carried the Indian flag during the closing ceremony of the Tokyo Olympics 2020?\n' \
                 '1. Neeraj Chopra\n2. PV Sindhu\n' \
                 '3. Bajrang Punia\n4. Ravi Kumar'
            q7='Who among the following were selected for the Rajiv Gandhi Khel Ratna Award 2019?\n' \
                 '1. Vijay Kumar and Yogeshwar Dutt\n2. Sakshi Malik and Jitu Rai\n' \
                 '3. Virat Kohli and Mirabai Chanu\n' \
                 '4. Bajrang Punia and Deepa Malik'
            q8='Which of these Badminton playersbecame 1st Indian to win a gold medal in' \
                 'Badminton World Championship?\n[1] PV Sindhu\n[2] Saina Nehwal\n' \
                 '[3] Srikanth Kidambi\n[4] Parupalli Kashyap'
            q9='Who Won 10th italian open title 2021?\n' \
                 '1. Novak Djokovic\n' \
                 '2. Rafael Nadal\n' \
                 '3. Dominic Thiem\n4. Stefanos Tsitsipas'
            q10='In which of these cities the famous "Eden Garden" Stadium is located?\n' \
            '[1] Mumbai\n' \
            '[2] Delhi\n' \
            '[3] Jaipur\n[4] Kolkata'

            quiz_dic[q1]=3

            quiz_dic[q2]=2

            quiz_dic[q3]=1

            quiz_dic[q4]=1

            quiz_dic[q5]=2

            quiz_dic[q6]=3

            quiz_dic[q7]=3

            quiz_dic[q8]=1

            quiz_dic[q9]=2

            quiz_dic[q10]=4

            random_nos=['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10']
            ele_in_lst=10
            score=0
            for i in range(5):
                question_no = ''
                random_no=randint(0,(ele_in_lst-1))
                question_no+=random_nos[random_no]
                question_no2=eval(question_no)
                random_nos.pop(random_no)
                ele_in_lst-=1
                print(question_no2)
                user_answer=int(input('Enter the option no.: '))
                if user_answer==quiz_dic[question_no2]:
                    score+=1
                    print(color.DARKCYAN+color.BOLD+"Congrats!!! Correct answer"+color.END)
                else:
                    print(color.UNDERLINE+color.RED+"Sorry... Incorrect Answer "+color.END)

            print('Quiz report: ')
            print('Your score is',score,'out of 5.')

            cur.execute('update leaderboard set points=points+{} where'
                        'username=username'.format(score))
            db.commit()
            cur.execute('update leaderboard set no_of_games=no_of_games+1 where'
                        ' username=username')
            db.commit()
            cur.execute('update leaderboard set rating=points/no_of_games where'
                        'username=username'.format(score))

            db.commit()
            print('Correct answers: ',score)
            print('Incorrect answers: ',(5-'score'))
            x=score
            y=5-score

            user_choice2=input('To see your performance through graph, Press G\n Press any hghgfhgbcrd')

            if user_choice2=='G':
                plotter(x, y, 'bar')
                plotter(x, y, 'pie')
                plotter(x, y, 'line')

            cur.execute('select * from leaderboard where username=username')
            recs=cur.fetchall()
            rank=recs[0][0]
            points=recs[0][2]
            no_of_games=recs[0][4]
            rating=recs[0][5]
            if rating>=4.5 and no_of_games>=3:
                division='Master'
                cur.execute('update leaderboard set division="Master" where username=username')
                db.commit()
            elif rating>=4 and no_of_games>=2:
                division='Ultra'
                cur.execute('update leaderboard set division="Ultra" where username=username')
                db.commit()
            elif rating>=3 and no_of_games>=2:
                division='Great'
                cur.execute('update leaderboard set division="Great" where username=username')
                db.commit()
            else:
                cur.execute('update leaderboard set division="Normal" where username=username')
                db.commit()
                division='Normal'

            print('After this quiz, there has been immediate change in the leaderboard rankings.')
            print('Your current ranking is',rank,'and total points are',points)
            print('Your rating is',rating,'and the division is',division)
        else:
            print('Invalid choice')

def authenticate():
    print("Hello USER.")
    checker = 0
    # users = {'Sanchit': 'genius'}

    while checker == 0:
        print('For logging in, press L')
        print('For signing in, press S')
        print('For exiting from the program, press E')
        user_choose = input('Enter your choice: ')

        if user_choose == 'L' or user_choose == 'l':
            cur.execute('select * from users')
            recs = cur.fetchall()
            users = []
            passes = []
            for i in recs:
                users.append(i[0])
                passes.append(i[1])
            username = input('Enter username: ')
            for j in users:

                if username == j:
                    password = input('Enter password: ')
                    if password == passes[users.index(j)]:
                        print('Successfully Logged in')
                        checker = 1
                        break
                    else:
                        print('Unsuccessful. Incorrect password.')
                        break
            else:
                print('Username not found')

        elif user_choose == 'S' or user_choose == 's':
            cur.execute('select * from users')
            recs = cur.fetchall()
            users = []
            passes = []
            for i in recs:
                users.append(i[0])
                passes.append(i[1])
            new_user = input('Enter your username: ')
            if new_user not in users:

                new_pass = input('Enter your password: ')
                re_pass = input('Re-enter your password: ')
                if new_pass == re_pass:
                    cur.execute('insert into users values("{}","{}")'.format(new_user, new_pass))

                    cur.execute('insert into leaderboard values(len(users),"new_user",0,"Normal")')
                    db.commit()
                    print('Account successfully created.')
                    print('Now please log in by using the saved credentials.')
                    # print('I am RILEY, your virtual assistant. Nice to meet you.')
                elif new_pass != re_pass:
                    print('Re-entered password does not match your password.')


            elif new_user in users:
                print('The entered username already exists.')
                print('Either log in or choose a different username')

        elif user_choose == 'E':

            print('Thanks for talking to me.')
            print('Regards RILEY')
            outer_loop_decider = 1


def search_question():
    query=input('Enter your question: ').split()
    new_str=''
    for k in query:
        new_str+=k+'+'

    # Generating the url
    url = "https://google.com/search?q="+new_str

    # Sending HTTP request
    request_result = requests.get(url)

    # Pulling HTTP data from internet
    soup = bs4.BeautifulSoup(request_result.text
                             , "html.parser")

    # Finding temperature in Celsius.
    # The temperature is stored inside the class "BNeawe".
    temp = soup.find("div", class_='BNeawe').text

    print(temp)


def lang_translate():
    translator= Translator(to_lang="Spanish")
    translation = translator.translate("Good Morning!")
    print (translation)

def take_picture():
    videocaptureobject = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret,frame = videocaptureobject.read()
    cv2.imwrite("NewPicture.jpg",frame)
    videocaptureobject.release()
    cv2.destroyAllWindows()

def plotter(x,y,type):
    if type == "line":
        plt.plot(x,y)
    elif type == "pie":
        plt.pie(x,labels=y)
    elif type == "bar":
        plt.bar(x,y)

    plt.show()

