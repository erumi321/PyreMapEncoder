# PyreMapPacker
A tool to pack JSON into binaries used by Pyre when loading maps

# What is this?
This is a tool to pack JSON into a usable binary format read by Pyre when the game loads a map. 

# How to use this?
The script by default reads from a file in the same location as it named <code>input.thing_text</code>. It outputs to <code>output.thing_bin</code> by default. The input file must be formatted like:
```
{
  "Obstacles": [
    {...},
    {...},
    ...
  ]
}
```
To see the fields and formats of obstacles it's advised to look at the original "JSON" (they aren't true JSON as the formatting is a little off) to see how obstacles are created.

# Putting it in Game
Copy your output.thing_bin into Pyre's <code>Content/Win/Maps</code> folder, and name it the same as your in code map name. Run the game and load the map; you should see the changes in-game.
