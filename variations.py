#!/usr/bin/python 3.7

# python implemmentation here

message = input("Enter your message: ")
print("Lowercase: ", message.lower())
print("Uppercase: ", message.upper())
print("CAPITALZIED: ", message.capitalize())
print("Title Case: ", message.title())

# use split method to seperate on space
words = message.split()
print("Words: ", words)

#sort list ( words ) and choose
sorted_words= sorted(words)
print("Alphabetic First Word: ", sorted_words[0])
print("Alphabetic Last Word: ", sorted_words[-1])


