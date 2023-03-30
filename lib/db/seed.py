from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Instructor, Dancer, Lesson

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///migrations_dance_match_app.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    

session.query(Instructor).delete()
session.commit()

prices = [20, 70, 150]
instructor = [
    Instructor(
        name=fake.name(), 
        rating=random.randint(1,5),
        price=random.choice(prices)
    )
for i in range(50)]

session.add_all(instructor)
session.commit()



session.query(Dancer).delete()
session.commit()

dancer = [
    Dancer(
        name=fake.name()
    )
for i in range(50)]

session.add_all(dancer)
session.commit()



session.query(Lesson).delete()
session.commit()

levels = ["Beginner", "Intermediate", "Advanced"]
age_groups = ["Kids", "Adults", "Seniors"]
styles = ["Salsa", "Flamenco", "Ballet", "Hip Hop", "Jazz"]


lesson = [
    Lesson(
        style=random.choice(styles),
        level=random.choice(levels),
        age_group=random.choice(age_groups),
        instructor_id=random.choice(instructor).id,
        dancer_id=random.choice(dancer).id
    )
for i in range(50)]

session.add_all(lesson)
session.commit()




