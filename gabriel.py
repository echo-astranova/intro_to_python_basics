# loops
# print odd numbers only
for i in range(10):
    # check which are even
    if i % 2 == 0:
        continue
    else: # odd
        print(i)


is_player_alive = True
player_health_level = 10
while is_player_alive:
    print("game is doing normal stuff")
    # some game stuff happened, player hurt
    player_health_level -= 2
    if player_health_level <= 0:
        is_player_alive = False
    if not is_player_alive:
        print("game over")
        # end the loop
        break

    # continue
    
        