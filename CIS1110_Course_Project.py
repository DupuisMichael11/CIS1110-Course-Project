import sys
import time
def slowprint(string):
    for char in range(len(string)):
        print(string[char],end="")
        time.sleep(1./50)

#Introduction
slowprint(f"Why hello there, and welcome to a wonderous story about a charasmatic little bard.  ")
slowprint(f"\nBefore we begin I need your help in telling the story by answering a few questions for me.  ")
slowprint(f"\nAfter typing your answer please make sure to press enter to move onto the next question.\n  ")
input(f"\nPress the enter key to continue...  ")

#5 Questions for inputs used in story
bardName = input("\nWhats the bards name:  ")
while len(bardName) == 0:
    bardName = input(f"Please enter the bards name:  ")
instrument = input("What instrument does the bard play:  ")
while len(instrument) == 0:
    instrument = input(f"Please enter an instrument:  ")
numberOfBirds = input("What is your favorite number:  ")
while len(numberOfBirds) == 0:
    numberOfBirds = input(f"Please enter a number:  ")
forestName = input("Choose a noun:  ")
while len(forestName) == 0:
    forestName = input(f"Please enter a person, place, or thing:  ")
pondName = input("Choose a second noun:  ")
while len(pondName) == 0:
    pondName = input(f"Please enter a person, place, or thing:  ")
slowprint("\nThank you for your help! Now let the story begin!\n  ")
input(f"\nPress enter to start the story...\n  ")

#While loop for whole story
keepPlaying = "yes"
while keepPlaying.lower() == "yes":


    #Story Begins
    slowprint(f"\nLong ago there was a bard named {bardName} who lived in {forestName} forest.  ")
    slowprint(f"\n{bardName} loved to take walks through {forestName} forest and play their {instrument} for all the woodland creatures they saw.  ")
    slowprint(f"\n{bardName} would even sing and dance with the woodland creatures from time to time.  ")
    slowprint(f"\nOne day {bardName} was walking through the forest when they heard the most beautiful sound.  ")
    slowprint(f"\nThere were {numberOfBirds} birds flitting from tree to tree, singing merrily.")
    slowprint(f"\n{bardName} pulled out their {instrument} and started playing a jaunty tune.\n ")

    #Decision 1
    singAlong = input(f"\nShould {bardName} sing along too? Please type yes or no:  ")
    if singAlong.lower() == "yes":
        slowprint(f"\nWhile {bardName} played along with the birds they got excited and sang even louder.   ")
        slowprint(f"\nThen {bardName} decided to sing along, while quite out of tune.\n ")
        slowprint(f"\n'Birds, birds with wings so grand,  ")
        slowprint(f"\nLet's sing and dance across the land.  ")
        slowprint(f"\nThe sky so wide, you fly so high.  ")
        slowprint(f"\nWill you come land, upon my hand.'\n  ")
        slowprint(f"\nAs soon as the bard finished their out of tune song, the birds flew down to land upon {bardName}'s hand...")
        slowprint(f"\nSQUAWK!!! {bardName} singing had been so bad they started attacking!")
        slowprint(f"\n{bardName} ran, and ran, deep into {forestName} forest, all scratched and bruised, until the nasty birds flew away.\n")
        input(f"\nPress enter to continue the story...  ")
    else:
        slowprint(f"\nAs {bardName} kept playing the merry tune, the birds flew about excitedly, chirpping and singing too their hearts content.")
        slowprint(f"\nThe birds flew down and landed upon {bardName}'s shoulders and {instrument} chirping along with the tune and hopping all about.  ")
        slowprint(f"\nSoon {bardName} moved deeper into the forest while playing the lovely tune.")
        slowprint(f"\nAnd the birds followed singing and dancing while they flew about. ")
        slowprint(f"\nMuch later they finally left {bardName} when the sun went down, flying away happily, back to their homes.\n  ")
        input(f"\nPress enter to continue the story...  ")

    #Second Decision intro
    slowprint(f"\nAs {bardName} travled deeper into {forestName} forest it slowly became darker and darker.  ")
    slowprint(f"\nLuckily {bardName} came across a pond with a sign reading. \n'{pondName} Pond, DON'T FEED THE BEARS!'")
    slowprint(f"\n{bardName} was tired after their adventure with the birds and decided to sit down to take a rest.  ")
    slowprint(f"\nWhile {bardName} was resting he noticed a bear walk up to the pond to take a drink.  ")
    slowprint(f"\nAfter drinking his fill, the bear sat down on his bum, and started to yawn.\n  ")

    #Decision 2
    singLullaby = input(f"\nShould {bardName} start singing a lullaby to the bear? Please type yes or no:  ")
    if singLullaby. lower() == "yes":
        slowprint(f"\nSlowly {bardName} started to sing a sweet lullaby to the bear.  ")
        slowprint(f"\n'Bear, bear don't you fret, ")
        slowprint(f"\nThis is a lullaby you won't forget.")
        slowprint(f"\nSleep now, and don't eat me.  ")
        slowprint(f"\nOr else your tummy will scream ouchie!  ")
        slowprint(f"\nI don't taste good, no I don't.  ")
        slowprint(f"\nYour tummy won't thank you, no it won't...'\n  ")
        slowprint(f"\nAs soon as the bard started their tune the bear covered its ears with its paws and howled in anger!  ")
        slowprint(f"\nSo engrossed in his terrible singing, {bardName} didn't realize the bear running straight for them.  ")
        slowprint(f"\nWhen the bear got near, the bards eyes opened wide with fright!  ")
        slowprint(f"\nSPLASH! went the bard into the pond! And away {bardName} swam as fast as they could.  ")
        slowprint(f"\nAs soon as {bardName} got to the other side they got up and ran away soaking wet. \nSQUISH, SQUISH, SQUISH.\n  ")
        input(f"\nPress enter to continue the story...  ")
    else:
        slowprint(f"\nAfraid their singing would startle the bear, {bardName} instead took out their {instrument} and started playing a soft lullaby.  ")
        slowprint(f"\nThe bear swayed back and forth to the sweet music.  ")
        slowprint(f"\nAnd as soon as {bardName} thought the bear would never sleep.  ")
        slowprint(f"\nIt finally laid its head down to rest and started snoring loudly.\n  ")
        input(f"\nPress enter to continue the story...  ")

    #Alternate Endings
    if singAlong. lower() == "yes" and singLullaby. lower() == "yes":
        slowprint(f"\n{bardName} soaking wet, beat and bruised, decided to head home to his quiet cottage in {forestName} forest.  ")
        slowprint(f"\nAs soon as he got home he threw his {instrument} in the trash. 'I'll never sing again!' they said.  ")
        slowprint(f"\nAnd because {bardName} never sang again, all the animals in the forest lived happily ever after.\n   ")
    elif singAlong. lower() == "no" and singLullaby. lower() == "no":
        slowprint(f"\n{bardName} happily strode home to their cottage in {forestName} forest. Playing their {instrument} all the way.  ")
        slowprint(f"\nAnd they say to this day whenever one enters {forestName} forest, ")
        slowprint(f"\nYou can still hear the sweet melody of {bardName}'s {instrument} playing through the forest.\n  ")
    else:
        slowprint(f"\n{bardName} went home confused, they couldn't tell why some animals were so mean and other so sweet.  ")
        slowprint(f"\n{bardName} continued to be confused for the rest of their days spent in the forest.  ")
        slowprint(f"\nNever figuring out that animals loved {bardName}'s music,  ")
        slowprint(f"\nbut could not stand their awful singing.  ")
        slowprint(f"\nTo this day {bardName} still sometimes sings to the woodland creatures,  ")
        slowprint(f"\nand their angry growls and chirps can still be heard throughout the forest, ")
        slowprint(f"as {bardName} runs from the animals that hear {bardName}'s terrible singing voice.\n  ")

    keepPlaying = input(f"\nThank you for playing. Would you like to play again? Pleast type yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
            keepPlaying = input(f"Please type yes or no:  ")





