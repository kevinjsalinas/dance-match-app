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
             

       # printer(self.name)



    
def beginner_dance_choice(self):
    exit = False
    while exit == False:
             options = input(f'Great! What style of dance are you interested in learning? \n \nType "Salsa", "Flamenco", "Ballet", "Hip Hop", or "Jazz": ')
             print(' ') 
             print(' ') 
             if options.lower() == 'salsa':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Salsa instructor for Beginners. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n \n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Beginner", Lesson.style == "Salsa")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
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
                                f'Type "all" to see all instructors. \n \n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Beginner", Lesson.style == "Flamenco")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
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
                                f'Type "all" to see all instructors. \n \n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Beginner", Lesson.style == "Ballet")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
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
                                f'Type "all" to see all instructors. \n \n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Beginner", Lesson.style == "Hip Hop")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
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
                                f'Type "all" to see all instructors. \n \n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Beginner", Lesson.style == "Jazz")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
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
             if options.lower() == 'salsa':
                 exit = False
                 while exit == False:
                    options = input(f'Groovy. Let\'s help you choose a Salsa instructor for Intermediate. \n \n--------------------------------------------------------------------\n \n' +\
                                f'Type "ratings" to see top-rated instructors with 4 stars or higher. \n' +\
                                f'Type "price" to see instructors sorted by price. \n' +\
                                f'Type "all" to see all instructors. \n \n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Intermediate", Lesson.style == "Salsa")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
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
                                f'Type "all" to see all instructors. \n \n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Intermediate", Lesson.style == "Flamenco")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
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
                                f'Type "all" to see all instructors. \n \n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Intermediate", Lesson.style == "Ballet")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
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
                                f'Type "all" to see all instructors. \n \n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Intermediate", Lesson.style == "Hip Hop")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
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
                                f'Type "all" to see all instructors. \n \n')
                    print(' ') 
                    print(' ') 
                    if options.lower() == 'ratings':
                        ratings = session.query(Instructor, Lesson).filter(and_(Instructor.id == Lesson.instructor_id, Instructor.rating >= 4, Lesson.level == "Intermediate", Lesson.style == "Jazz")).all()
                        print('🌟🕺🌟 Top-Rated Instructors 🌟🕺🌟')
                        print(' ')
                        for instructor in ratings:
                              print(f"-- {instructor[0].name}, {instructor[0].rating} stars")
                        print(' ')
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
    pass




if __name__ == '__main__':
    engine = create_engine('sqlite:///migrations_dance_match_app.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input('Welcome to Dance Matcher! Please enter your name: ')
    CLI(user_input)




  
# def make_bottle(self):
#     user_grape = input("Type the number of the grape from the list above: ")
#     user_winery = input("Type the number of the winery from the list above: ")
#     year = input("What vintage is the bottle?: " )
#     price = input("How much did you pay for the bottle?: " )
#     score = input("How would you rate it on a scale of 1-10?: " )

#     bottle = Bottle(
#             price = price,
#             score = score,
#             year = year,
#             grape_id = self.grapes[int(user_grape) - 1].id,
#             winery_id = self.wineries[int(user_winery) - 1].id
#     )

#     session.add(bottle)
#     session.commit()

#     self.bottles.append(bottle)
#     print(' ')
#     print('Congratulations! You have added the following wine to your Vitual Cellar!')

#     print_bottle(bottle)


       
# def printer(user_input):
#     print(' ')
#     print(f'Goodbye {user_input}!')


          #              print(f'{text.center(202)}')
          #              price_text = '\n'.join(['{}.....${}'.format(*t).center(200) for t in zip(instructor_names, instructor_prices)])
          #              print(f'{price_text}')