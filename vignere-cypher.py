import pyfiglet, termcolor, time
# ACTIVITY2 NO3 PSEUDOCODE WITH GIT COMMITS
# State variables
Message=""
KeyWord=""
def MainCode(Message, KeyWord):
    CipherText=""
    # Makes the conversion on each position for the keyword
    KeyValues=[ord(j)-65 for j in KeyWord]
    LetterPosition=0
    # Convert current positional character to a corresponding letter value based on the Message (0-25)
    for j in Message:
        LetterValue=ord(j) - 65   
        # Modulo 26 to have a range value of 0-25 only
        CipherValue=(LetterValue+KeyValues[LetterPosition])%26
        # Convert the value back to a letter
        CipherCharacter=chr(CipherValue+65)
        # Add/push the cipher letter to the final cipher text
        CipherText+=CipherCharacter
        # Add current position to the keyword, (will serve as the end when the code reaches the last letter)
        LetterPosition=(LetterPosition+1)%len(KeyWord)
    return CipherText

# Defined functions that give design (animations, font, and color)
def ShowResults():
    showResults = 'Here is your Cipher text:\n'
    for i in range(len(showResults)):
        print(termcolor.colored(showResults[i], 'green'), end='', flush=True)
        time.sleep(0.1)
def CreatedCypherText():
    Seperate= ' '.join(CipherText)
    print(termcolor.colored(pyfiglet.figlet_format(Seperate, font="alligator", justify="center", width=220), 'red'))
    print("or:\n"	)
    for i in range(len(Seperate)):
        print(termcolor.colored(f"{Seperate[i]}", 'red'), end='', flush=True)
        time.sleep(0.09)

# Print the output
Message=str(input("Enter the message:\n"))
KeyWord=str(input("Enter the keyword:\n"))
CipherText=MainCode(Message, KeyWord)
ShowResults()
CreatedCypherText()

# PRODUCE THE CIPHERTEXT OF THE FOLLOWING:
# Message: THISISTHELASTTASKHOORDAY
# Key: KNIGHTS

# HONTIVEROS, JEROME ANDREI O.   
# BSCPE 1-5