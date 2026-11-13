# Imports

import time
import os

# Colors

RESET = "\033[0m"
WHITE = "\033[97m"
GRAY = "\033[90m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

BOLD = "\033[1m"
ITALIC = "\033[3m"


# Terminal Functions

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def pause(seconds=1):
    time.sleep(seconds)


def typewrite(text, color=WHITE, style="", speed=0.035):
    print(f"{style}{color}", end="")

    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)

    print(RESET)


# Formatting Functions

def narrator(text, delay=2):
    typewrite(f"*{text}*", GRAY, ITALIC)
    pause(delay)


def dialogue(character, text, color=CYAN, delay=2):
    print()
    typewrite(f"{character}: ", color, BOLD, 0.025) 
    typewrite(f'"{text}"', color, ITALIC, 0.035)
    pause(delay)


def player(text, delay=2):
    typewrite(f"Player: ", GREEN, BOLD, 0.025) 
    typewrite(f'"{text}"', GREEN, BOLD)
    pause(delay)


def thought(text, delay=2):
    typewrite(f"*{text}*", GRAY, ITALIC)
    pause(delay)


def dramatic(text, delay=2):
    typewrite(text, RED, BOLD, 0.08)
    pause(delay)


def highlight(text, delay=2):
    typewrite(text, MAGENTA, BOLD)
    pause(delay)


def scene(title):
    clear()

    print(f"\n{MAGENTA}{BOLD}")
    print("=" * 45)
    print(title.center(45))
    print("=" * 45)
    print(RESET)

    pause(1)

scene("CHAPTER 1")

dramatic(".. Dup..", 1)
dramatic("Dup... Dup....", 2)
dramatic("*Footsteps getting closer...*", 3)

dialogue("???", "Hellooooooo!! Can you hear uss???", delay=4)

narrator("You slowly open your eyes, to the voice calling you.", 4)
narrator("You see a girl with pink hair standing in front of you.", 4)
thought("She's goddamn gorgeous, but what is this outfit of hers?", 4)
thought("Is she going to a cosplay event?", 4)

pause(2)

dialogue("Eris", "Oh there, you are awake.", delay=4)
narrator("You slowly get up.", 4)
dialogue("Eris", "Sir, may I know who you are?", delay=4)
player("Oh sure, I'm Kim Minjoon.", 4)
dialogue("Eris", "King Mwinjon? That's a unique name!", delay=3)
dialogue("Eris", "So, King Mwinjon. Where are you from?", delay=4)

thought("Why is she saying my name so weirdly?", 4)
player("Uh, I'm from Seoul.", 4)
dialogue("Eris", "Seoul? Never heard of that place.", delay=3)
dialogue("Eris", "Which kingdom does it fall in?", delay=4)

player("Kingdom? It's in South Korea.", 4)
dialogue("Eris", "South Korea? Never heard of that place.", delay=3)
dialogue("Eris", "So you're from a distant continent? Probably from the Nova Continent.", delay=4)

thought("Huh? Nova Continent?", 3)
player("Excuse me, but what is this place?", 4)
dialogue("Eris", "This is the Isgard Kingdom on the Lumina Continent.", delay=4)


# Mental Breakdown
narrator("You are in shock. You're apparently from a different continent and a different kingdom.", 4)

thought("WTFFF!! I was just enjoying my fried chicken, and now I'm in a different continent?", 4)
thought("I shouldn't have fallen asleep at that shady store.", 4)


# Girl's Dialogue
dialogue("Eris", "Umm sir, you must be new here, so please head straight down this road.", delay=4)
dialogue("Eris", "You will find the adventurers guild.", delay=4)


# Mental Talks
thought("Huh?? This setting reminds me of that shitty game.", 4)
thought("What was it called again?", 4)
thought("Oh yeah, it was called...", 2)

highlight("HEAVEN'S FIELD", 2)

thought("Ohh, then she must be the tutorial NPC.", 4)
thought("I can't believe that I am inside Heaven's Field!", 4)
thought("Then I must go to the adventurers guild and register as an adventurer.", 4)
thought("...after that, maybe I can find a way to get back to Earth.", 4)

# Back Again
player("Oh sure, I was also heading the same way.", 4)

dialogue("Eris", "Ohh, then please follow me.", delay=4)
narrator("You follow her.", 4)
dialogue("Eris", "Btw, my name is Eris. I work as a guide for tourists here.", delay=4)
player("Thank you, Eris. It was nice meeting with you.", 4)

narrator("You bid her farewell and head inside the adventurers guild.", 4)
narrator("You see a lot of people inside the guild. Some are talking to each other, while others are training their skills.", 4)
narrator("You see a small elf girl at the counter.", 4)

# Inside Adventurers Guild

dialogue(
    "Lilith",
    "Hello there! You seem new here. Welcome to the adventurers guild. "
    "My name's Lilith, and I work as a receptionist here.",
    color=MAGENTA,
    delay=7
)

player("Hello Lilith, my name is Kim. I want to register as an Adventurer", 4)

dialogue(
    "Lilith",
    "Ohh, then please fill out this form and submit it to me.",
    color=MAGENTA,
    delay=4
)

narrator("You fill out the form and submit it to Lilith.", 4)

dialogue(
    "Lilith",
    "Thank you for submitting the form. Now, we will need to check your magic proficiency",
    color=MAGENTA,
    delay=4
)
narrator("Lilith takes out a crystal ball from under the counter.", 4)
dialogue(
    "Lilith",
    "Please place your hand on the crystal ball, and it will check your magic proficiency.",
    color=MAGENTA,
    delay=4
)

narrator("You place your hand on the crystal ball.", 4)
narrator("The crystal ball starts glowing and emits a purple light.", 4)
narrator("Everyone around you stands in fear, Lilith can't close her mouth.", 4)

player("Uhh? 'm new here? What does this mean?", 4)

dialogue(
    "Lilith",
    "Ohh, it seems that you have a very high magic proficiency. "
    "But, this purple light is a sign of a very dangerous magic. ",
    color=MAGENTA,
    delay=6
)
dialogue(
    "Lilith",
    "Its the magic used by the witches.",
    color=MAGENTA,
    delay=6
)
player("So? Is that a bad thing?", 4)
dialogue(
    "Lilith",
    "Ofc it is. Empire has special forces to hunt down witches, and they will come after you.",
    color=MAGENTA,
    delay=6
)
player("But Im not a witch right?", 4)
player("I havent done anything wrong.", 4)
dialogue(
    "Lilith",
    "I know, but the Empire will not care about that. They will hunt you down and kill you.",
    color=MAGENTA,
    delay=6
)
player("Then what should I do?", 4)
narrator("Lilith takes you to a closed room and whispers to you.", 4)   
dialogue(
    "Lilith",
    "You need to hide your magic and create an alias.",
    color=MAGENTA,
    delay=6
)
player("How do I do that?", 4)
dialogue(
    "Lilith",
    "Your magic is very strong, you have the ability to hunt down witches. You can use that to your advantage."
    "You can create an alias and become a witch hunter. The Empire will not suspect you.",
    color=MAGENTA,
    delay=6
)
player("I see, then I will do that.", 4)
player("But how?", 4)
dialogue(
    "Lilith",
    "You need to find a witch and defeat her. That will prove your ability as a witch hunter.",
    color=MAGENTA,
    delay=6
)
player("But where can I find a witch?", 4)
dialogue(
    "Lilith",
    "There is a witch that has been causing trouble in the nearby village. You can start there.",
    color=MAGENTA,
    delay=6
)
player("I see, then I will head there.", 4)
narrator("Lilith gives you a map and some supplies.", 4)
narrator("You head out to find this witch.", 4)

# Journey to the first witch    

narrator("You reach the village.", 4)
narrator("Nothing remains here, only the empty houses", 4)
narrator("You see a few travelers wandering around.", 4)
player("Excuse me, do you know where I can find the witch?", 4)
dialogue(
    "Traveler",
    "Ohh, you are looking for the witch? She is in the forest nearby."
    "But be careful dear, she is very powerful and dangerous.",
    color=YELLOW,
    delay=4
)
player("Thank you for the information.", 4)
dialogue(
    "Traveler",
    "Young bastards dont really care their lives at all.",
    color=YELLOW,
    delay=4
)

narrator("You head into the forest.", 4) 
narrator("You see a small hut in the middle of the forest.", 4)     
narrator("You slowly approach the hut.", 4)
narrator("A woman with long black hair, long legs wearing a black robe comes out.", 4)
narrator("She has a very beautiful face, her charm is mesmerizing.", 4)

dialogue(
    "Witch",
    "Ohh my!! We have a new face here.",
    color=RED,
    delay=4
)
dialogue(
    "Witch",
    "I can feel your magic, it is very strong.",
    color=RED,
    delay=4
)
dialogue(
    "Witch",
    "You see I have been waiting for someone like you, my magic is unrefined and I needed someone to help me refine it.",
    color=RED,
    delay=4
)

dialogue(
    "Witch",
    "I want you as my partner, we can dual cultivate our magic and become the strongest.",
    color=RED,
    delay=4
)
choice = input("Do you want to accept the witch's offer? (yes/no): ").strip().lower()
if choice == "yes":
    player("I accept your offer.", 4)
    dialogue(
        "Witch",
        "Ohh, I am glad you accepted my offer. We will become the strongest together.",
        color=RED,
        delay=4
    )
    narrator("You and the witch start to dual cultivate your magic.", 4)
    narrator("You become the strongest sorcerer in the land.", 4)
    scene("THE END")

player("I am not interested in your offer.", 4)
player("I am here to defeat you and prove my ability as a witch hunter.", 4)

dialogue(
    "Witch",
    "What? A witch hunter? Oh my, what a shame, I was hoping to have a partner to refine my magic.",
    color=RED,
    delay=4
)

dialogue(
    "Witch",
    "But I guess I have no choice, I will have to kill you.",
    color=RED,
    delay=4
)

player("I will not let you harm anyone else.", 4)
narrator("You raise the wand, Lilith gave you", 4)
narrator("You damn witch, you don't know what you're dealing with!", 4)
narrator("Im the one who deafeated all the bosses in Heaven's Field, Im no scared of a mere witch", 4)

dialogue(
    "Witch",
    "You space out too much, you are not even aware of your surroundings."
    "Don't think of yourself as a protagonist of a novel, will you?",
    color=RED,
    delay=4
)

# Fight With the witch

narrator("The witch raises her wand and casts a spell.", 4)
narrator("A big fireball is coming at you", 4)
narrator("Ah! a fireball I can easily block it with the shield spell", 4)
narrator("You raise your wand to cast the shield spell but u pause", 4)
narrator("Wait, but how do i cast it?", 4)
narrator("The fireball is heading straight for you!", 4)
player("Ah!! Help me!!", 4)

scene("TO BE CONTINUED")
