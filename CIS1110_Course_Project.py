#Introduction
print(f"\nWhy hello there, and welcome to a wonderous story about a peppy little bard who had quite the adventure traveling through the forest.  ")
print(f"\nBut before we begin I need your help in telling the story by answering a few questions for me.  ")
print(f"\nAfter typing your answer please make sure to press enter to move onto the next question.  ")
input(f"\nPress the enter key to continue...  ")

#5 Questions for inputs used in story
bardName = input("What is the bards name:  ")
instrument = input("What instrument does the bard play:  ")
numberOfBirds = input("What is your favorite number:  ")
forestName = input("Choose a noun:  ")
pondName = input("Choose a second noun:  ")
print("\nThank you for your help! Now let the story begin!  ")

#Story Begins
print(f"\nLong ago there was a bard named {bardName} who lived in a forest called {forestName}.  ")
print(f"{bardName} loved to take walks through {forestName} forest and play their {instrument} for any woodland creatures they ran into.  ")
print(f"{bardName} would even sing and dance with the woodland creatures sometimes.  ")
print(f"Oneday {bardName} was walking through the forest when he heard the most beautiful sound.  ")
print(f"There were {numberOfBirds} flitting through the trees singing merrily")

#Decision 1
singAlong = input(f"/n {bardName} pulled out their {instrument} and started playing a jaunty tune. Should {bardName} sing along too? Type yes or no:  ")
if singAlong.lower() == "yes":
    print(f"While {bardName} played along with the birds they got excited and chirped even louder.   ")
    print(f"Then {bardName} sang along with the birds quite out of tune. Birds, birds with wings so grand, Let's sing and laugh across the land. The sky so wide, you fly so high. Will you land upon my hand."  )
    print(f"As soon as the bard finished their out of tune song, the birds obliged and flew down to land upon {bardName}'s hand...")
    print(f"And immediately started attacking them!!!")
    print(f"{bardName} ran and ran deep into {forestName} forest until he got away.")
else:
    print(f"As the {bardName} kept playing the merry tune, the birds flew about excitedly chirping  and singing too their hearts content.  ")
    print(f"The birds even flew down and landed upon {bardName}'s shoulders and {instrument} chirping along with the tune and hopping all about.  ")
    print(f"The birds stayed with {bardName} deep into the forest singing and dancing in the air late into the evening.  ")

#Decision 2


