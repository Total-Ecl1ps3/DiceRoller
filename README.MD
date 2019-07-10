# DiceRoller
___
```
Written by Magnus "Total_Ecl1ps3" K. K.
```
___
### What is this?
This is a simple dice roller for DnD written in python.  
It accepts Standard dice notation (i.e. `4d6r1k3`), and converts this into a dice roll.  
___
### How do i use it?
It's pretty simple, just start the program with `./dice.py` and type in your roll in standard dice notation, then watch as the program spits out your roll! 
#### Example:
```
[total_ecl1ps3@potato ~]$ ./dice.py 
Enter dice code: 1d6+4
Modifier: +4
Dice Rolls: [6]
Total: 10
```
___
### What else does it do?
It can roll stats for you, and calculate your modifier based on the roll!  
#### Example:
```
[total_ecl1ps3@potato ~]$ ./dice.py -sr
Strength: 16
Mod: 3

Dexterity: 12
Mod: 1

Constitution: 14
Mod: 2

Intelligence: 12
Mod: 1

Wisdom: 14
Mod: 2

Charisma: 11
Mod: 0
```
___
### Supported flags w/ examples
`-i` / `--interactive` - Start DiceRoller in interactive mode, so you can keep entering DiceCodes without having to re-run the program! (Exit with CTRL+C)
```
[total_ecl1ps3@potato ~]$ ./dice.py -i
Enter dice code: 1d20+4
Modifier: +4
Dice Rolls: [19]
Total: 23

Enter dice code: 2d80-20
Modifier: -20
Dice Rolls: [46, 7]
Total: 33

Enter dice code: 2d1-10
Modifier: -10
Dice Rolls: [1, 1]
Total: -8

Enter dice code: ^C
Bye!

```
___
`-d` / `--dicecode` - Define the dicecode/standard dice notation at launch
```
[total_ecl1ps3@potato ~]$ ./dice.py -d 8d20+4
Modifier: 4
Dice Rolls: [12, 10, 1, 8, 3, 11, 3, 17]
Total: 69
```
___
`-v` / `--debug` - Get verbose (debug) output, perfect for when you're wondering why your roll was so high or low!  
```
[total_ecl1ps3@potato ~]$ ./dice.py -v
Enter dice code: 3d20r5k2
DiceCode before alteration: 3d20r5k2
DiceCode after alteration: 3d20r5k2
Number of dice to roll: 3
Dice value to roll: 20
DiceArray before rerolls: [18, 14, 13]
Reroll all rolls that equal/is lower than: 5
DiceArray after rerolling: [18, 14, 13]
Keep this many dice after roll: 2
DiceArray before removing all but the 2 highest dice: [18, 14, 13]
Array length: 3
After keeping highest 2: [18, 14]
Dice Rolls: [18, 14]
Total: 32
```
___

`-sr` / `--staroll` - Roll a set of standard DnD stats, and calculate modifier
```
[total_ecl1ps3@potato ~]$ ./dice.py -sr
Strength: 16
Mod: 3

Dexterity: 12
Mod: 1

Constitution: 14
Mod: 2

Intelligence: 12
Mod: 1

Wisdom: 14
Mod: 2

Charisma: 11
Mod: 0
```

___
`-q` / `--quiet` - Hide the induvidual dice rolls, helpful for those rolls where you roll more than 20-ish dice.  
```
[total_ecl1ps3@potato ~]$ ./dice.py -d 10000d20r10 -q
Total: 154659

```
___
`-h` / `--help` - Get some help! (Print help message)  
```
[total_ecl1ps3@potato ~]$ ./dice.py -h
usage: dice.py [-h] [-v] [-sr] [-d DICECODE]

optional arguments:
  -h, --help            show this help message and exit
  -v, --debug           Enable debug mode
  -sr, --statroll       Do a stat roll (4d6r1k3)
  -d DICECODE, --dicecode DICECODE
                        Specify dicecode at launch (Example=dice.py --dicecode
                        4d20+69

``` 
