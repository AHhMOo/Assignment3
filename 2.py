#task1
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#task2

additional_facilities =  "audio system" if venue =="larg hall" else "projector"
print(additional_facilities)

#task3
food = str(input("would you like vegetarian food(yes,no): "))
recommend = "Veggie Delight Caterers" if food=="yes" else  "Gourmet Meals Caterers"
print(recommend)


