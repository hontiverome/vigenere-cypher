# ACTIVITY2 NO3 PSEUDOCODE WITH GIT COMMITS
# State variables
Message=str(input("Enter the message\n:"))
KeyWord=str(input("Enter the keyword\n:"))
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
# Print the output
print(CipherValue)
# PRODUCE THE CIPHERTEXT OF THE FOLLOWING:
# Message: THISISTHELASTTASKHOORDAY
# Key: KNIGHTS

# HONTIVEROS, JEROME ANDREI O.   
# BSCPE 1-5