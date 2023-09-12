# Задание №1
word = str(input())
reverse_word = word[::-1]

if word == reverse_word:
    print("yes")
else:
    print("no")


# Задание №2
my_string=str(input())
spaces=' '.join(my_string.split())

print(spaces)