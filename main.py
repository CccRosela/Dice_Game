# main logic (functions will be added at a later point
# will make 3 classes -> character, and 2 job classes (warrior, sage)
# goal is to do 20 explorations to reach the end of the game
def main():
  player = create_player() # needs to be done

  while player.is_alive() and explorations < 20:  # player.is_alive(), a character class function
   # event happens 
    explorations += 1
    pass

  if player.is_alive():P
    epilogue_alive(player)
  else:
    epilogue_dead(player)

if __name__ == "__main__":
  main()
