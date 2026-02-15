def health_range(Current_health):
    return(Current_health + 4) - 6

def current_turn(Turn):
    return(Turn)

Current_health = 102
Turn = 0

while Turn < 100 and Current_health >= 2:
   
    print(f"Turn: {current_turn(Turn)} | Health: {health_range(Current_health)}")
    Turn += 1
    Current_health -= 2

print("Game Over!")





    



    





















