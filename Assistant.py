from Modules import *

outer_loop_decider=0

while outer_loop_decider==0:
    authenticate()

    loop_decider=0
    while loop_decider==0:
        print('I can do the following tasks. ')
        print('1. Reminders')
        print('2. Take a picture')
        print('3. Play a Quiz')
        print('4. Search information')
        print('5. Translate language')
        choice1 = int(input('Enter the task number you want me to do: '))
        if choice1 == 1:
            reminder(1,{},10,'Hello')
        elif choice1==2:
            take_picture()
            print('Picture taken')
            print('Image saved as NewPicture')
        elif choice1==3:
            quiz()
        elif choice1==4:
            search_question()
        elif choice1==5:
            lang_translate()
        elif choice1==6:
            loop_decider=1
