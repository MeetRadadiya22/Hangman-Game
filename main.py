import random
import stages
import wordList

lives = 7
#print logo

print(wordList.logo)


#random_word
chosen_word = random.choice(wordList.word_list)

#print(chosen_word)

#display list with blanks
display = []

for i in range(len(chosen_word)):
  display += "_"
  print(display[i], end=" ")

#variable for end game
end_of_game = False

#looping user-input 
guesslist = []
while end_of_game == False:
  #user input
  guess = input("\n\nGuess the letter: ")
  if guess.isalpha():
    
    if guess not in guesslist:
      if len(guess) == 1:
        guesslist.append(guess)
        #add letters where the user guessed it right
        for position in range(len(chosen_word)):
          letter = chosen_word[position]
          if guess == letter:
            #changes display list element "_" to the guessed letter.
            display[position] = letter
          print(display[position], end=" ")

        

        #checks whether the guessed number is in the chosen_word or not and gives the number of lives 
        if guess not in chosen_word:
          lives -= 1

          if lives == 6:
            print(stages.stages[0]) 
          elif lives == 5:
            print(stages.stages[1])
          elif lives == 4:
            print(stages.stages[2])
          elif lives == 3:
            print(stages.stages[3])
          elif lives == 2:
            print(stages.stages[4])
          elif lives == 1:
            print(stages.stages[5])
          else:
            print(stages.stages[6])

          print(f"\n{lives} lives left")
          if lives == 0:
            end_of_game = True
            print("\nyou loose\n")
            print(f"The word was '{chosen_word}'")


        #checks whether there is any blank "_" in display or not so we can get out of the while(whole main loop).
        if "_" not in display:
          end_of_game = True
          print("\n\nYou win")
      else:
        print("only one character is allowed.")  
    else:
      print(f"Its repeatitive letter, try any other letter than {guess}.") 
      for d in range(len(display)):
        print(display[d], end=" ")   

  else:
      print("invalid input, only alphabets required.")
  


