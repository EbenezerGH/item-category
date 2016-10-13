from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Items

engine = create_engine('sqlite:///categoryitems.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



#Item for Soccer
category1 = Category(name = "Futbol")

session.add(category1)
session.commit()

menuItem1 = Items(name = "Ball", description = " Round object that is hit or thrown or kicked in games.", sport = "Futbol", category = category1)

session.add(menuItem1)
session.commit()


menuItem2 = Items(name = "Cleats", description = "One of a number of projecting pieces of metal, rubber, or other material on the sole of a shoe, designed to prevent the wearer from losing their footing.", sport = "Futbol", category = category1)

session.add(menuItem2)
session.commit()

menuItem3 = Items(name = "Water Bottles", description = "Source of hydration for those long 90 minute games.", sport = "Futbol", category = category1)

session.add(menuItem3)
session.commit()


#Item for Basketball
category2 = Category(name = "Basketball")

session.add(category2)
session.commit()


menuItem1 = Items(name = "Basketball", description = "Spherical object used to score points in the other team's hoop.", sport = "Basketball", category = category2)

session.add(menuItem1)
session.commit()

menuItem2 = Items(name = "Sneakers", description = "Shoes needed to be efficient at the game", sport = "Basketball", category = category2)

session.add(menuItem2)
session.commit()

menuItem3 = Items(name = "Uniform", description = "Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ", sport = "Basketball", category = category2)

session.add(menuItem3)
session.commit()


#Item for Baseball
category1 = Category(name = "Baseball")

session.add(category1)
session.commit()


menuItem1 = Items(name = "Bat", description = "Used by the batter to hit the ball.", sport = "Basketball", category = category1)

session.add(menuItem1)
session.commit()

menuItem2 = Items(name = "Baseball Mitten", description = "Used to soften the collision between the baseball and your hand.", sport = "Basketball", category = category1)

session.add(menuItem2)
session.commit()

menuItem3 = Items(name = "Gyoza", description = "The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner... You might get hungry.", sport = "Basketball", category = category1)

session.add(menuItem3)
session.commit()


#Item for Frisbee
category1 = Category(name = "Frisbee")

session.add(category1)
session.commit()


#Item for Snowboarding
category1 = Category(name = "Snowboarding")

session.add(category1)
session.commit()


#Item for Rock Climbing
category1 = Category(name = "Rock Climbing")

session.add(category1)
session.commit()


#Item for Foosball
category1 = Category(name = "Foosball")

session.add(category1)
session.commit()


#Item for Skating
category1 = Category(name = "Skating")

session.add(category1)
session.commit()


#Item for Hockey
category1 = Category(name = "Hockey")

session.add(category1)
session.commit()


print "Added Items to the Catalog!"