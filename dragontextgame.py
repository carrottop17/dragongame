import sys
import random
import time

hero = {
	'health': 50,
	'sword': 5,
	'slingshot': 2
}

dragon = {
	'health': 50,
	'fire': 10
}

def fight():
	weapon = raw_input("Which weapon should you attack with? Sword or Slingshot")
	time.sleep(2)
	if weapon == 'sword':
		attack_number = hero['sword'] * random.randrange(5)
		print "You attacked the dragon with " + str(attack_number) + " sword power!"
		time.sleep(2)
		dragon['health'] = dragon['health'] - attack_number
		if dragon['health'] < 0:
			dragon['health'] = 0
		print "the dragon's health is now " + str(dragon['health'])
		time.sleep(2)
	elif weapon == 'slingshot':
		attack_number = hero['slingshot'] * random.randrange(20)
		print "You attacked the dragon with " + str(attack_number) + " slinghshot power!"
		time.sleep(2)
		dragon['health'] = dragon['health'] - attack_number
		if dragon['health'] < 0:
			dragon['health'] = 0
		print "the dragon's health is now " + str(dragon['health'])
		time.sleep(2)

def dragon_fight():
	print "Now the dragon attacks you!"
	time.sleep(2)
	dragon_attack = dragon['fire'] * random.randrange(5)
	defense = random.randrange(10)
	if defense <= 5:
		defended_amount = random.randrange(10)
		if defended_amount > dragon_attack:
			dragon_attack = 0
			defended_amount = 0
		print "You defended the Dragon's fire attack by " + str(defended_amount) + " amount"
		time.sleep(2)
		dragon_attack = dragon_attack - defended_amount
	print "The dragon attacks you with his " + str(dragon_attack) + " Fire Breath!"
	time.sleep(2)
	hero['health'] = hero['health'] - dragon_attack
	if hero['health'] < 0:
		hero['health'] = 0
	print "Your health is now " + str(hero['health'])
	time.sleep(2)

print "You enter the dungeon and encounter a dragon!"
time.sleep(2)
response = raw_input("Would you like to fight or flee?")
if response == "flee":
	exit = raw_input("Type yes or no")
while response != 'fight':
   if exit != 'no' and  exit != 'yes':
       print "This is not a valid choice!"
       exit = raw_input("Type yes or no")
   elif exit == 'yes':
       print "Get ready to fight!"
       time.sleep(2)
       response = 'fight'
   elif exit == 'no':
       sys.exit()

while hero['health'] > 0 and dragon['health'] > 0:
	fight()
	if dragon['health'] == 0:
		print "Huzzah! You have defeated the dragon! You are showered with riches and titles!"
		time.sleep(2)
	dragon_fight()
	if hero['health'] <= 0:
		print "You are dead! The dragon has won. All is lost!"
		time.sleep(2)
	if dragon['health'] <= 0:
		print "Huzzah! You have defeated the dragon! You are showered with riches and titles!"
		time.sleep(2)


