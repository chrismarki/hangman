import random

class hangman:
	def __init__(self,Start):
		Start = true

	def guesses(target_word,wrongguess_count, wrongguess_list):
		val = input("Enter your one letter guess: ")

		#Guess error handling
		while val.isalpha() == False or len(val) > 1:
			val = input("Please enter one letter as a guess: ") 

		#If guess is not in the target word, build the noose and display used letters
		if val not in target_word: 
			print("Not in the target word. Try Again")

			wrongguess_list.append(val)
			wrongguess_count = wrongguess_count + 1
			print(wrongguess_count)

			hangman.build_noose(wrongguess_count, wrongguess_list)
			hangman.guesses(target_word, wrongguess_count,wrongguess_list)

		#if guess is true then print the list of letters guessed
		elif val in target_word:
			print("Hey, you got a letter. Try again")
			alphabet.remove(val)
			print(alphabet)
			hangman.guesses(target_word, wrongguess_count,wrongguess_list)

	def build_noose(wrongguess_count, wrongguess_list):
		if wrongguess_count == 1:
			print(wrongguess_list)
			print("______")
		if wrongguess_count == 2:
			print(wrongguess_list)
			print("\n|\n|\n|\n|\n|______")
		if wrongguess_count == 3:
			print(wrongguess_list)
			print("_____\n|\n|\n|\n|\n|______")
		if wrongguess_count == 4:
			print(wrongguess_list)
			print("_____\n|  |\n|\n|\n|\n|______")
		if wrongguess_count == 5:
			print(wrongguess_list)
			print("_____\n|  |\n|  o\n|\n|\n|______")
		if wrongguess_count == 6:
			print(wrongguess_list)
			print("_____\n|  |\n|  o\n|  |\n|\n|______")
		if wrongguess_count == 7:
			print(wrongguess_list)
			print("_____\n|  |\n|  o\n| -|\n|\n|______")
		if wrongguess_count == 8:
			print(wrongguess_list)
			print("_____\n|  |\n|  o\n| -|-\n|\n|______")
		if wrongguess_count == 9:
			print(wrongguess_list)
			print("_____\n|  |\n|  o\n| -|-\n| / \n|______")
		if wrongguess_count == 10:
			print(wrongguess_list)
			print("_____\n|  |\n|  o\n| -|-\n| / \\\n|______")
			print("Game Ogre")

words = ["Hello", "Hangman", "Python", "Programming", "OnePiece"]

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

target_word = (words[(random.randrange(1,len(words)))])

target_word = "Hello"
hangman.guesses(target_word, 0, [])


