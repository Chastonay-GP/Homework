# Write a small script that :
# Asks the user for its name
# Asks the user for its age
# Calculates the age corresponding to the next tenth
# Tells the user, using his name, how many years remain before the next decade… (ex: “Luc, in 4 years you’ll be 50.”)
# asks the user for its gender
# if the user is a female aged more than 18, add a “Mrs.” before her name.
# if the user is a male aged more than 18, add a “Mr.” before his name.

name = input("What is your name?")
print("Hi, {}. Nice to meet you! :D".format(name))

age = int(input('How old are you?'))

next_tenth = ((age + 10) // 10 * 10)

age_dif = next_tenth - age

print("Wow! {}, in {} year(s) you'll be {}!".format(name,age_dif,next_tenth))

gender = input("Are you male of female?")

if gender in ["male", "Male"] and (age > 18):
    print("Mr. {}".format(name))
elif gender in ["female", "Female"] and (age > 18):
    print("Mrs. {}".format(name))
else:
    print(name)