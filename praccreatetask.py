move_list = ["punch", "kick", "block"]
print("This is a two player fighting game! The first one to 5 points wins, good luck!")
def playGame():
    p1_score = 0
    p2_score = 0
    for x in move_list:
        user_action = input("Player one, please pick a move you'd like to use!(kick,punch,block)")
        user_action2 = input("Player two, please pick a move you'd like to use!(kick,punch,block)")
        print("Player one picked " + user_action + ", Player two picked " + user_action2)
        if user_action == user_action2:            
            print("It's a tie!")
        elif user_action == "punch":
            if user_action2 == "block":
                print("Player two blocked the punch!")
                p2_score = p2_score + 1
            else:
                print("Both players attacked!")
        elif user_action == "kick":
            if user_action2 == "punch":
                print("Both players attacked!")
            else:
                print("Player two blocked the kick!")
                p2_score = p2_score + 1
        elif user_action == "block":
            if user_action2 == "kick":
                print("Player one blocked the kick!")
                p1_score = p1_score + 1
            else:
                print("Player one blocked the punch!")
                p1_score = p1_score + 1 
        print( "P1: " + str(p1_score), "P2: " + str(p2_score))
        if p1_score == 5 or p2_score == 5:
            print("thanks for playing!")
        else: 
            continue
    print(x)
    


playGame()