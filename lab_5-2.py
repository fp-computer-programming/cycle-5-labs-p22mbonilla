# Author MB 10/27/2021

first = input("the first word: ")
second = input("the second word: ")

if first < second:
    print(first + " " + "comes before" + " " + second)
elif first > second:
    print(first + " " + "comes after" + " " + second)
else:
    print("words are the same.")
