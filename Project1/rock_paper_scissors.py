import random 
# Major rectification required not working for all cases 
# Problem was with break/return in While True loop

def rock_paper_scissors():
	npc_choices = ["Rock","Paper","Scissors"]
	isPlaying = True
	while isPlaying:
	    print("Choose either Rock,Paper or Scissors!")
	    inp = input("Please Type here : ")
	    victory_msg = "YOU WON!!!"
	    print(inp)
	    if inp not in ["Rock","Paper","Scissors"]:
	        print("Wrong input!!!")
	        rock_paper_scissors()
	    else:
	        npc_choice = random.choice(npc_choices)
	        if npc_choice == "Rock" and inp == "Paper":
	            print(victory_msg)
	        elif npc_choice == "Paper" and inp == "Scissors":
	            print(victory_msg)
	        elif npc_choice == "Scissors" and inp == "Rock":
	            print(victory_msg)
	        elif npc_choice == inp:
	            print(f"You Tied!! The computer also chose {npc_choice}")
	            print("Play again ? ")
	            exit = input("Y/N : ")
	            if exit == "N":
	                print("BYE!")
	                isPlaying = False
	            else:
	                rock_paper_scissors()           
	        else:
	            print(f"You Lost!! The computer chose {npc_choice}")
	            print("Play again ? ")
	            exit = input("Y/N : ")
	            if exit == "N":
	                print("BYE!")
	                isPlaying = False
	            else:
	                rock_paper_scissors()       

rock_paper_scissors()