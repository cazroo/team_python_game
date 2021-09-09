import sys
import random
import time


def print_slow(str):
    for char in str:
        time.sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()


round = [
    "Round 1"
    "Round 2"
    "Round 3"
    "Round 4"
]

# ## Intro ###

name = input("So contestant, what's your name? ")
print("\033[H\033[J")              
                
print_slow(f"Well {name}, welcome to...")
time.sleep(2)
print("\033[H\033[J")                
                
print("""
                  __                                                   
       __        /\ \                                                  
 _ __ /\_\    ___\ \ \/'\   __  __                                     
/\`'__\/\ \  /',__\ \ , <  /\ \/\ \                                     
\ \ \/ \ \ \/\__, `\ \ \ \`\ \ \_\ \                                    
 \ \_\  \ \_\/\____/\ \_\ \_\/`____ \                                   
  \/_/   \/_/\/___/  \/_/\/_/`/___/> \                                 
                             __ /\___/                                 
                 __   __  __/\_\ \/____    ___      __    ____   ____  
               /'__`\/\ \/\ \/\ \/\_ ,`\ /' _ `\  /'__`\ /',__\ /',__\ 
              /\ \L\ \ \ \_\ \ \ \/_/  /_/\ \/\ \/\  __//\__, `/\__, `\ 
              \ \___, \ \____/\ \_\/\____\ \_\ \_\ \____\/\____\/\____/
               \/___/\ \/___/  \/_/\/____/\/_/\/_/\/____/\/___/ \/___/ 
                    \ \_\                                              
                     \/_/                                                                                            
                     """)
time.sleep(3)
print("\033[H\033[J")

print_slow("""
Like all good games - and don't be mistaken, this is a good game - you stand to win a cash prize.
""")
time.sleep(3)
print("\033[H\033[J")


print_slow("""
Your starting prize fund is a cool $50,000; however,
over the rounds you risk losing that precious cash with every incorrect answer.
""")
time.sleep(3)
print("\033[H\033[J")

print_slow("""
Incorrect answers in Round 1 cost you $1,000,
Those in Round 2 cost $3,000.
Mistakes in Round 3 cost $5,000; but
the real hard hitter is Round 4 where wrong 
answers cost you a whopping $10,000""")
time.sleep(3)
print("\033[H\033[J")

print_slow("""
When you're ready to give your answer, type A, B, C or D on your keyboard to select your choice
""")
time.sleep(3)
print("\033[H\033[J")

print_slow("Now, onto Round 1 we GOOOO!")
time.sleep(2)
print("\033[H\033[J")
cash = 50000

# round1
def quiz_1():
    correct = int(0)
    incorrect = int(0)
    global cash
        
    print(f"Round 1                      £{cash}\n")

    print_slow("After the invasion of which country, did the United Kingdom enter into a war with Germany?\nA = Czechoslovakia\nB = Austria\nC = Serbia\nD = Poland\n")
    answer1 = input("Answer: ")
    if answer1 == "D" or answer1 == "d":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! You got the first question wrong that doesn't bode well for the rest of the game. ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")
   
    
    print_slow("Solar panels generate electricity from what source?\nA = The Sun\nB = The Sea \nC = The Wind\nD = The Earth")
    answer2 = input("\nAnswer: ")
    if answer2 == "A" or answer2 == "a":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
        print("\033[H\033[J")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! ({cash})")
    time.sleep(2)
    print("\033[H\033[J")


    2
    print_slow("What country is brie cheese originally from?\nA = Germany\nB = Belgium\nC = France\nD = Luxembourg\n")
    answer3 = input("Answer:")
    if answer3 == "C" or answer3 == "c":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print_slow("In what 80’s year did Queen inform everyone that Another one had Bitten the Dust?\nA - 1982\nB - 1980\nC - 1987\nD - 1985")
    answer15 = input("\nAnswer:")
    if answer15 == "B" or answer15 == "b":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print_slow("What is the largest ocean on Earth?\nA: Indian\nB: Pacific\nC: Atlantic\nD: Arctic")
    answer5 = input("\nAnswer:")
    if answer5 == "B" or answer5 == "b":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")


    print_slow("""
    Well done on completing the first round!
    Looks like you might be a bit of a whiz kid, huh?
    Let's keep that energy up in Round 2
    """)
    time.sleep(2)
    print("\033[H\033[J")


# Round2
    2
    print_slow("Which is the only country to have won 3 Eurovision Song Contests in a row (1992, 1993 and 1994)?\nA - Sweden\nB - Ireland\nC - Greece\nD - United Kingdom")
    answer6 = input("\nAnswer:")
    if answer6 == "B" or answer6 == "b":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
        print("\033[H\033[J")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")
    
    2
    print_slow("How many strings does a violin have?\nA = 5\nB = 6\nC = 4\nD = 7")
    answer7 = input("\nAnswer:")
    if answer7 == "C" or answer7 == "c":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
        print("\033[H\033[J")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print_slow("Who discovered germs?\nA = Louis Pasteur\nB = Robert Koch\nC = Claudius Galenus\nD = Edward Jenner")
    answer8 = input("\nAnswer: ")
    if answer8 == "A" or answer8 == "a":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print_slow("What social media app only lets you view pictures and messages for a limited time?\nA = Instagram\nB = Facebook\nC = Twitter\nD = Snapchat")
    answer9 = input("\nAnswer: ")
    if answer9 == "D" or answer9 == "d":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print_slow("What is the highest mountain in England?\nA: Carrauntoohil\nB: Ben Nevis\nC: Scafell Pike\nD:Snowdon")
    answer10 = input("\nAnswer: ")
    if answer10 == "c" or answer10 == "C":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    print_slow("""
    Looks like you've risen to the challenge and managed to keep
    that cash nicely topped up
    Let's see if you're able to continue it 
    in Round 3
    """)
    time.sleep(2)
    print("\033[H\033[J")

    # Round3

    2
    print_slow("What is the geographical term for a group, or chain, of islands?\nA: Archipelago\nB: Atoll\nC: Cove\nD: Cape")
    answer11 = input("\nAnswer: ")
    if answer11 == "A" or answer11 == "a":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Who wrote the Lord of the Rings books?\nA = JRR Tolkien\nB = George RR Martin\nC = RA Salvatore\nD = CSS Lewis\n")
    answer12 = input("Answer: ")
    if answer12 == "A" or answer12 == "a":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Which infamous psychologist created the theories of psychoanalysis?\nA = Karl Jung\nB = Sigmund Freud\nC = Theodore Adorno\nD = Alfred Adler")
    answer13 = input("\nAnswer: ")
    if answer13 == "B" or answer13 == "b":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Who is the lead singer of Radiohead?\nA - Jonny Greenwood\nB - Ed O’Brien\nC - Philip Selway\nD - Thom Yorke")
    answer14 = input("\nAnswer: ")
    if answer14 == "D" or answer14 == "d":
        correct += 1
        print_slow(f"Correct ({cash}! Next round...\n")
    else:
        incorrect += 1
        cash -= 5000
    print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What year was the first Iphone released?\nA = 2005\nB = 2007\nC = 2008\nD = 2010")
    answer15 = input("\nAnswer: ")
    if answer15 == "B" or answer15 == "b":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    print_slow(f"""
    Things getting a bit tricky now, eh?
    Well you've made your way to the final round
    Remember, wrong answers cost you $10,000 here so tread carefully!
    Good luck, and Godspeed
    """)
    time.sleep(2)
    print("\033[H\033[J")


    # Round 4
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What year was the World Wide Web (www.) released for public use?\nA = 1987\nB = 1989\nC = 1991\nD = 1993\n")
    answer16 = input("Answer: ")
    if answer16 == "B" or answer16 == "b":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What year was Marmite invented?\nA = 1902\nB = 1929\nC = 1859\nD = 1932\n")
    answer17 = input("Answer: ")
    if answer17 == "A" or answer17 == "a":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")
    
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What forms the tectonic boundary between the Pacific Plate and the North American Plate?\nA: San Andreas Fault\nB: Palu-Koro Fault\nC: Atacama Fault\nD: Gulf of California Rift Zone")
    answer18 = input("\nAnswer: ")
    if answer18 == "b" or answer18 == "B":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("In which year was modern anaesthesia discovered?\nA = 1841\nB = 1842\nC = 1849\nD = 1856")
    answer19 = input("\nAnswer: ")
    if answer19 == "B" or answer19 == "b":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")

    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Which Disney film did Demi Lovato star in?\nA = High School Musical\nB = Hannah Montana The Movie\nC = Camp Rock\nD = The Lizzie")
    answer20 = input("\nAnswer: ")
    if answer20 == "C" or answer20 == "c":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 100000
        print_slow(f"Wrong! ({cash})\n")
    time.sleep(2)
    print("\033[H\033[J")
    return

def quiz_2():
    correct = int(0)
    incorrect = int(0)
    global cash
    # round1
    if cash <= 0:
        print ("Sorry you have gone bankrupt. You will not be walking away with any cash today")
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("After the invasion of which country, did the United Kingdom enter into a war with Germany?\nA = Czechoslovakia\nB = Austria\nC = Serbia\nD = Poland\n")
    answer1 = input("Answer: ")
    if answer1 == "D" or answer1 == "d" or answer1 == "Poland":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! ({cash})\n")
       
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Solar panels generate electricity from what source?\nA = The Sun\nB = The Sea \nC = The Wind\nD = The Earth")
    answer2 = input("\nAnswer: ")
    if answer2 == "A" or answer2 == "a" or answer2 == "The Sun":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! ({cash})\n")

    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What country is brie cheese originally from?\nA = Germany\nB = Belgium\nC = France\nD = Luxembourg")
    answer3 = input("\nAnswer: ")
    if answer3 == "C" or answer3 == "c" or answer3 == "France":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! ({cash})\n")

    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("In what 80’s year did Queen inform everyone that Another one had Bitten the Dust?\nA - 1982\nB - 1980\nC - 1987\nD - 1985")
    answer15 = input("\nAnswer: ")
    if answer15 == "B" or answer15 == "b" or answer15 == "1980":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What is the largest ocean on Earth? 
    A: Indian 
    B: Pacific 
    C: Atlantic 
    D: Arctic\n""")
    answer5 = input("Answer: ")
    if answer5 == "B" or answer5 == "b" or answer5 == "Pacific":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! ({cash})\n")
    
    2
    print_slow("""
    Well done on completing the first round!
    Looks like you might be a bit of a whiz kid, huh?
    Let's keep that energy up in Round 2
    """)
    time.sleep(2)
    print("\033[H\033[J")
    prizemoney = cash
    # Round2
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Which is the only country to have won 3 Eurovision Song Contests in a row (1992, 1993 and 1994)?\nA - Sweden\nB - Ireland\nC - Greece\nD - United Kingdom")
    answer6 = input("\nAnswer: ")
    if answer6 == "B" or answer6 == "b" or answer6 == "Ireland":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("How many strings does a violin have?\nA = 5\nB = 6\nC = 4\nD = 7")
    answer7 = input("\nAnswer: ")
    if answer7 == "C" or answer7 == "c" or answer7 == "4":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Who discovered germs?\nA = Louis Pasteur\nB = Robert Koch\nC = Claudius Galenus\nD = Edward Jenner")
    answer8 = input("\nAnswer: ")
    if answer8 == "A" or answer8 == "a" or answer8 == "Louis Pasteur":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What social media app only lets you view pictures and messages for a limited time?\nA = Instagram\nB = Facebook\nC = Twitter\nD = Snapchat")
    answer9 = input("\nAnswer: ")
    if answer9 == "D" or answer9 == "d" or answer9 == "Snapchat":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What is the highest mountain in England? 
    A: Carrauntoohil 
    B: Ben Nevis
    C: Scafell Pike 
    D: Snowdon\n""")
    answer10 = input("Answer: ")
    if answer10 == "C" or answer10 == "c":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print_slow("""
    Looks like you've risen to the challenge and managed to keep
    that cash nicely topped up
    Let's see if you're able to continue it 
    in Round 3
    """)
    time.sleep(2)
    print("\033[H\033[J")

    # Round3
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Which continent has the most LEDCs? 
    A: Europe 
    B: South America 
    C: Africa 
    D: Asia\n""")
    answer11 = input("Answer: ")
    if answer11 == "C" or answer11 == "c":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Who wrote the Lord of the Rings books?\nA = JRR Tolkien\nB = George RR Martin\nC = RA Salvatore\nD = CSS Lewis")
    answer12 = input("\nAnswer: ")
    if answer12 == "A" or answer12 == "a" or answer12 == "JRR Tolkein":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Which infamous psychologist created the theories of psychoanalysis?\nA = Karl Jung\nB = Sigmund Freud\nC = Theodore Adorno\nD = Alfred Adler")
    answer13 = input("\nAnswer: ")
    if answer13 == "B" or answer13 == "b" or answer13 == "Theodore Adorno":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Who is the lead singer of Radiohead?\nA - Jonny Greenwood\nB - Ed O’Brien\nC - Philip Selway\nD - Thom Yorke")
    answer14 = input("\nAnswer: ")
    if answer14 == "D" or answer14 == "d" or answer14 == "Thom Yorke":
        correct += 1
        print_slow(f"Correct ({cash}! Next round...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What year was the first Iphone released?\nA = 2005\nB = 2007\nC = 2008\nD = 2010")
    answer15 = input("\nAnswer: ")
    if answer15 == "B" or answer15 == "b" or answer15 == "2007":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print_slow(f"""
    Things getting a bit tricky now, eh?
    Well you've made your way to the final round
    Remember, wrong answers cost you $10,000 here so tread carefully!
    Good luck, and Godspeed
    """)
    time.sleep(2)
    print("\033[H\033[J")

    # Round 4
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What year was the World Wide Web (www.) released for public use?\nA = 1987\nB = 1989\nC = 1991\nD = 1993\n")
    answer16 = input("Answer: ")
    if answer16 == "B" or answer16 == "b" or answer16 == "1989":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What year was Marmite invented?\nA = 1902\nB = 1929\nC = 1859\nD = 1932\n")
    answer17 = input("Answer: ")
    if answer17 == "A" or answer17 == "a" or answer17 == "1902":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What forms the tectonic boundary between the Pacific Plate and the North American Plate? 
    A: San Andreas Fault 
    B: Palu-Koro Fault 
    C: Atacama Fault 
    D: Gulf of California Rift Zone\n""")

    answer18 = input("Answer:")
    if answer18 == "A" or answer18 == "a":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print_slow("In which year was modern anaesthesia discovered?\nA = 1841\nB = 1842\nC = 1849\nD = 1856")
    answer19 = input("\nAnswer:")
    if answer19 == "B" or answer19 == "b" or answer19 == "1842":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Which Disney film did Demi Lovato star in?\nA = High School Musical\nB = Hannah Montana The Movie\nC = Camp Rock\nD = The Lizzie")
    answer20 = input("\nAnswer: ")
    if answer20 == "C" or answer20 == "c" or answer20 == "Camp Rock":
        correct += 1
        print_slow(f"Correct ({cash})! Next round...\n")
    else:
        incorrect += 1
        cash -= 100000
        print_slow(f"Wrong! ({cash})\n")
    print("\033[H\033[J")
    2
def quiz_3():
    correct = int(0)
    incorrect = int(0)
    global cash

    def print_slow(str):
        for char in str:
            time.sleep(2)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        if cash <= 0:
            print ("Sorry but that means you are too dumb to make any cash today. Better luck with the rest of your pityful life")

    round = "Round One"

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round One!
    Which 90s, noodle headed, boy band’s name was the amalgamation of the last letters of each of the 5 members’ surnames?
        A - Blue
        B - Five  
        C - LFA  
        D - NSYNC\n""")
    r1q1 = input("\nAnswer: ")
    if r1q1 == "d" or r1q1 == "D":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    2
    print_slow("""During the reign of Elizabeth I of England, which country sent an armada invasion fleet?
        A - Italy 
        B - Germany 
        C - Spain 
        D - The Netherlands\n""")
    r1q2 = input("\nAnswer: ")
    if r1q2 == "c" or r1q2 == "C":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! Next question...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What nut is in the middle of a Ferrero Rocher? 
        A- Brazil Nut 
        B - Hazelnut
        C - Macadamia Nut 
        D - Marcona Almond\n""")
    r1q3 = input("Answer: ")
    if r1q3 == "b" or r1q3 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! Next question...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What is the name of the classic 1972 arcade game based on table tennis? 
        A - Frogger 
        B - Pong 
        C - Pacman 
        D - Space Invaders\n""")
    r1q4 = input("Answer: ")
    if r1q4 == "b" or r1q4 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! Next question...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""How many countries make up the United Kingdom? 
        A - 1 
        B - 2 
        C - 3  
        D - 4\n""")
    r1q5 = input("Answer: ")
    if r1q5 == "d" or r1q5 == "D":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! Next question...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! You have £{cash} remaining.\n Next question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print_slow("""
    Well done on completing the first round!
    Looks like you might be a bit of a whiz kid, huh?
    Let's keep that energy up in Round 2
    """)
    time.sleep(2)
    print("\033[H\033[J")


    ####### ROUND 2 ########
    round = "Round 2"
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Greatly revered British nurse Florence Nightingale is well-known for her work in British hospitals, and her standards of cleanliness - but on which battlefields did she first operate as a nurse/medic?
        A - Kabul 
        B - Crimea 
        C - Zara 
        D - Aleppo\n""")
    r2q1 = input("Answer: ")
    if r2q1 == "b" or r2q1 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Which mathematical symbol was the title of Ed Sheeran’s first album in 2011?
        A - +  
        B - X  
        C - =  
        D - %\n""")
    r2q2 = input("Answer: ")
    if r2q2 == "b" or r2q2 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""In which sport can you throw a “curveball? 
        A - Basketball 
        B - Bowling 
        C - Baseball 
        D - Handball\n""") 
    r2q3 = input("Answer: ")

    if r2q3 == "c" or r2q3 == "C":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What popular games console did Luigi's Mansion debut on? 
        A - Xbox 360 
        B - Gamecube 
        C - Dreamcast 
        D - Playstation 2\n""")
    r2q4 = input("Answer: ")

    if r2q4 == "b" or r2q4 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""The European Union is made up of how many member states? 
        A - 26 
        B - 30 
        C - 27 
        D - 28\n""")
    r2q5 = input("Answer: ")

    if r2q5 == "c" or r2q5 == "C":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print_slow("""
    Looks like you've risen to the challenge and managed to keep
    that cash nicely topped up
    Let's see if you're able to continue it 
    in Round 3
    """)
    time.sleep(2)
    print("\033[H\033[J")

    ################# Round 3 ##############
    round = "Round 3"
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round 3!
    Who created the first vaccines?
        A = Edward Jenner 
        B = Robert Koch 
        C = Andreas Vesalius 
        D = Alexander Semmelweiss\n""")
    r3q1 = input("Answer: ")
    if r3q1 == "a" or r3q1 == "A":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What is the real first name of ‘Ozzy’ Osbourne?
        A - John  
        B - Michael  
        C - Tom  
        D - Oswald\n""")
    r3q2 = input("Answer: ")
    if r3q2 == "a" or r3q2 == "A":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What unit of length is qual to around 5.8 trillion miles? 
        A = Kilometre 
        B = Centimetre 
        C = Lightyear 
        D = Furlong\n""")
    r3q3 = input("Answer: ")
    if r3q3 == "c" or r3q3 == "C":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What fashion house is behind the perfume, 'Light Blue'? 
        A - Versace
        B - Chanel
        C - Christian Dior
        D - Dolce & Gabbana\n""") 
    r3q4 = input("Answer: ")
    if r3q4 == "d" or r3q4 == "D":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What is the geographical term for a group, or chain, of islands? 
        A - Archipelago 
        B - Atoll 
        C - Cove 
        D - Cape\n""")
    r3q5 = input("Answer: ")
    if r3q5 == "a" or r3q5 == "A":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)

    print("\033[H\033[J")
    2
    print_slow(f"""
    Things getting a bit tricky now, eh?
    Well you've made your way to the final round
    Remember, wrong answers cost you $10,000 here so tread carefully!
    Good luck, and Godspeed
    """)
    time.sleep(2)
    print("\033[H\033[J")

    ################# Round 4 ##################
    round = "Round 4"
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round Four!
    Before it’s inception as a modern nation state, Canada was ruled as a colony of the British Empire - but which year was the country given independence?
        A - 1897 
        B - 1921 
        C - 1948 
        D - 1982\n""")
    r4q1= input("Answer: ")
    if r4q1 == "d" or r4q1 == "D":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""An album or single is certified Diamond Selling if it has sold how many copies?
        A - 1 Million  
        B - 10 Million  
        C - 50 Million  
        D - 100 Million\n""")
    r4q2= input("Answer: ")
    if r4q2 == "b" or r4q2 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Where does the Greek Goddess Persephone spend half of the year?
        A - Mount Olympus 
        B - The Underworld
        C - Knossos Palace
        D - Mount Ida\n""")
    r4q3= input("Answer: ")
    if r4q3 == "b" or r4q3 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""In what year was the first transatlantic radio broadcast? 
        A - 1887 
        B - 1921 
        C - 1905 
        D - 1902\n""")
    r4q4= input("Answer: ")
    if r4q4 == "d" or r4q4 == "D":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Which strait, located between the Pacific and Arctic oceans, separates the Chukchi Peninsula? 
        A - Menai 
        B - Messina 
        C - Malacca 
        D - Bering\n""")
    r4q5 = input("Answer: ")
    if r4q5 == "b" or r4q5 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    2
def quiz_4():
    global cash
    right = ["\nCorrect!", "\nBingo!", "\nNot bad!", "\nYou've done this before!", "\nMeh, that was easy.", "\nWhoop!", "\npffft - even I knew that!", "\nIncredible!\nWell, for you...", "\nImpressive...\nSort of...", "\n*Rapturous applause*", "\nHmph, I'm impressed.", "\n*Approving nod*", "\nHey, you got that right!", "\n...Oh, yes,\nRight answer!"]
    wrong = ["\nWrong!", "\nNope!", "\nNada.", "\nSeriously?", "\nYou're embarrasing both of us!", "\nOh well, can't win 'em all!", "\nPffffft.", "\nIncorrect! Shame.", "\nHey, where's the ASCII art of me faecpalming?", "\nEver heard the phrase 'quit while you're ahead'? Yeah, pretty relevant right now.", "\nYou got that one wrong - too bad!", "\nBahaha!\nThat was a joke, right?", "\nAwkward...", "\nYou've gotta be joking? No!", "\nNot quite but...\nQue Sera Sera."]
    nq = ["Moving on!", "Next round...", "Onwards!", "Onto the next!", "Having fun? \nYou shouldn't be!", "Next!", "And again!", "Are you bored?\nI'm bored."]

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Here comes Round 1...\nThinking caps on!\nNow remember: take your time - there's no pressure...")
    2
    print_slow ("\nOnly a big bunch of people waiting to see you fail - er, I mean, win!\nAnyhoo...\n")
    time.sleep(2)
    print("\033[H\033[J")

    #Round1 #Question1
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Roman Emperor Julius Ceaser was infamously stabbed to death - but who was he most surprised to find had betrayed him?\n\nA: Mark Anthony \nB: Marcus Junius Brutus \nC: Marcus Aurelius \nD: Octavian Augustus\n")
    r1a1 = input("\nAnswer:")
    if r1a1 == "B" or r1a1 == "b":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
        2  
    else:
        cash -= 1000
        print_slow(f"Et tu? Nevermind...\nTotal: £{cash}\nBetter luck next time...")
    time.sleep(2)

    print("\033[H\033[J")
    2
    #Question2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Which 80s star is recognised by Guinness World Records as the best-selling female recording artist of all time?\n\nA: Madonna \nB: Diana Ross \nC: Pat Benatar \nD: Tina Turner\n")
    r1a2 = input("\nAnswer: ")
    if r1a2 == "A" or r1a2 == "a":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
          
    else:
        cash -= 1000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)
    print("\033[H\033[J")
    
        #Question3
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What's the biggest animal in the world?\n\nA: Blue Whale \nB: African Elephant \nC: Colossal Squid \nD: Whale Shark\n")
    r1a3 = input("\nAnswer: ")
    if r1a3 == "A" or r1a3 == "a":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
        2      
    else:
        cash -= 1000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)  
    print("\033[H\033[J")
    
    #Question4
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Who invented the aeroplane?\n\nA: Richard Branson \nB: Nikola Tesla \nC: The Wright Brothers \nD: Harvey Hubbell\n")
    r1a4 = input("\nAnswer: ")
    if r1a4 == "C" or r1a4 == "c":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq)) 
    else:
        cash -= 1000
        print_slow("Wright! It's the Wrong Brothers! \nI mean, wrong! It's the Wright Brothers!")
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)  
    print("\033[H\033[J")
    #Question5
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("How many states make up the USA?\n\nA: 50 \nB: 49 \nC: 62 \nD: 51\n")
    r1a5 = input("\nAnswer: ")
    if r1a5 == "A" or r1a5 == "a":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        2  
    else:
        cash -= 1000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
    time.sleep(2) 
    print("\033[H\033[J")
    #ROUND2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("And so ends Round 1.") 
    print_slow("""
    Well done on completing the first round!
    Looks like you might be a bit of a whiz kid, huh?
    Let's keep that energy up in Round 2
    """)
    print("\033[H\033[J")
    #QUESTION1
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("In which year did Queen Elizabeth II ascend to the British throne?\n\nA: 1952 \nB: 1953 \nC: 1955 \nD: 1956\n")
    r2a1 = input("\nAnswer: ")
    if r2a1 == "A" or r2a1 == "a":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
        2  
    else:
        cash -= 3000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)
    print("\033[H\033[J") 
    #QUESTION2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Three of the top 15 best-selling albums of the 00s belong to which four-piece band?\n\nA: Snow Patrol \nB: Take That \nC: Coldplay \nD: The Killers\n")
    r2a2 = input("\nAnswer: ")
    if r2a2 == "C" or r2a2 == "c":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    else:
        cash -= 3000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2) 
    print("\033[H\033[J")
    #QUESTION3
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("In which country was the 2008 Olympics held?\n\nA: London \nB: China \nC: Brazil \nD: Japan\n")
    r2a3 = input("\nAnswer: ")
    if r2a3 == "B" or r2a3 == "b":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
        2  
    else:
        cash -= 3000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)  
    print("\033[H\033[J")
    #QUESTION4
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Since 2017, how many characters can a single tweet be when posting on Twitter?\n\nA: 144 \nB: 200 \nC: 240 \nD: 280\n")
    r2a4 = input("\nAnswer: ")
    if r2a4 == "D" or r2a4 == "d":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    else:
        cash -= 3000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)
    print("\033[H\033[J")
    #QUESTION5
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Bucharest is the capital of which country?\n\nA: Hungary \nB: Romania \nC: Czech Rep \nD: Croatia\n")
    r1a5 = input("\nAnswer: ")
    if r1a5 == "B" or r1a5 == "b":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")    
    else:
        cash -= 3000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
    time.sleep(2)
    print("\033[H\033[J")
    #ROUND3
    print_slow("""
    Looks like you've risen to the challenge and managed to keep
    that cash nicely topped up
    Let's see if you're able to continue it 
    in Round 3
    """)
    time.sleep(2)
    print("\033[H\033[J")
    #QUESTION1
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Which two men are cited as the discoverers of DNA?\n\nA: Lambert and Butler \nB: Crick and Watson \nC: Holmes and Watson \nD: Dobash and Dobash\n")
    r3a1 = input("\nAnswer: ")
    if r3a1 == "B" or r3a1 == "b":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        time.sleep(2)
        print_slow(random.choice(nq))
    else:
        cash -= 5000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)
    print("\033[H\033[J")
    #QUESTION2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Which Scottish band released Take Me Out in 2004?\n\nA: Biffy Clyro \nB: The Fratellis \nC: Franz Ferdinand \nD: Snow Patrol\n")
    r3a2 = input("\nAnswer: ")
    if r3a2 == "C" or r3a2 == "c":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    else:
        cash -= 5000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)
    print("\033[H\033[J")
    #QUESTION3
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print("\033[H\033[J")
    2
    print_slow("How many actors have played the role of James Bond?\n\nA: 5 \nB: 7 \nC: 11 \nD: 9\n")
    r3a3 = input("\nAnswer: ")
    if r3a3 == "D" or r3a3 == "d":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
             
    else:
        cash -= 5000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)
    print("\033[H\033[J")
    #QUESTION4
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Bill Gates dropped out of which university?\n\nA: Harvard \nB: Cambridge \nC: Oxford \nD: Stanford\n")
    r3a4 = input("\nAnswer: ")
    if r3a4 == "A" or r3a4 == "a":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))  
    else:
        cash -= 5000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)
    print("\033[H\033[J")
    #QUESTION5
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("The strait of Gibraltar separates the Iberian peninsula from which African country?\n \nA: Sudan \nB: Morocco \nC: Egypt \nD: Libya\n")
    r3a5 = input("\nAnswer: ")
    if r3a5 == "B" or r3a5 == "b":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
    else:
        cash -= 5000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
    time.sleep(2)
    print("\033[H\033[J") 
    
    # ROUND4

    print_slow(f"""
    Things getting a bit tricky now, eh?
    Well you've made your way to the final round
    Remember, wrong answers cost you $10,000 here so tread carefully!
    Good luck, and Godspeed
    """)
    time.sleep(2)
    print("\033[H\033[J")
    
    #QUESTION1
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Which infamous psychologist created the theories of psychoanalysis?\n \nA: Karl Jung \nB: Sigmund Freud  \nC: Theodore Adorno \nD: Aldred Adler\n")
    r4a1 = input("\nAnswer: ")
    if r4a1 == "B" or r4a1 == "b":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
        2  
    else:
        cash -= 10000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)
    print("\033[H\033[J")

    #QUESTION2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What is the real name of American singer P!nk?\n \nA: Joanne Noelle Levesque \nB: Stefani Angeline Germanotta \nC: Eliabeth Woodridge Grant \nD: Alecia Beth Moore\n")
    r4a2 = input("\nAnswer: ")
    if r4a2 == "D" or r4a2 == "d":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
  
    else:
        cash -= 10000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)
    print("\033[H\033[J")
    # Question 3
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What is William Shakespeare's shortest play?\n \nA: Romeo & Juliet \nB: Hamlet \nC: The Comedy of Errors \nD: Macbeth\n")
    r4a3 = input("\nAnswer: ")
    if r4a3 == "C" or r4a3 == "c":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    else:
        cash -= 10000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)
    print("\033[H\033[J")
    #QUESTION4
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("What year was the World Wide Web released for public use?\n \nA: 1987 \nB: 1989 \nC: 1991 \nD: 1993\n")
    r4a4 = input("\nAnswer: ")
    if r4a4 == "B" or r4a4 == "b":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    else:
        cash -= 10000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
        print_slow(random.choice(nq))
    time.sleep(2)
    print("\033[H\033[J")
    #QUESTION5
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("The Kaliningrad Oblast borders which body of water?\n \nA: Gulf of Mexico \nB: Gulf of Aden \nC: Baltic Sea \nD: Meditarranean Sea\n")
    r4a5 = input("\nAnswer: ")
    if r4a5 == "C" or r4a5 == "c":
        print_slow(random.choice(right))
        print_slow(f"\nTotal: £{cash}\n")
    else:
        cash -= 10000
        print_slow(random.choice(wrong))
        print_slow(f"\nTotal: £{cash}\n")
    time.sleep(2)

def quiz_5():
    correct = int(0)
    incorrect = int(0)  
    global cash
   
    round = "Round One"
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round One!
    Which two symbols adorned the flag of the Soviet Union?
    A = Scythe and Hammer 
    B = Hammer and Sickle 
    C = Hammer and Axe 
    D = Axe and Arrow
    \n""")
    r1q1 = input("Answer: ")
    if r1q1 == "b" or r1q1 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Vanessa Carlton became a one-hit wonder for which 2001 song? 
    A = 500 Miles 
    B = A Thousand Miles 
    C = 8 Mile 
    D = One More Mile\n""")
    r1q2 = input("Answer: ")
    if r1q2 == "b" or r1q2 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! Next question...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""In the NATO phonetic alphabet, what word represents the letter 'O'? 
    A = Oscar 
    B = Oliver 
    C = Omega
    D = Octopus
    \n""")
    r1q3 = input("Answer: ")
    if r1q3 == "a" or r1q3 == "A":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! Next question...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What does a Geiger counter measure? 
    A = Earthquakes\n 
    B = Temperature\n
    C = Distance \n
    D = Radiation\n""")
    r1q4 = input("Answer: ")
    if r1q4 == "d" or r1q4 == "D":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! Next question...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("Which of these is NOT a continent? A: North America B: Antarctic C: Australia D: Africa \n")
    r1q5 = input("Answer: ")
    if r1q5 == "b" or r1q5 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! Next question...\n")
    else:
        incorrect += 1
        cash -= 1000
        print_slow(f"Wrong! You have £{cash} remaining.\n Next question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    print_slow("""
    Well done on completing the first round!
    Looks like you might be a bit of a whiz kid, huh?
    Let's keep that energy up in Round 2
    """)
    time.sleep(2)
    print("\033[H\033[J")

    ####### ROUND 2 ########
    round = "Round 2"
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""In which year did the Russia Revolution first start to take place?
    A = 1917 
    B = 1918 
    C = 1921 
    D = 1923\n""")
    r2q1 = input("Answer: ")
    if r2q1 == "a" or r2q1 == "A":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What is David Bowie's real surname?
    A = Micheals 
    B = Peters 
    C = Williams 
    D = Jones \n""")
    r2q2 = input("Answer: ")
    if r2q2 == "d" or r2q2 == "D":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Charles Dickens wrote A Tale of Two Cities. What are the 2 cities? 
    A = Milan and Paris 
    B = London and Paris 
    C = Liverpool and Paris 
    D = Rome and Paris
    \n""") 
    r2q3 = input("Answer: ")
    if r2q3 == "b" or r2q3 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""What is Elon Musk's aerospace company called? 
    A = Virgin Atlantic 
    B = Tesla 
    C = NASA 
    D = Spacex?\n""")
    r2q4 = input("Answer: ")
    if r2q4 == "d" or r2q4 == "D":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Which American state is named after an English monarch? 
    A = Georgia 
    B = Virginia 
    C = Louisiana 
    D = Pennsylvania \n""")
    r2q5 = input("Answer: ")
    if r2q5 == "b" or r2q5 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 3000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    
    print_slow("""
    Looks like you've risen to the challenge and managed to keep
    that cash nicely topped up
    Let's see if you're able to continue it 
    in Round 3\n""")
    time.sleep(2)
    print("\033[H\033[J")

    ################# Round 3 ##############
    round = "Round 3"
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round 3! 
    Sir Walter Raleigh, a favourite of Elizabeth I, notoriously introduced tobacco to England - but which monarch ordered his execution?
    A = Mary I 
    B = Elizabeth I 
    C = James I 
    D = Charles II​ \n """)
    r3q1 = input("Answer: ")
    if r3q1 == "c" or r3q1 == "C":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round 3!
    What is the name of Parmore’s debut album?
    A = Riot! 
    B = Paramore 
    C = All We Know is Falling 
    D = Brand New Eyes \n""")
    r3q2 = input("Answer: ")
    if r3q2 == "c" or r3q2 == "C":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round 3!
    Which gas is the most found in abundance in the Earth's atmosphere? 
    A = Oxygen 
    B = Nitrogen 
    C = Carbon dioxide
    D =  Hydrogen
    \n""")
    r3q3 = input("Answer: ")
    if r3q3 == "b" or r3q3 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round 3!
    What Company did Elon musk found? 
    A = Virgin Atlantic 
    B = Tesla 
    C = NASA 
    D = Spacex \n""")
    r3q4 = input("Answer: ")
    if r3q4 == "b" or r3q4 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    2

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round 3!
    How many countries sit along the Equator? 
    A: 16 
    B: 12 
    C: 9 
    D: 13\n""")
    r3q5 = input("Answer: ")
    if r3q5 == "d" or r3q5 == "D":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 5000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")

    print_slow(f"""
    Things getting a bit tricky now, eh?
    Well you've made your way to the final round
    Remember, wrong answers cost you $10,000 here so tread carefully!
    Good luck, and Godspeed
    """)
    time.sleep(2)
    print("\033[H\033[J")

    ################# Round 4 ##################
    round = "Round 4"
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round Four!
    In 1066, who did William of Normandy defeat to claim the English throne? 
    A = Harold of Sweden 
    B = King Alfred 
    C = Harold Godwineson 
    D = Henry VI of Germany\n""")
    r4q1= input("Answer: ")
    if r4q1 == "c" or r4q1 == "C":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round 4! 
    Including streaming figures, what was the best-selling UK single of the 2010s?
    A = Uptown Funk - Bruno Mars 
    B = Thinkin Out Loud - Ed Sheeran 
    C = Shape Of You - Ed Sheeran 
    D = Despacito - Justin Bieber
    \n""")
    r4q2= input("Answer: ")
    if r4q2 == "c" or r4q2 == "C":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    2

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round 4!
    In chess, which piece cannot move in a straight line?
    A = Knight 
    B = Bishop 
    C = Pawn 
    D = The King
    \n""")
    r4q3= input("Answer: ")
    if r4q3 == "a" or r4q3 == "A":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    

    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round 4!
    In which decade was the Sony Walkman launched? 
    A = 1960s 
    B = 1970s 
    C = 1980s 
    D = 1990s
    \n""")
    r4q4= input("Answer: ")
    if r4q4 == "b" or r4q4 == "B":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    2
    print(f"{round}---------------------------------------------------------------------------------------£{cash}\n")
    print_slow("""Round 4!
    In which Japanese city would you find the Yodo and Dojima rivers?
    A = Osaka 
    B = Tokyo 
    C = Kyoto 
    D = Nagoya\n""")
    r4q5= input("Answer: ")
    if r4q5 == "a" or r4q5 == "A":
        correct += 1    
        print_slow(f"Correct You have £{cash} remaining! \nNext question...\n")
    else:
        incorrect += 1
        cash -= 10000
        print_slow(f"Wrong! You have £{cash} remaining.\nNext question...\n")
    time.sleep(2)
    print("\033[H\033[J")
    
list = [quiz_1, quiz_2, quiz_3, quiz_4, quiz_5]
random.choice(list)()

def wc1():
    print_slow("""What was the name of Tool's first studio album.
        A. Opiate
        B. 10,000 days
        C. Lateralus
        D. Fear innoculum""") 
   
    ans_one = input("\nAnswer:")
    if ans_one == "A" or ans_one == "a":
        print_slow("That is.......THE CORRECT ANSWER, congratulations!")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow(f"{name}, you've now doubled your cash prize - how fantastic!")
        time.sleep(2)
        print("\033[H\033[J")
    else:
        print_slow(f"I'm sorry {name} but that is the wrong answer")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow("You gambled it all and lost, but hey, you tried your best")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow(f"Better luck next time {name}!")
        time.sleep(2)
        print("\033[H\033[J")
        
def wc2():
    print_slow("""After World War Two, when did military conscription in the UK end?
        A. 1962 
        B. 1960 
        C. 1957 
        D. 1955""")
    ans_two = input("\nAnswer:  ")
    if ans_two == "B" or ans_two == "b":
        print_slow("That is.......THE CORRECT ANSWER, congratulations!")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow(f"{name}, you've now doubled your cash prize to an amazing - how fantastic!")
        time.sleep(2)
        print("\033[H\033[J")
    else:
        print_slow(f"I'm sorry {name} but that is the wrong answer")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow("You gambled it all and lost, but hey, you tried your best")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow(f"Better luck next time {name}!")
        time.sleep(2)
        print("\033[H\033[J")
def wc3():
    print_slow("""Where is the oldest tree in the world?
        A. India
        B. Switzerland
        c. Africa
        D. California\n""")
    ans_three = input("Answer: ")
    if ans_three == "D" or ans_three == "d":
        print_slow("That is.......THE CORRECT ANSWER, congratulations!")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow(f"{name}, you've now doubled your cash prize to an amazing - how fantastic!")
        time.sleep(2)
        print("\033[H\033[J")
    else:
        print_slow(f"I'm sorry {name} but that is the wrong answer")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow("You gambled it all and lost, but hey, you tried your best")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow(f"Better luck next time {name}!")
        time.sleep(2)
        print("\033[H\033[J")
def wc4():
    print_slow("""What famous landmark is situated at Latitude: 27°10'30.2"N, Longitude: 78°02'31.6"E?
        A. Statute of Liberty
        B. Taj Mahal
        C. Eiffel Tower
        D. St Paul's Cathedral\n""") 
    ans_four = input("Answer:  ")
    if ans_four == "B" or ans_four == "b":
        print_slow("That is.......THE CORRECT ANSWER, congratulations!")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow(f"{name}, you've now doubled your cash prize to an amazing - how fantastic!")
        time.sleep(2)
        print("\033[H\033[J")
    else:
        print_slow(f"I'm sorry {name} but that is the wrong answer")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow("You gambled it all and lost, but hey, you tried your best")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow(f"Better luck next time {name}!")
        time.sleep(2)
        print("\033[H\033[J")
def wc5():
    print_slow("""How many computer languages are in use?
        A. 2000
        B. 5000
        C. 50
        D. 20\n""")
    ans_five = input("Answer:  ")
    if ans_five == "A" or ans_five == "a":
        print_slow("That is.......THE CORRECT ANSWER, congratulations!")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow(f"{name}, you've now doubled your cash prize to an amazing - how fantastic!")
        time.sleep(2)
        print("\033[H\033[J")
    else:
        print_slow(f"I'm sorry {name} but that is the wrong answer")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow("You gambled it all and lost, but hey, you tried your best")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow(f"Better luck next time {name}!")
        time.sleep(2)
        print("\033[H\033[J")



questions = [wc1, wc2 , wc3, wc4, wc5]

def wc_round():
    print_slow("""Congratulations on making it to the end!
    However, we have one more little surprise up our sleeve""")
    time.sleep(1)
    print("\033[H\033[J")
    print_slow("""You've managed to bag yourself a healthy chunk of cash,
    but could we tempt you to gamble to get more?""")
    time.sleep(1)
    print("\033[H\033[J")
    print_slow("""You have the opportunity now whether to answer one wildcard question.
    If you answer correctly then you will have DOUBLED your cash prize!
    """)
    time.sleep(1)
    print("\033[H\033[J")
    print_slow("""But if you answer incorrect you will LOSE the cash you have gathered so far and 
    go home without a penny""")
    time.sleep(1)
    print("\033[H\033[J")
    print_slow(f"So {name}, are you going to risk it?")
    wc = input("Y or N? ")
    if wc == "Y" or wc == "y":
        print_slow("""Brave one, let's hope it all works out
        Here's your wildcard question...""")
        time.sleep(2)
        print("\033[H\033[J")
        random.choice(questions)()
    else:
        print_slow("""Some things are worth keeping safe -name-,
        We wish you the best luck and don't go spending your money all at once ;)""")
        time.sleep(2)
        print("\033[H\033[J") 

def failed_quiz():
    if cash < 0 or cash == 0:
        print_slow("""So after battling yoru way through the rounds,
        it looks like you haven't managed to save any of that cash prize""")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow("That means you're going home empty handed :(")
        time.sleep(2)
        print("\033[H\033[J")
        print_slow("""Ah well...
        You could always try again...but for now, goodbye!""")
    else:
        wc_round()
failed_quiz()
print("\033[H\033[J")
   
print("				THANKS 4 PLAYING			")
time.sleep(3)
print("\033[H\033[J")
