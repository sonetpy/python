age = int(input("What is your current age? "))
max_age = 90
life_to_live = (max_age - age)
total_days = life_to_live * 365
total_weeks = total_days / 7
print("You have {} years, {} weeks and {} days remaining".format(life_to_live,total_weeks,total_days))
