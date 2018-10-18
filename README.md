# LabGame

Welcome! ![alt text](https://static-cdn.jtvnw.net/emoticons/v1/425618/1.0 "LuL")

# Controls
Key | Action
--- | ---
`W` | Move forward
`S` | Move backward
`A` | Turn left
`D` | Turn right
`F` | Attack
`R` | Wait
`E` | Exit
`0` | Developer console

# Console commands
## Player commands
Command | Effect
--- | ---
`player hp <playerid> <amount>` | Sets the players health points
`player tp <playerid> <x> <y>` | Teleports the player to given cordinates
`player face <playerid> <0-3>` | Turns the player towards the given direction (0 - up, 1 - right, 2 - down, 3 - left)

## Enemy commands
Command | Effect
--- | ---
`enemy spawn <x> <y> <0-3> <health> <hearing range>` | Spawns an enemy with given parameters

## Display commands
Command | Effect
--- | ---
`devmap <0-2>` | Switch between map display modes
`printerr <msg>` | Prints given error message
