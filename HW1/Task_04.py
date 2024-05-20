# is String palindrome

word = input('Enter a word: ')
revWord = ""

for i in range(len(word) - 1, -1, -1):
    revWord += word[i]

print(revWord)

if(revWord == word):
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
