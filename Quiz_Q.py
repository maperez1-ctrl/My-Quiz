
# this is used for random values for the game
import random



# Questions
# I wanted to use a tuple instead of a string cause i got worried about messing things up if i moved around my list to much.
questions = ("What is the closest living relative of a manatee :",
            "In the game deltarune whats charater is the creators self-insert :",
            'What monster in monster hunter is know to the community as "the pickle :", ',
            "Who are the big three in shonen:",
            "The japanese race horse Stay Gold sired many famous race horses, however which one is the most famous and responsible for the 12 billion yen incedent:",
            "What is the true meaning of the name Matthew:",
            "What is the reason men are worse at dealing with illness than woman are?:", 
            "Who is the aura master of Dragon Ball:", 
            "What bird lays an egg so big ,compared to its body size, that it rearranges its internal organs and bones:",
            "The iconic bald egale screech is actual a? :",
            "What is the strongest competitive dual typing in pokemon:", 
            "In jiujitsu kaisen, what is the name of the prized curesed techniqe of the zenin clan:",
            "In the X-men, who has the mutant ability to make portals to limbo?:",
            "What animal has the strongest punch per milimeter in the animal kindom:",
            "In team Avater for Avater Last Air Bender who is the only non-bender named? :",
            "How tall is Bad Bunny? :" ,
            "What is the name of the current dictating party of Nicaragua :",)
            
# This took way longer than it should have            
options = (("A. Dolphin ", "B. Fish ", "C. Elephant ", "D. Possom "),
            ("A. Asgore ", "B. Dess ", "C. Sans ", "D. Annoying Dog "),
            ("A. Jin Dahaad ", "B. Deviljho ", "C. Shara Ishvalda ", "D. Kulu-Ya-Ku"),
            ("A. One Piece, Bleach, Naruto ", "B. DragonBall, Sailor Moon, Evangelion ", "C. DragonBall, Konosuba, Jujutsu Kaisen ", "D. My Hero, Re: Zero, Banananya"),
            ("A. Gold Ship ", "B. Fenomeno ", "C. Orfevre ", "D. Nakayama Festa"),
            ("A. Pain ", "B. Flea ", "C. Gift from God ", "D. Gift of patience "),
            ("A. Men are Dramatic", "B. Girls are built different ", "C. Girls are better with illness to protect babies ", "D. Testosterone is a immune suppressant "),
            ("A. Yamacha ", "B. Piccolo ", "C. Goku ", "D. Tein "),
            ("A. Swan", "B. Peacock ", "C. Spoonbill", "D. Kiwi "),
            ("A. Chicken ", "B. Redtailed Hawk ", "C. Peregrine Falcon ", "D. American Seagull "),
            ("A. Fairy-Steel ", "B. Steel-Water ", "C. Ghost-Normal ", "D. Ice-Grass "),
            ("A. Projection Sorcery", "B. Straw Doll Technique ", "C. Infinity ", "D. The Ten Shadows "),
            ("A. Magik ", "B. Storm ", "C. Jean Grey ", "D. Jubalie "),
            ("A. Mantis Shrimp", "B. Gorilla ", "C. Kangaroo ", "D. Human "),
            ("A. Zuko ", "B. Toph ", "C. Sokka ", "D. Katara"),
            ("A. 5'11 ", "B. 5'8 ", "C. 6'2 ", "D. 5'6 "),
            ("A. Contra ", "B. Sandinista ", "C. Communist ", "D. Independent Libral "))

# I am preparing for the num i will need to store with these three
Answers = ("C", "D", "B", "A", "A", "C", "D", "B", "D", "B", "A", "D", "A", "A", "C", "A", "B")
score = 0
coins = 0

# Ok so i need question num to keep track of the questions and answers
question_num = 0
# This was going to be for guesses but ill use it for input
guesses = []
# Ill be honest never thought to use a bool needed help for this
do_over = False






#My first thought was if/then but this just makes everthing run at once and then i put conditions
while question_num < len(questions):
    question = questions[question_num]
    print("-----------------------")
    print(question)

    # This is where i use the randomizer to control game events
    rng = random.randint(1, 100)

    if rng <= 15:
        print("Taxes have been bad this year -3") # Got this idea from Gas prices
        coins -= 3
        print(f"{coins}")
    
    
        
    # My answers i just attanched to the queston num so they stay together
    for option in options[question_num]:
        print(option)

    

    # Shop Function :) Just made them correspond to nums
    def shop(coins):
        print("1. Skip question (cost: 3 coins)")
        print("2. Extra point (cost: 5 coins)")
        print("3. Exit shop")


        return input ("Choose an option: ")

    #Since its input anyway i put the shop with the question options
    guess = input("Enter (A, B, C, D) or Shop: ").upper()

    
    if guess == "SHOP":

        # The actual shop or at least the items is if/thens for options
        choice = shop(coins)   
        if choice == "1" and coins >= 3:
            coins -= 3
            question_num += 1
            print("skipped")
            continue

        elif choice == "2" and coins >= 5:
            coins -= 5
            score += 1

        elif choice == "3":
            pass

        else:
            print (" Either you're broke or can't read and push the wrong button")

        guess = input ("Now answer the Question: ").upper()



    
    
    

    


    #To compare
    guesses.append(guess)

    # to check answers 
    if guess == Answers[question_num]:
        score += 1
        coins += 5
        print(f"you're right, your coins: {coins}")
        


    else:
        print(f" Don't Worry i didn't expect you to know, your coins: {coins}")
        



    # I put the other rng way down here so it happens after the question
    if 40 <= rng <= 50:
        print("Do Over! same question again")
        continue     
    question_num += 1



# Score count how many you got
score = int(score)
print (f"Score: {score}")





