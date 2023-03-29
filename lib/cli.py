from db.models import Instructor, Dancer, Lesson
from sqlalchemy import create_engine
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
        print(f'🕺🕺🕺🕺 Get ready to get your groove on {self.name} 🕺🕺🕺🕺')
        print(' ')

        exit = False
        while exit == False:
                options = input(f'Type "instructors" to see a list of instructors, type "styles" to see different styles of lessons: ')
                print(' ') 
                print(' ') 
                if options.lower() == 'instructors':
                     show_instructors_list(self)
                elif options.lower() == 'styles':
                     show_lessons_list(self)
                else:
                    exit = True
                    
        
                # print(' ')
                # user_input = input("Would you like to stop now? (Type Y/N): ")
                # print(' ')
                # if user_input == "Y" or user_input == 'y':
                #     exit = True

        # printer(self.name)



def show_instructors_list(self):
    print_instructors(self.instructors)


def print_instructors(instructors):

    print(' ')
    print('🕺 Instructors 🕺')
    print(' ')
    for instructor in instructors:
        print(f'{instructor.id}. {instructor.name}')

    print(' ')


def show_lessons_list(self):
    print_lessons(self.lessons)


def print_lessons(lessons):
    print(' ')
    print('** Lessons **')
    print(' ')

    for lesson in lessons:
        print(f'{lesson.id}. {lesson.style}')
    
    print(' ')


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