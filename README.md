# PyreMapEncoder
A tool to pack JSON into binaries used by Pyre when loading maps

# What is this?
This is a tool to pack JSON into a usable binary format read by Pyre when the game loads a map. 

# Installation
Download the latest [Release](https://github.com/erumi321/PyreMapEncoder/releases/). Open command prompt and cd into the directory of the wheel and pip install it, remeber to have .whl at the end of the name.

# How to use this?
From the command line run the command
```
pyre_map_encoder ec
```
The command by default reads from a file in the same location as it's run named <code>input.thing_text</code>. It outputs to <code>output.thing_bin</code> by default. The input file must be formatted like:
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
To change the input path use the arg <code>-i</code> or <code>--input</code> and to hcange the output path use the arg <code>-o</code> or <code>--output</code>

# Putting it in Game
Copy your output file into Pyre's <code>Content/Win/Maps</code> folder, and name it the same as your in code map name. Run the game and load the map; you should see the changes in-game.
