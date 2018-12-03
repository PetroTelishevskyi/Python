from models import db, Contact
from faker import Factory

fake = Factory.create()
# Spanish
#fake = Factory.create('es_ES')
# Reload tables
db.drop_all()
db.create_all()
# Make 100 fake contacts

for num in range(100):
    auditory = fake.auditory()
    surname = fake.surname()
    date = fake.date()
    time = fake.time()
    # Save in database
    mi_contacto = Contact(auditory=auditory, surname=surname, date=date, time=time)
    db.session.add(mi_contacto)

db.session.commit()
