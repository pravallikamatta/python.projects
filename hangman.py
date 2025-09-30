import random
lives=6
word=random.choice(['python','java','kotlin','javascript'])
print("Random word selected by computer:",word)
word_length=len(word)
display=[]
for i in range(word_length):
    display+="_"
print(display)
game_ovr=False
while not game_ovr:
    guesses=input("Enter a letter:").lower()
    for position in range(len(word)):
        letter=word[position]
        if letter==guesses:
            display[position]=guesses
    print(display)

    if guesses not in word:
     lives-=1
     if lives == 0:
        game_ovr=True
        print("you lose")
    if '_' not in display:
        game_ovr=True
        print("you win")       































