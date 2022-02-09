import random

class hangman:
	def __init__(self,Start):
		Start = true


	def guesses(wordlist):
		val = input("Enter your one letter guess: ")

		while val.isalpha() == False or len(val) > 1:
			val = input("Please enter one letter as a guess: ") 






words = ["Hello", "Hangman", "Python", "Programming", "One Piece"]

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# for x in alphabet:
#	if x.isalpha():
#		print(x + " is a letter")

target_word = (words[(random.randrange(1,len(words)))])

hangman.guesses(target_word)



