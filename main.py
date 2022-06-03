from random import randint


def displayIntro():
    fileName = "hangman-ascii.txt"
    file = open(fileName, "r")
    for iterator in range(0, 23):
        print(file.readline(), end='')
    file.close()


def displayEnd(result):
    fileName = "hangman-ascii.txt"
    file = open(fileName, "r")
    content = file.readlines()
    if result == True:
        for i in range(190, 203):
            print(content[i], end="")
    elif result == False:
        for i in range(99, 112):
            print(content[i], end="")
    file.close()


def displayHangman(state):
    fileName = "hangman-ascii.txt"
    file = open(fileName, "r")
    content = file.readlines()
    if state == 5:
        for i in range(24, 33):
            print(content[i], end="")
    elif state == 4:
        for i in range(37, 46):
            print(content[i], end="")
    elif state == 3:
        for i in range(50, 59):
            print(content[i], end="")
    elif state == 2:
        for i in range(63, 72):
            print(content[i], end="")
    elif state == 1:
        for i in range(76, 85):
            print(content[i], end="")
    elif state == 0:
        for i in range(89, 98):
            print(content[i], end="")


def getWord():
    fileName = "hangman-words.txt"
    file = open(fileName, "r")
    content = file.readlines()
    rand = randint(1, len(content))
    file.close()
    return content[rand]


def valid(c):
    if len(c) == 1 and c.isalpha() and c.islower():
        return True
    else:
        return False


def play():
    word = getWord()
    dashes = "_" * (len(word)-1)
    state = 5
    forSomeReasonStringComparisonDoesNotWorkSoICreatedThis = 0
    while state > 0:
        displayHangman(state)
        print("Guess the word: " + dashes)
        attempt = input("Enter the letter: \n")
        while valid(attempt) == False:
            attempt = input("Enter the letter: \n")
        actual = False
        for letterIndex, letter in enumerate(word):
            if letter == attempt:
                actual = True
                index = letterIndex
                for dashIndex in range(0, len(dashes)):
                    if dashIndex == index:
                        temp = list(dashes)
                        temp[index] = attempt
                        dashes = "".join(temp)
                        forSomeReasonStringComparisonDoesNotWorkSoICreatedThis = forSomeReasonStringComparisonDoesNotWorkSoICreatedThis + 1
        if actual == False:
            state = state - 1
        if forSomeReasonStringComparisonDoesNotWorkSoICreatedThis == len(word)-1:
            print("Hidden word was: "+word)
            return True
    if state == 0:
        displayHangman(state)
        print("Hidden word was: " + word)
        return False

def hangman():
    Continue = "yes"
    while Continue == "yes":
        displayIntro()
        result = play()
        displayEnd(result)
        print("Do you want to play again? (yes/no)\n")
        Continue = input()
        if Continue == "no":
            break

if __name__ == "__main__":
    hangman()
