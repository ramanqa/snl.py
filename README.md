# Setup #
`$> pip install PyYAML`


# RULES #
1. Max 4 players
2. First join first turn
3. Players can only join before a game starts
4. Start position is 0
5. Game starts when 1st player rolls dice (calls play_turn method)
6. Game ends when one player reaches position 50
7. First player to reach position 50 is winner

# GAME API #
## Start Game ##
`game = Game()`

## Join Player ##
`player_id = game.join("PLAYER_NAME")`

## Play Turn ##
`game_state_json = game.play_turn(player_id)`
 - returns game state in JSON string if successful turn
 - throws excpetion if 
  1. player does not have turn
  2. game has ended



