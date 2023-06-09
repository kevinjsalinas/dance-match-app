from models import Instructor, Dancer, Lesson
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker




class CLI:
    def __init__(self, user_input):
       self.instructors = [instructor for instructor in session.query(Instructor)]
       self.dancers = [dancer for dancer in session.query(Dancer)]
       self.lessons = [lesson for lesson in session.query(Lesson)]
       self.name = user_input
       self.start()


  #####
    #Show me a list of instructors
    def start(self):
       print(' ')
       print(' ')
       print(f'🕺🕺🕺🕺 Get ready to get your groove on, {self.name}! 🕺🕺🕺🕺')
       print(' ')
       print(' ')

       exit = False
       while exit == False:
             options = input(f'We\'re excited to match you with the right instructor. First, tell us about your dance experience. \n \nType "Beginner", "Intermediate", or "Advanced": ')
             print(' ') 
             print(' ') 
             level = options
             if options.lower() == 'beginner':
                 beginner_dance_choice(self)

             elif options.lower() == 'intermediate':
                 intermediate_dance_choice(self)

             elif options.lower() == 'advanced':
                 advanced_dance_choice(self)
             else:
               #added just now 
               print(' ')
               user_input = input('To see other options, type "more" else "exit": ')
               print(' ')
               if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                    print(f"Goodbye {self.name}")
                    quit()
             





    
def beginner_dance_choice(self):
    exit = False
    while exit == False:
             options = input(f'Great! What style of dance are you interested in learning? \n \nType "Salsa", "Flamenco", "Ballet", "Hip Hop", or "Jazz": ')
             print(' ') 
             print(' ')
             style = options 
             level = "Beginner"
             if options.lower() == 'salsa':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Salsa instructor for Beginners. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Beginner", Lesson.style == "Salsa")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Beginner", Lesson.style == "Salsa")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Beginner", Lesson.style == "Salsa")).all()
                       print('💃🕺💃 All Beginner Salsa Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Beginner", Lesson.style == "Salsa")).all()
                        print('💃🕺💃 All Beginner Salsa Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'flamenco':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Flamenco instructor for Beginners. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n' +\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Beginner", Lesson.style == "Flamenco")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Beginner", Lesson.style == "Flamenco")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Beginner", Lesson.style == "Flamenco")).all()
                       print('💃🕺💃 All Beginner Flamenco Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Beginner", Lesson.style == "Flamenco")).all()
                        print('💃🕺💃 All Beginner Flamenco Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'ballet':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Ballet instructor for Beginners. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Beginner", Lesson.style == "Ballet")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Beginner", Lesson.style == "Ballet")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Beginner", Lesson.style == "Ballet")).all()
                       print('💃🕺💃 All Beginner Ballet Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Beginner", Lesson.style == "Ballet")).all()
                        print('💃🕺💃 All Beginner Ballet Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'hip hop':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Hip Hop instructor for Beginners. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Beginner", Lesson.style == "Hip Hop")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Beginner", Lesson.style == "Hip Hop")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Beginner", Lesson.style == "Hip Hop")).all()
                       print('💃🕺💃 All Beginner Hip Hop Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Beginner", Lesson.style == "Hip Hop")).all()
                        print('💃🕺💃 All Beginner Hip Hop Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'jazz':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Jazz instructor for Beginners. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Beginner", Lesson.style == "Jazz")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Beginner", Lesson.style == "Jazz")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Beginner", Lesson.style == "Jazz")).all()
                       print('💃🕺💃 All Beginner Jazz Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Beginner", Lesson.style == "Jazz")).all()
                        print('💃🕺💃 All Beginner Jazz Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             else:
                exit = True

def intermediate_dance_choice(self):
    exit = False
    while exit == False:
             options = input(f'Great! What style of dance are you interested in learning? \n \nType "Salsa", "Flamenco", "Ballet", "Hip Hop", or "Jazz": ')
             print(' ') 
             print(' ') 
             style = options 
             level = "Intermediate"
             if options.lower() == 'salsa':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Salsa instructor for Intermediate. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Intermediate", Lesson.style == "Salsa")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Intermediate", Lesson.style == "Salsa")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Intermediate", Lesson.style == "Salsa")).all()
                       print('💃🕺💃 All Intermediate Salsa Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Intermediate", Lesson.style == "Salsa")).all()
                        print('💃🕺💃 All Intermediate Salsa Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'flamenco':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Flamenco instructor for Intermediate. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Intermediate", Lesson.style == "Flamenco")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Intermediate", Lesson.style == "Flamenco")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Intermediate", Lesson.style == "Flamenco")).all()
                       print('💃🕺💃 All Intermediate Flamenco Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Intermediate", Lesson.style == "Flamenco")).all()
                        print('💃🕺💃 All Intermediate Flamenco Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'ballet':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Ballet instructor for Intermediate. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Intermediate", Lesson.style == "Ballet")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Intermediate", Lesson.style == "Ballet")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Intermediate", Lesson.style == "Ballet")).all()
                       print('💃🕺💃 All Intermediate Ballet Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Intermediate", Lesson.style == "Ballet")).all()
                        print('💃🕺💃 All Intermediate Ballet Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'hip hop':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Hip Hop instructor for Intermediate. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Intermediate", Lesson.style == "Hip Hop")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Intermediate", Lesson.style == "Hip Hop")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Intermediate", Lesson.style == "Hip Hop")).all()
                       print('💃🕺💃 All Intermediate Hip Hop Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Intermediate", Lesson.style == "Hip Hop")).all()
                        print('💃🕺💃 All Intermediate Hip Hop Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'jazz':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Jazz instructor for Intermediate. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Intermediate", Lesson.style == "Jazz")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Intermediate", Lesson.style == "Jazz")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Intermediate", Lesson.style == "Jazz")).all()
                       print('💃🕺💃 All Intermediate Jazz Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Intermediate", Lesson.style == "Jazz")).all()
                        print('💃🕺💃 All Intermediate Jazz Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 
             else:
                exit = True


def advanced_dance_choice(self):
    exit = False
    while exit == False:
             options = input(f'Great! What style of dance are you interested in learning? \n \nType "Salsa", "Flamenco", "Ballet", "Hip Hop", or "Jazz": ')
             print(' ') 
             print(' ') 
             style = options
             level = "Advanced"
             if options.lower() == 'salsa':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Salsa instructor for Experts. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Advanced", Lesson.style == "Salsa")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      
                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Advanced", Lesson.style == "Salsa")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Advanced", Lesson.style == "Salsa")).all()
                       print('💃🕺💃 All Advanced Salsa Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Advanced", Lesson.style == "Salsa")).all()
                        print('💃🕺💃 All Advanced Salsa Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'flamenco':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Flamenco instructor for Experts. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Advanced", Lesson.style == "Flamenco")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      
                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Advanced", Lesson.style == "Flamenco")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Advanced", Lesson.style == "Flamenco")).all()
                       print('💃🕺💃 All Advanced Flamenco Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Advanced", Lesson.style == "Flamenco")).all()
                        print('💃🕺💃 All Advanced Flamenco Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'ballet':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Ballet instructor for Experts. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Advanced", Lesson.style == "Ballet")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Advanced", Lesson.style == "Ballet")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Advanced", Lesson.style == "Ballet")).all()
                       print('💃🕺💃 All Advanced Ballet Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Advanced", Lesson.style == "Ballet")).all()
                        print('💃🕺💃 All Advanced Ballet Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'hip hop':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Hip Hop instructor for Experts. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Advanced", Lesson.style == "Hip Hop")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Advanced", Lesson.style == "Hip Hop")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Advanced", Lesson.style == "Hip Hop")).all()
                       print('💃🕺💃 All Advanced Hip Hop Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Advanced", Lesson.style == "Hip Hop")).all()
                        print('💃🕺💃 All Advanced Hip Hop Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 

             elif options.lower() == 'jazz':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Jazz instructor for Experts. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n'+\
                                f'Type "dancers" to see other dancers in your level and style. \n\n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Advanced", Lesson.style == "Jazz")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
                        join_lesson(style, level)
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()      

                    elif options.lower() == 'price':
                         prices = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Advanced", Lesson.style == "Jazz")).all()
                         print('Instructors by Price 💵')
                         print(' ')
                         price_list = (prices)
                         show_instructor = []
                         for i in price_list:
                             show_instructor.append(i[0])
                         show_instructor.sort(key=lambda i:i.price)
                         for price in show_instructor:
                              print(f"-- {price.name}: ${price.price}")
                         print(' ')
                         join_lesson(style, level)
                         #added just now 
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()  
                    elif options.lower() == 'all':
                       all = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Lesson.level == "Advanced", Lesson.style == "Jazz")).all()
                       print('💃🕺💃 All Advanced Jazz Instructors 💃🕺💃')
                       print(' ')
                       for instructor in all:
                           print(f"-- {instructor[0].name}")
                       print(' ')
                       join_lesson(style, level)
                       #added just now 
                       print(' ')
                       user_input = input('To see other options, type "more" else "exit": ')
                       print(' ')
                       if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                         print(f"Goodbye {self.name}")
                         quit()
                    elif options.lower() == 'dancers':
                        dancers = session.query(Dancer, Lesson).filter(and_(Dancer.id == Lesson.dancer_id, Lesson.level == "Advanced", Lesson.style == "Jazz")).all()
                        print('💃🕺💃 All Advanced Jazz Dancers 💃🕺💃')
                        print(' ')
                        for dancer in dancers:
                              print(f"-- {dancer[0].name}")
                        print(' ')
                        #added just now 
                        print(' ')
                        user_input = input('To see other options, type "more" else "exit": ')
                        print(' ')
                        if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit()
                    else:
                         ##### just added
                         print(' ')
                         user_input = input('To see other options, type "more" else "exit": ')
                         print(' ')
                         if user_input == "Exit" or user_input == 'EXIT' or user_input == 'exit':
                              print(f"Goodbye {self.name}")
                              quit() 
             else:
                exit = True


def join_lesson(style, level):
    instructor_name = input("Type the name of the instructor you'd like to enroll with OR hit enter: ")
    found_instructor = session.query(Instructor).filter(Instructor.name == instructor_name).first()
#     print(found_instructor)
    dancer = session.query(Dancer).filter(Dancer.name == user_input).first()
    if dancer and found_instructor:
        lesson = Lesson(
            style = style,
            level = level,
            age_group = "Kids",
            instructor_id = found_instructor.id,
            dancer_id = dancer.id
        )
        print("")
        print(f"🎊 🥳 🎊 Congrats! Get excited for your first lesson with {instructor_name}! 🎊 🥳 🎊")
        session.add(lesson)
        session.commit()
    else:
        print("")




if __name__ == '__main__':
    engine = create_engine('sqlite:///migrations_dance_match_app.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    print(" ")
    print("__        __     _                                _           ____                             __  __         _         _                  _ ") 
    print("\ \      / /___ | |  ___  ___   _ __ ___    ___  | |_  ___   |  _ \   __ _  _ __    ___  ___  |  \/  |  __ _ | |_  ___ | |__    ___  _ __ | |")
    print(" \ \ /\ / // _ \| | / __|/ _ \ | '_ ` _ \  / _ \ | __|/ _ \  | | | | / _` || '_ \  / __|/ _ \ | |\/| | / _` || __|/ __|| '_ \  / _ \| '__|| |")
    print("  \ V  V /|  __/| || (__| (_) || | | | | ||  __/ | |_| (_) | | |_| || (_| || | | || (__|  __/ | |  | || (_| || |_| (__ | | | ||  __/| |   |_|")
    print("   \_/\_/  \___||_| \___|\___/ |_| |_| |_| \___|  \__|\___/  |____/  \__,_||_| |_| \___|\___| |_|  |_| \__,_| \__|\___||_| |_| \___||_|   (_)")
    print(" ")
    print(" ")
    print(" ")
    user_input = input("Please enter your name: ")
    print(" ")
    print(" ")
    print(" ")
    print(" o   \ o /  _ o         __|    \ /     |__        o _  \ o /   o    ")
    print("/|\    |     /\   ___\o   \o    |    o/    o/__   /\     |    /|\   ")
    print("/ \   / \   | \  /)  |    ( \  /o\  / )    |  (\  / |   / \   / \   ")
    print(" ")
    CLI(user_input)
