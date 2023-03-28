from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Instructor, Lesson, Dancer

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///migrations_dance_match_app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

instructor1 = Instructor(name="bob")
session.add_all([instructor1])
session.commit()

# session.query(Instructor).delete()
# session.commit()

# instructor = [
#     Instructor(
#         name=fake.name()
#     )
# for i in range(5)]

# session.add_all(instructor)
# session.commit()


# session.query(Lesson).delete()
# session.commit()

# lesson = [
#     Lesson(
#         style=fake.word()
#     )
# for i in range(5)]

# session.add_all(lesson)
# session.commit()


# session.query(Dancer).delete()
# session.commit()

# dancer = [
#     Dancer(
#         name=fake.name()
#     )
# for i in range(5)]

# session.add_all(dancer)
# session.commit()




