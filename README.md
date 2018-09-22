# Games

## Installation

0. Symlink (`ln -s`) the `game.sh` file in this directory to a directory of your choice.
    - The target directory must be withing your `$PATH`
    - An empty `install.sh` file is included, which will soon be updated.

## Rules and Gameplay

### Mastermind
- A command-line adaptation of Mastermind, using numbers instead of colors.
- Requirements: [Python 3.6](https://www.anaconda.com/download/)

1. Type `game mastermind` into the command prompt.
2. Add flags if necessary.
    - Select difficulty by typing `-d <num>`, where <num> is an integer 1-9.
    - Optionally clear the screen before playing the game with the flag `-c`.
3. Input a 4-digit number after the `> ` prompt.
4. Every `*` printed after your input represents one correct number in the right place (but
   you won't know which is which).
5. To exit the game, simply type `exit`.

```shell
$ game mastermind -d 0

======================
Welcome to Mastermind!
See README.md for help
Generating random 4-digit number...

Based on your difficulty, there are 1 possible combinations
> 0000
****
Well done! All in all, you took: 1 tries.
======================
```

### Exploder
- "A fun little game where you try to bounce balls till they explode!"
- Requirements: [Beaker Browser](https://beakerbrowser.com/)
    - Opens a `dat` (P2P) website

1. Type `game exploder` into the command prompt.
2. No flags are available at this time.
3. Click and drag to create explosions and set the circles on fire.
