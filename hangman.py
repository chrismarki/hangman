import random


class hangman:
	def __init__(self,Start):
		Start = true

	def guesses(target_word,wrongguess_count, active_wordbank, blank_word):
		val = input("Enter your one letter guess: ").lower()
		print(val)
		#Guess error handling
		while val.isalpha() == False or len(val) > 1 or val not in active_wordbank:
			val = input("Please enter one letter as a guess and not repeat any guesses: ").lower()


		#If guess is not in the target word, build the noose and display used letters
		if val not in target_word: 

			print("Not in the target word. Try Again")
			active_wordbank.remove(val)
			wrongguess_count = wrongguess_count + 1
			
			hangman.build_noose(wrongguess_count, active_wordbank)
			hangman.guesses(target_word, wrongguess_count,active_wordbank, blank_word)

		#if guess is true then print the list of letters guessed
		elif val in target_word:

			del_target = list(blank_word)
			indx = 0

			for x in target_word:
				if x == val:
					del_target[indx] = val
				indx = indx + 1

			word_vic = "".join(del_target)
			print("Target Word:", del_target)
			print(alphabet)

			active_wordbank.remove(val)


			if word_vic.find("_") == -1:
				print("You WON!!!!!")
				exit()


			hangman.guesses(target_word, wrongguess_count,active_wordbank, del_target)
	

	#build the noose depend on wrong guesses count
	def build_noose(wrongguess_count, active_wordbank):
		if wrongguess_count == 1:
			print("Remaining leters:", active_wordbank)
			print("______")
		if wrongguess_count == 2:
			print("Remaining leters:", active_wordbank)
			print("\n|\n|\n|\n|\n|______")
		if wrongguess_count == 3:
			print("Remaining leters:", active_wordbank)
			print("_____\n|\n|\n|\n|\n|______")
		if wrongguess_count == 4:
			print("Remaining leters:", active_wordbank)
			print("_____\n|  |\n|\n|\n|\n|______")
		if wrongguess_count == 5:
			print("Remaining leters:", active_wordbank)
			print("_____\n|  |\n|  o\n|\n|\n|______")
		if wrongguess_count == 6:
			print("Remaining leters:", active_wordbank)
			print("_____\n|  |\n|  o\n|  |\n|\n|______")
		if wrongguess_count == 7:
			print("Remaining leters:", active_wordbank)
			print("_____\n|  |\n|  o\n| -|\n|\n|______")
		if wrongguess_count == 8:
			print("Remaining leters:", active_wordbank)
			print("_____\n|  |\n|  o\n| -|-\n|\n|______")
		if wrongguess_count == 9:
			print("Remaining leters:", active_wordbank)
			print("_____\n|  |\n|  o\n| -|-\n| / \n|______")
		if wrongguess_count == 10:
			print("Remaining leters:", active_wordbank)
			print("_____\n|  |\n|  o\n| -|-\n| / \\\n|______")
			print("Game Ogre")
			exit()


words = ["hello", "hangman", "python", "programming", "onepiece","luffy","alberti","steven","wedding","valentinesday","wordle","hydaelyn","reaper","zodiark"]

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

target_word = (words[(random.randrange(1,len(words)))])

#target_word = "hello"

#Print Blank word 
blank_word = "_"*len(target_word)

print("Target Word:", list(blank_word))

hangman.guesses(target_word, 0, alphabet, blank_word)


