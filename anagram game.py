import random, time

def main():
    play = True
    totalpoints = 0
    intro()
    while play == True:
        wordlist = wordlistf()
        wordlist_rand = wordlist_randf(wordlist)
        points, undertimelimit, no_skip = game(wordlist, wordlist_rand)
        totalpoints += points
        game_finish(points, undertimelimit, no_skip)
        play = playagain_prompt(play, totalpoints)


def anagram(word):
    letters = []
    for letter in word:
        letters.append(letter)

    letters_rand = []
    for i in range(len(word)):
        rand_index = random.randint(0,len(word)-1-i)
        letters_rand.append(letters[rand_index])
        letters.pop(rand_index)

    anagram = ""
    for letter in letters_rand:
        anagram += letter
    anagram = anagram.upper()
    return anagram

def wordlistf():
    words = ["APPLE", "HOUSE", "BANANA", "FOOD", "GHOST", "MARIO", "WATER", "SMARTPHONE", "COVID", "HELLO", "OMG", "KEYBOARD", "COMPUTER", "ALEXA", "TELEVISION", "DESK"]
    wordlist = []
    original_wordsn = len(words)-1
    for i in range(10):
        rand_index = random.randint(0,original_wordsn-i)
        wordlist.append(words[rand_index])
        words.pop(rand_index)
    return wordlist

def wordlist_randf(wordlist):
    wordlist_rand = []
    for word in wordlist:
        word = anagram(word)
        wordlist_rand.append(word)
    return wordlist_rand
        
def intro():
    print("\n")
    print("Welcome to Mar1oo's Anagram game!")
    print("The rules are quite simple: you will see 10 anagrams of words of varying lenght and difficulty and you have to guess the correct words!")
    print("Every word you get right is 1 point!")
    print("If you want to skip a word, just type \"pass\" and you will move on to the next word.")
    print("\n")
    print("Are you ready? Press enter to start!")
    print("\n")
    entertostart = input()
    return

def game(wordlist, wordlist_rand):
    points = 0
    skipped_words_rand = []
    skipped_words = []
    time_start = time.time()
    undertimelimit = False
    no_skip = True
    for i in range(len(wordlist_rand)):
        print("Word " + str(i+1) + ": " + wordlist_rand[0])
        guess = input()
        while guess.upper() != wordlist[0]:
                if guess != "pass":
                    print("Wrong! Try again!")
                    guess = input()
                else:
                    skipped_words_rand.append(wordlist_rand[0])
                    skipped_words.append(wordlist[0])
                    wordlist_rand.pop(0)
                    wordlist.pop(0)
                    break
        if guess != "pass":
            print("Correct!")
            wordlist_rand.pop(0)
            wordlist.pop(0)
            points += 1
        print("\n")
        time_end = time.time()
        if (time_end - time_start) > 60:
            print("Time's over!")
            print("\n")
            return points, undertimelimit, no_skip
    while len(skipped_words) > 0:
        no_skip = False
        skipped_words_index = 0
        for i in range(len(skipped_words_rand)):
            print("Skipped word: " + skipped_words_rand[skipped_words_index])
            guess = input()
            while guess.upper() != skipped_words[skipped_words_index]:
                if guess != "pass":
                    print("Wrong! Try again!")
                    guess = input()
                else:
                    skipped_words_index += 1
                    break
            if guess != "pass":
                print("Correct!")
                skipped_words_rand.pop(skipped_words_index)
                skipped_words.pop(skipped_words_index)
                points += 1
            print("\n")
            time_end = time.time()
            if (time_end - time_start) > 60:
                print("Time's over!")
                print("\n")
                return points, undertimelimit, no_skip
    print("\n")
    print("Game finished!")
    print("\n")
    undertimelimit = True
    return points, undertimelimit, no_skip

def game_finish(points, undertimelimit, no_skip):
    if undertimelimit == True:
        print("Congratulations! You guessed all 10 words under the time limit and managed to obtain 10 points!")
        if no_skip == True:
            print("You also didn't skip any words! You're the best!")
    elif points >= 8:
        print("Good job! You got " + str(points) + " points.")
    elif points >= 5:
        print("You got " + str(points) + " points. I'm sure you'll do better next time!")
    elif points >= 2:
        print("You got only " + str(points) + "...")
    else:
        print("You got " + str(points) + "... did you even try?")
    return

def playagain_prompt(play, totalpoints):
    print("\n")
    print("Do you want to play again? Your points will save.")
    print("Type \"yes\" or \"no\", then press enter.")
    choice = input()
    while not(choice.lower() in ["yes", "no"]):
        print("Type either \"yes\" or \"no\"!")
        choice = input()
    if choice.lower() == "yes":
        print("Perfect! Press enter when you're ready!")
        input()
    elif choice.lower() == "no":
        play = False
        print("\n")
        print("Ok! Your total score is " + str(totalpoints) + ".")
        print("Thanks for playing my game!")
        print("\n")
    return play

main()
