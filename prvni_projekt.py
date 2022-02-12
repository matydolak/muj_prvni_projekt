import re
import random

def find_sum(str1):
    # Regular Expression that matches
    # digits in between a string
    return sum(map(int, re.findall('\d+', str1)))

'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

user = ("bob", "ann", "mike", "liz")
password = ("123", "pass123", "password123", "pass123")

uzivatel = str(input("username:"))
heslo = str(input("password:"))
cara = "-" * 35

if uzivatel not in user:
    print("unregistered user, terminating the program..")
    quit()
else:
    index = user.index(uzivatel)
    if heslo != password[index]:
        print("wrong password, terminating the program..")
        quit()

print(cara)
print("Welcome to the app, " + uzivatel)
print("We have 3 texts to be analyzed.")
print(cara)
vyber = input("Enter a number btw. 1 and 3 to select: ")

if not vyber.isdigit():
    print("selection needs to be a number, terminating the program..")
    quit()

elif vyber != '1' and vyber != '2' and vyber != '3':
    print("wrong selection, terminating the program..")
    quit()

index = int(vyber) - 1

#pocet slov
word_list = TEXTS[index].split()
number_of_words = len(word_list)

#počet slov začínajících velkým písmenem
words_start_uppercase = 0
for word in word_list:
    if word[0].isupper():
        words_start_uppercase = words_start_uppercase + 1

#počet slov psaných velkými písmeny
uppercase_words = 0
for word in word_list:
    if word.isupper():
        uppercase_words = uppercase_words + 1

#počet slov psaných malými písmeny
lowercase_words = 0
for word in word_list:
    if word.islower():
        lowercase_words = lowercase_words + 1

#počet čísel (ne cifer),
numeric_words = 0
for word in word_list:
    if word.isnumeric():
        numeric_words = numeric_words + 1

#sumu všech čísel (ne cifer) v textu
count_numbers = find_sum(TEXTS[index])

print(cara)
print("There are " + str(number_of_words) + " words in the selected text.")
print("There are " + str(words_start_uppercase) + " titlecase words.")
print("There are " + str(uppercase_words) + " uppercase words.")
print("There are " + str(lowercase_words)  + " lowercase words.")
print("There are " + str(numeric_words) +  " numeric strings.")
print("The sum of all the numbers is " + str(count_numbers))
print(cara)
print("LEN|  OCCURENCES\t|NR.\t|WORD")
print(cara)

for n in range(0, 12):
    r = random.randint(1, number_of_words)
    if len(word_list[r - 1]) >= 10:
        tab = "\t\t|"
    elif len(word_list[r - 1]) > 5:
        tab = "\t\t\t|"
    else:
        tab = "\t\t\t\t|"
    print(str(n) + "|" + len(word_list[r - 1])*"*" + tab + str(r) + "\t\t" + word_list[r - 1])
