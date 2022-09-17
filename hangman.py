from random_word import RandomWords
import re


def main():
    chars = generate_word()
    print(checkGuesses(chars))


def generate_word():
    l = 0
    while l < 3 or l > 10:
        try:
            l = int(input("Number of Letters (3-10): "))
        except:
            continue
    r = RandomWords()
    word = None
    while word == None or word.isalpha() == False:
        word = r.get_random_word(
            hasDictionaryDef="true", minLength=l, maxLength=l, minCorpusCount=5000)
    return [*word.upper()]


def guess():
    guess = ""
    while len(guess) != 1:
        guess = input("Enter a Letter: ").upper()
    return guess


def checkGuesses(chars):
    hint = []
    letters = []
    stage = 1
    guesses = 0
    for i in range(len(chars)):
        hint.append("_ ")
    while guesses < 7:
        letter = guess()
        letters.append(letter)
        if letter not in chars:
            guesses += 1
            stage += 1
        else:
            indices = [i.start() for i in re.finditer(letter, "".join(chars))]
            for i in indices:
                hint[i] = letter
        print(draw_hangman(stage, " ".join(hint), ", ".join(set(letters))))
        if "".join(hint) == "".join(chars):
            break
    return win_or_lose(guesses, stage, chars)


def win_or_lose(guesses, stage, chars):
    if stage == 8:
        return """You Lose! The word was """ + "".join(chars) + "!"
    else:
        return """You Win! You've found """ + "".join(chars) + """ with """ + str(guesses) + """ errors!"""


def draw_hangman(stage, hint, letters):
    if stage == 1:
        return '''
  +---+
  |   |
      |
      |
      |
      |
=========\n''' + hint + """\nYour Guesses So Far: """ + letters
    elif stage == 2:
        return '''
  +---+
  |   |
  O   |
      |
      |
      |
=========\n''' + hint + """\nYour Guesses So Far: """ + letters
    elif stage == 3:
        return '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========\n''' + hint + """\nYour Guesses So Far: """ + letters
    elif stage == 4:
        return '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========\n''' + hint + """\nYour Guesses So Far: """ + letters
    elif stage == 5:
        return '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========\n''' + hint + """\nYour Guesses So Far: """ + letters
    elif stage == 6:
        return '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========\n''' + hint + """\nYour Guesses So Far: """ + letters
    elif stage == 7:
        return '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\n''' + hint + """\nYour Guesses So Far: """ + letters
    elif stage == 8:
        return '''
  +---+
  |   |
 ​​​​​💀   |
 /|\  |
 / \  |
      |
=========\n''' + letters


if __name__ == "__main__":
    main()
