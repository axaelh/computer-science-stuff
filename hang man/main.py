import re
#get answer
answer_character = "Hello, hello? Uh, I wanted to record a message for you to help you get settled in on your first night."
answer_character = answer_character.upper()
#store known or unknown letters
answer_guesses = []

for current_answer_character in answer_character:
    if re.search("^[A-Z]$", current_answer_character):
        answer_guesses.append(False)
    else:
        answer_guesses.append(True)
#Logic of playing the game.
guessed_letters = []
num_of_incorrect_guesses = 0

while num_of_incorrect_guesses < 5 and False in answer_guesses:
    print("----------------------------")
    print("Guessed letters: ", end = "")

    for current_guessed_letters in guessed_letters:
        print(f"{current_guessed_letters}" , end = "")
    print()

    print(f"Number of inccorect guesses remaining: {5 - num_of_incorrect_guesses}")

    print()

    for answer_index in range(len(answer_character)):
        if answer_guesses[answer_index]:
            print (answer_character[answer_index], end = "")
        else:
            print("_", end = "")

    print()

    letter = input("Enter a letter: ")

    letter = letter.upper()

    if letter not in guessed_letters and len(letter) == 1 and re.search("^[A-Z]$", letter):
      guessed_letters_insert_index = 0

      for current_guessed_letter in guessed_letters:
        if letter < current_guessed_letter:
          break
        guessed_letters_insert_index += 1
      guessed_letters.insert(guessed_letters_insert_index, letter)
      
      if letter in answer_character:
            for current_answer_index in range(len(answer_character)):
                if letter == answer_character[current_answer_index]:
                    answer_guesses[current_answer_index] = True
      else:
            num_of_incorrect_guesses += 1
# Game is Over. Display whether user won or lost.
if num_of_incorrect_guesses < 5:
    print("Congrats big dog you won :D Have a cookie 🍪")
else:
    print("you lost loser you suck lolz")
print(f"{answer_character} is the answer to the puzzle")
