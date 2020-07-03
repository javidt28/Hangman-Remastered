'''This imports the random python module'''
import random
import pathlib


WORDS1 = ["cool", "banjo", "crypt", "fjord", "gazebo", "pixel", "javid", "facebook", "twitter"]

WORDS2 = ["google", "python", "java", "matrix", "arrays", "function", "class", "array"]

WORDS3 = ["howard", "bison", "university"]

WORDS = WORDS1 + WORDS2 + WORDS3
leader = {}
score = 0

IS_FIRST_TIME = True
LETTERS_AVAIL = "abcdefghijklmnopqrstuvwxyz"
count = 0


def welcome():
    """ This function is going to welcome the user and give them the game instructions. """
    print(
        "========================================================================="
    )
    print("Welcome to GameOn Hangman ® ")
    print("Guess letters one at a time to solve the word puzzle.")
    print("Type a letter to guess it. Each time you solve a")
    print("word puzzle ten (10) points will be added to your score.")
    print("You will have only eight (8) attempts of guessing the ")
    print("wrong letter before the game termiates and the man is hung.")
    print("Each time the game is ran a new word or phrase will be generated.")
    print("The image below is what you'll see after eight (8) wrong guesses. ")
    print('''
                             _________
                            |         |
                            |         💀
                            |        /|\\
                            |         |
                            |        / \\
                            |
                              ========== ''')
    print(
        "=========================================================================")
    

    return "GameOn"

def replace_dashes(top_secret, dashes_pos, last_guess):
    ''' This function weill update the dashes (-) with the user guess if the guess is correct'''

    output = ""

    for word, i in enumerate(top_secret):
        if top_secret[word] == last_guess:
            output = output + last_guess
        else:
            output = output + dashes_pos[word]
    return output

def draw_hangman(attempts):
    ''' This function is where the hangman images are drawn '''
    hangman = [
        '''
   __________
  |         |
  |
  |
  |
  |
   ========== ''', '''
   __________
  |          |
  |          🙁
  |
  |
  |
   ========== ''', '''
  
   __________
  |         |
  |         😖
  |         |
  |
  |
   ========== ''', '''
  
   __________
  |         |
  |         😫
  |         |\\
  |
  |
   ========== ''', '''

   __________
  |         |
  |         😨
  |        /|\\
  |
  |
   ========== ''', '''

   __________
  |         |
  |         😰
  |        /|\\
  |         |
  |
   ========== ''', '''

   __________
  |         |
  |         😱
  |        /|\\
  |         |\\
  |
   ========== ''', '''
   __________
  |         |
  |         💀
  |        /|\\
  |         |
  |        / \\
  |
   ========== '''] 
  
    return hangman[attempts]

def input_processing(guess):
  ''' Convert user guess to lowercase'''
  user_guess = guess.lower()
  return user_guess

def play_a_turn():
    ''' This function is responsible for looping the game if the user wants to play again'''
    print()
    print("Please type yes to play again else type no to end.")
    keep_playing = input("Would you like to play again? ").lower()
    print()
    if keep_playing in "yes":
        main_game()
        return True
    else:
        print("Thanks for playing!")
        with open("leaderboard.txt") as file0:
          with open("output.txt", "a") as file1:
            for line in file0:
              file1.write(line)
        display_leader()
        return False

def display_leader():
  print()
  print("======== LEADERBOARD ========")
  with open("output.txt", "r", encoding="utf-8") as file:
    for line in file:
      print(line.strip())
  return False

def leaderboard():
  file = pathlib.Path("leaderboard.txt")
  if file.exists():
    pass
  else:
    file_open = open("leaderboard.txt", "x")
    file_open.write("Name" + "      " " Games Won " + "   " + " Points\n")
    file_open.close()
    file_open1 = open("output.txt","x")
    file_open1.write("Name" + "      " " Games Won " + "   " + " Points\n")
    file_open1.close()

  print()

  user_name = input("Please enter your name: ")

  if user_name != 'end':
    if user_name not in leader:
      leader[user_name] = score
    else:
      leader[user_name] += score + 1
  
  for key in leader:
    f = open("leaderboard.txt", "w")
    f.write("\n" + str(key) + "        " + str(leader[key]) + "            "+str((leader[key] * 10)))
    f.close()
   

  return " "

def main_game():
  ''' This is the where all the helper functions will be combiled to run the game of Hangman '''
  
  global IS_FIRST_TIME
  if IS_FIRST_TIME:
    print(welcome())
    print(leaderboard())
    IS_FIRST_TIME = False

  random_word = random.randint(0, 19)
  random_secret_word = WORDS[random_word]

  dashes = "_" * len(WORDS[random_word])
  attempts = 7
  correct_guess = 0
  wrong_guess = 0
  score = 0

  print("This word has", len(random_secret_word), "letters!")
  print("You have these letters available ", LETTERS_AVAIL)

  while attempts > 0 and dashes != (WORDS[random_word]):
      print("\n", dashes)
      print()
      user_guess = input_processing(guess=input("Please guess a letter: "))
      print()

      if len(user_guess) != 1:
          print()
          print("Your Guess can only be one Character! ")
          print()

      elif user_guess in random_secret_word:
          correct_guess += 1
          dashes = replace_dashes(random_secret_word, dashes, user_guess)
          print("You have", correct_guess, "correct guesses!")

      elif user_guess not in random_secret_word:
          attempts -= 1
          wrong_guess += 1
          print("You have", attempts, "attempts left!")
          print(draw_hangman(wrong_guess))

  if attempts == 0:
      print("You exhausted all your attempts")
      print("You lost!", "the word you failed to guess was:",
            random_secret_word)
  if dashes == (WORDS[random_word]):
      print("You guessed the word", random_secret_word, "correctly!")
      score += 1
      print("You won bragging rights!")
      leaderboard()
      play_a_turn()

  elif dashes != (WORDS[random_word]):
      print("You have no bragging rights!")
      play_a_turn()
      print()
      return "Bye!"
  print()
  return "Have a nice day!"


print(main_game())
