#!/usr/bin/env python
import random
import re
import argparse
import math
import os
import signal
seed_bytes = 2048
random.seed(os.urandom(seed_bytes))

# Add CLI flag parser
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--debug", help="Enable debug mode", action="store_true")
parser.add_argument("-i", "--interactive", help="Enable interactive mode, return to the DiceCode entry on finish", action="store_true")
parser.add_argument("-sr", "--statroll", help="Do a stat roll (4d6r1k3)", action="store_true")
parser.add_argument("-d", "--dicecode", help="Specify dicecode at launch (Example=dice.py --dicecode 4d20+69")
parser.add_argument("-q", "--quiet", help="Don't display the induvidual dice rolls, only the total.", action="store_true")
args = parser.parse_args()
# STAT ROLL 4d6r1k3
if args.statroll == True:
	for x in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
		d = []
		d.append(random.randint(2, 6)) 
		d.append(random.randint(2, 6)) 
		d.append(random.randint(2, 6)) 
		d.append(random.randint(2, 6)) 
		if args.debug == True:
			print('Rolls: \n' + str(d))
		d.remove(min(d))
		dsum = int(sum(d)) 
		mod = math.floor((dsum - 10) / 2)
		print(x + ': ' + str(sum(d)) + '\nMod: ' + str(mod) + '\n')
		
	exit()
def RollTheDice():
	if args.dicecode:
		dicecode = args.dicecode
	else:
		dicecode = input('Enter dice code: ')
	
	# DEBUG STUFFz
	if args.debug == True:
		print('DiceCode before alteration: ' + dicecode)
	
	# Check if first character is a number, if not, prefix dicecode with "1" to only roll one dice
	if dicecode[0].isdigit() == False : 
		dicecode = '1' + dicecode
	
	# DEBUG STUFFz
	if args.debug == True:
		print('DiceCode after alteration: ' + dicecode)
	
	snumdice = re.match(r'^\d+', dicecode)
	
	# DEBUG STUFFz
	if args.debug == True:
		print('Number of dice to roll: '+snumdice.group(0))
	
	# Get dice value to roll
	sdiceval = re.search('(?<=d)\d+', dicecode)
	
	# Covert to int
	diceval = int(sdiceval.group())
	numdice = int(snumdice.group())
	
	# DEBUG STUFFz
	if args.debug == True:
		print('Dice value to roll: '+sdiceval.group())
	
	# Reset dice array
	dicearray = []
	for x in range(0, numdice):
		dicearray.append(random.randint(1, diceval))
	
	if 'r' in dicecode:
		sdicereroll = re.search('(?<=r)\d+', dicecode)
		dicereroll = int(sdicereroll.group())
		if dicereroll >= diceval:
			print('r cant >= d value, wtf dude?')
			exit()
	
		if args.debug == True:
			print('DiceArray before rerolls: ' + str(dicearray))
			print('Reroll all rolls that equal/is lower than: ' + sdicereroll.group())
	
		while min(dicearray) <= dicereroll:
			dicearray.remove(min(dicearray))
			dicearray.append(random.randint(dicereroll+1, diceval))
		if args.debug == True:
			print('DiceArray after rerolling: ' + str(dicearray))	
	else:	
		if args.debug == True:
			print('r not specified, skipping...')
	if 'k' in dicecode:
		sdicekeep = re.search('(?<=k)\d+', dicecode)
		dicekeep = int(sdicekeep.group())
		if dicekeep >= numdice:
			print('k cant >= ammount of dice to roll, wtf dude?')
			exit()
	
		if args.debug == True:
			print('Keep this many dice after roll: ' + sdicekeep.group())
		while len(dicearray) > dicekeep:
			if args.debug == True:
				print('DiceArray before removing all but the '+str(dicekeep)+' highest dice: '+str(dicearray))
				print('Array length: ' + str(len(dicearray)))
			dicearray.remove(min(dicearray))
	
		if args.debug == True:
			print('After keeping highest ' + str(dicekeep) + ': ' + str(dicearray))
	else:	
		if args.debug == True:
			print('k not specified, skipping...')
		
	if '+' in dicecode:
		sdiceplus = re.search('(?<=\+)\d+', dicecode)
		diceplus = int(sdiceplus.group())
		print('Modifier: +' + sdiceplus.group())	
		if args.quiet != True:
			print('Dice Rolls: '+ str(dicearray))	
		print('Total: ' + str(sum(dicearray) + diceplus) + '\n')
	elif '-' in dicecode:
		sdiceminus = re.search('(?<=\-)\d+', dicecode)
		diceminus = int(sdiceminus.group())
		print('Modifier: -' + sdiceminus.group())	
		if args.quiet != True:
			print('Dice Rolls: '+ str(dicearray))	
		print('Total: ' + str(sum(dicearray) - diceminus) + '\n')
	else:
		if args.quiet != True:
			print('Dice Rolls: '+ str(dicearray))	
		print('Total: ' + str(sum(dicearray)) + '\n')
	return;
try:
	if args.interactive:
		while (True):
			RollTheDice()
	else:
		RollTheDice()
except KeyboardInterrupt:
	print("\nBye!")
finally:
	exit()
