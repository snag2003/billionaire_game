print("Do you want to play?")
answer_int = input("Enter Y for yes or N for no: ")
print(answer_int)

def new_question(question, price, option1, option2, option3, option4, answer):
    score = 0
    print("For $", price, ".", question)
    print("A.", option1)
    print("B.", option2)
    print("C.", option3)
    print("D.", option4)

    option1 = "A"
    option2 = "B"
    option3 = "C"
    option4 = "D"
    given_answer = input("Please enter A, B, C or D")
    print(given_answer)
    if given_answer == answer:
        score += price
        print("YOU GOT IT RIGHT!!!. You now own $", score, ". Please press enter to keep playing.")
        input()
    else:
        print("You got it wrong :( You lost " + str(score) + ". Please restart the code to try again.")
    

if answer_int == "Y":
    print("Well let's start!!!")
    print("We have 15 questions prepared for you with an acumulable amount of $1,000,000.")
    print("Remember the rules:")
    print("1. You must answer 15 multiple-choice questions correctly in a row to win the jackpot.")
    print("2. You may quit at any time and keep their earnings.")
    print("3. For each question, you are shown the question and four possible answers in advance before deciding whether to play on or not. If you do decide to offer an answer, it must be correct to stay in the game.")
    print("We will start right away with the first question. Press ENTER: ")
    input()
    new_question("In the UK, the abbreviation NHS stands for National what Service?", 100, "Humanity", "Health", "Honor", "Household", "B")
    new_question("Which Disney character famously leaves a glass slipper behind at a royal ball?", 200, "Pocahontas", "Sleeping Beauty", "Cinderella", "Elsa", "C")
    new_question("What name is given to the revolving belt machinery in an airport that delivers checked luggage from the plane to baggage reclaim?", 300, "Hangar", "Terminal", "Concourse", "Carousel", "D")
    new_question("Which of these brands was chiefly associated with the manufacture of household locks?", 500, "Phillips", "Flymo", "Chubb", "Ronseal", "C")
    new_question("The hammer and sickle is one of the most recognisable symbols of which political ideology?", 1000, "Republicanism", "Communism", "Conservatism", "Liberalism", "B")
    new_question("Which toys have been marketed with the phrase “robots in disguise”?", 2000, "Bratz Dolls", "Sylvanian Families", "Hatchimals", "Transformers", "D")
    new_question("What does the word loquacious mean?", 4000, "Angry", "Chatty", "Beautiful", "Shy", "B")
    new_question("Obstetrics is a branch of medicine particularly concerned with what?", 8000, "Childbirth", "Broken bones", "Heart Conditions", "Old Age", "A")
    new_question("In Doctor Who, what was the signature look of the fourth Doctor, as portrayed by Tom Baker?", 16000, "Bow-tie, braces and tweed jacket", "Wide-brimmed hat and extra long scarf", "Pinstripe suit and trainers", "Cape, velvet jacket and frilly shirt", "B")
    new_question("Which of these religious observances lasts for the shortest period of time during the calendar year?", 32000, "Ramadan", "Diwali", "Lent", "Hanukkah", "B")
    new_question("At the closest point, which island group is only 50 miles south-east of the coast of Florida?", 64000, "Bahamas", "US Virgin Islands", "Turks and Caicos Islands", "Bermuda", "A")
    new_question("Construction of which of these famous landmarks was completed first?", 125000, "Empire State Building", "Royal Albert Hall", "Eiffel Tower", "Big Ben Clock Tower", "D")
    new_question("Which of these cetaceans is classified as a “toothed whale”?", 250000, "Gray Whale", "Minke Whale", "Sperm Whale", "Humpback Whale", "C")
    new_question("Who is the only British politician to have held all four “Great Offices of State” at some point during their career?", 500000, "David Lloyd George", "Harold Wilson", "James Callaghan", "John Major", "C")
    new_question("In 1718, which pirate died in battle off the coast of what is now North Carolina?", 1000000, "Calico Jack", "Blackbeard", "Bartholomew Roberts", "Captain Kidd", "B")
    print("OMG YOU GOT EVERYTHING RIGHT!!!")
    print("YOU JUST WON")
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    print("ONE")
    print("MILLION")
    print("DOLLARS")
    print("$$$$$$$$$$$$$$$$$$$$$$$")
elif answer_int == "N":
    print("Oh, well... GET OUT OF HERE!!!")
else:
    print("You entered a wrong letter. :(")