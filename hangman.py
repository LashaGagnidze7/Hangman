import random

def wordSaver():
    word = open('word', 'r')
    script = word.read()
    word.close()
    return script

def displayIntro():
    text = open('Beginning', 'r')
    beginnigText = text.read()
    text.close()
    print(beginnigText)


def displayEnd(result):
    print('Hidden word was: ' + wordSaver())
    if result:
        text = open('Winner', 'r')
        winnerText = text.read()
        text.close()
        print(winnerText)
    else:
        text = open('Loser', 'r')
        losingText = text.read()
        text.close()
        print(losingText)


def displayHangman(state):
    lives5 = open('position1', 'r')
    lives4 = open('position2', 'r')
    lives3 = open('position3', 'r')
    lives2 = open('position4', 'r')
    lives1 = open('position5', 'r')
    died = open('position6', 'r')
    displayer = {
        1: lives5.read(),
        2: lives4.read(),
        3: lives3.read(),
        4: lives2.read(),
        5: lives1.read(),
        6: died.read(),

    }
    lives5.close()
    lives4.close()
    lives3.close()
    lives2.close()
    lives1.close()
    died.close()
    print(displayer.get(state))


def getWord():
    words = open('hangman-words.txt', 'r')
    wordsList = words.readlines()
    words.close()
    word = random.choice(wordsList).strip()
    file = open('word', 'w')
    file.write(word)
    file.close()
    return word


def valid(c):
    if c in wordSaver() and c.islower():
        return True
    return False

def play():
    getWord()
    word = wordSaver()
    wordList = list(word)
    conwertedWord = '*'*len(word)
    conwertedWordList = list(conwertedWord)
    newWord = ''
    alreadyUsed = []
    index = 1
    while index <= 6:
        if conwertedWord == word:
            return True
        if index == 6:
            displayHangman(index)
            break
        displayHangman(index)
        print('Guess the word: ' + conwertedWord)
        c = input('Enter the letter: ')
        while c in alreadyUsed:
            c = input('You already inserted that letter, please insert different one: ')
        while not c.islower() or len(c) != 1 or not c.isalpha():
            c = input('Please enter a single English lowercase letter: ')
        alreadyUsed.append(c)
        for letter in wordList:
            if letter == c:
                indexer = wordList.index(letter)
                conwertedWordList.pop(indexer)
                conwertedWordList.insert(indexer, letter)
                wordList.pop(indexer)
                wordList.insert(indexer, '_')
        for char in conwertedWordList:
            newWord += char
        conwertedWord = newWord
        newWord = ''
        if not valid(c):
            index += 1
    return False

def playAgain():
    answer = input('Do you want to play again? (yes/ no)')
    if answer == 'yes':
        return hangman()
    return False

def hangman():
        displayIntro()
        result = play()
        displayEnd(result)
        while True:
            if playAgain() == False:
                break

if __name__ == "__main__":
    hangman()
