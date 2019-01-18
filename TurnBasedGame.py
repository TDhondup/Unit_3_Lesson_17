import time
import random

print()
print('-'*65)
print()

print('A wild Wartortle appears!')
time.sleep(0.6)
print('...the background music changes...')
time.sleep(0.6)
print('You only have one Pokémon, Leekbird!')
time.sleep(0.6)
print('I choose you Leekbird!!!')
time.sleep(0.6)
print()

#set the starting health values
leekbird_hp = 150
wartortle_hp = 150

print('Starting HP:')
time.sleep(0.2)
print('Leekbird HP: ' + str(leekbird_hp))
time.sleep(0.2)
print('Wartortle HP: ' + str(wartortle_hp))
time.sleep(0.2)
print()

#this is the battle loop, continues as long as one pokemon is alive
while leekbird_hp > 0 and wartortle_hp > 0:

	print('What will Leekbird do?')
	time.sleep(0.6)
	print('- [1] Tackle 👊')

	print('- [2] Super Screech ')

	print('- [3] Roost ❤️')

	print('- [4] Capture')

	print('- [5] Run Away')

	print()

	player_move = input('Pick a move using the corresponding number: ')
	player_move = int(player_move)
	if player_move == 1:
		wartortle_hp = wartortle_hp - 25
		print('Leekbird uses Tackle and deals 25 HP of damage!')

	elif player_move == 2:
		damage = random.randint(5, 40)
		wartortle_hp = wartortle_hp - damage
		print('Leekbird uses Super Screech and deals ' + str(damage) + ' HP of damage!')

	elif player_move == 3:
		leekbird_hp = leekbird_hp + 100
		print('Leekbird uses Roost and recovers 100 HP!')




	elif player_move == 4:
		capture_roll = random.randint(0, 170)
		if capture_roll > wartortle_hp:
			print('You have captured Wartortle!')
			break
		else:
			print('You tried to capture Wartortle but failed.')

	elif player_move == 5:
		runaway_chance = random.randint(1,2)
		if runaway_chance == 1:
			print('You have successfully run away!')
			break

		elif runaway_chance == 2:
			print('You tried to run, but failed!')



	time.sleep(0.6)
	print()

	#enemy battle choices
	enemy_move = random.randint(1,2)
	if enemy_move == 1:
		leekbird_hp = leekbird_hp - 30
		print('Wartortle uses Water Blast 💦 and deals 30 HP of damage!')

	elif enemy_move == 2:
		leekbird_hp = leekbird_hp - 20
		wartortle_hp = wartortle_hp + 20
		print('Wartortle uses Drink Blood 💉 and deals 20 HP of damage while also recovering 20 HP of health!')

	time.sleep(0.6)
	print()

	#check and avoid negative HP

	if leekbird_hp < 0:
		leekbird_hp = 0

	if wartortle_hp < 0:
		wartortle_hp = 0

	#display current health
	print('Updated HP: ')
	time.sleep(0.2)
	print('Leekbird HP: ' + str(leekbird_hp))
	time.sleep(0.2)
	print('Wartortle HP: ' + str(wartortle_hp))
	time.sleep(0.2)

#check who won!

if leekbird_hp > 0 and wartortle_hp == 0:
	print('Wild wartortle has fainted, Leekbird wins!')
	time.sleep(0.3)

if leekbird_hp == 0 and wartortle_hp > 0:
	print('Leekbird has fainted, wild wartortle wins!')
	time.sleep(0.3)
	print('You have no remaining Pokémon, you lose.')





