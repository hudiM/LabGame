# LabGame

Welcome! ![alt text](https://static-cdn.jtvnw.net/emoticons/v1/425618/1.0 "LuL")

# Controls
Key | Action
--- | ---
`W` | Move forward
`S` | Move backward
`A` | Move left
`D` | Move right
`F` | Attack
`R` | Wait
`E` | Exit
`0` | Developer console

# Console commands
## Player commands
Command | Effect
--- | ---
`player.hp.<amount>` | Sets the players health points
`player.tp.<x>.<y>` | Teleports the player to given cordinates
`player.face.<0-3>` | Turns the player towards the given direction (0 - up, 1 - right, 2 - down, 3 - left)

## Enemy commands
Command | Effect
--- | ---
`enemy.spawn.<x>.<y>.<0-3>.<health>` | Spawns an enemy with given parameters

## Display commands
Command | Effect
--- | ---
`devmap.<0-2>` | Switch between map display modes
`printerr.<msg>` | Prints given error message
