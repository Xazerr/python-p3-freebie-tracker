from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()
session.commit()

company1 = Company(name="TMobile", founding_year=1995)
company2 = Company(name="EastWestFshns", founding_year=2006)

dev1 = Dev(name="Wangeci")
dev2 = Dev(name="Ochieng")

freebie1 = Freebie(item_name="Hoodies", value=50, company=company1, dev=dev1)
freebie2 = Freebie(item_name="Matchball", value=22, company=company1, dev=dev2)
freebie3 = Freebie(item_name="Prem bag", value=15, company=company2, dev=dev1)

session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])

session.commit()

print("Database seeded successfully.")

companies = session.query(Company).all()
for company in companies:
    print(company)
    for freebie in company.freebies:
        print(f"  Freebie: {freebie.item_name} (Value: ${freebie.value}) given to Dev: {freebie.dev.name}")

devs = session.query(Dev).all()
for dev in devs:
    print(dev)
    for freebie in dev.freebies:
        print(f"  Received freebie: {freebie.item_name} from Company: {freebie.company.name}")
