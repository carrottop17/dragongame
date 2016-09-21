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
	elif weapon != 'sword' and weapon != 'slingshot':
		print "This weapon is not a valid choice.  The Dragon takes advantage of your stupidity and attacks for 5 points of Fire Breath"
		hero['health'] = hero['health'] - 5
		print "Your health is now " + str(hero['health'])
		# weapon == raw_input("Type sword or slingshot")
		fight()
   

def dragon_fight():
	print "The dragon attacks you!"
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

def more_power():
	option = raw_input("Would you like to stay alive with a potion?")
	if option == "yes":
		power_up = raw_input("Which potion? Beetlejuice or hotsauce?")
		if power_up == "Beetlejuice":
			hero['health'] = 20
		elif power_up == "hotsauce":
			hero['health'] = 2
		print "Your health is now " + str(hero['health'])
	else:
		print "You are dead! The dragon has won. All is lost!"
		time.sleep(2)


                               
print ("                                        S,  S,                              ")
print ("                                        ss,Sss, ,s                         ")
print ("                                     ,ssSSSSSSSSSSs,                        ")
print ("                                S, sSSSSSSSSSSSSSS`SSSs                      ")
print ("                                 SSSSSSSSSSSSSSSSSSoSSS                     ")
print ("                               sSSSSSSSSSSSSSSSSSSSSSSSSs,  ,s               ")
print ("                              sSSSSSSSSS SSSSSS    SSSSSS SSSSS,             ")
print ("                             sSSSSSSSSSSs  SSSSssssss`SSSSSSSS              ")
print ("                             sSSSSSSSSSS             ss S Ss                ")
print ("                             sSSSSSSSSSS,                   S  ,sSSs        ")
print ("                             sSSSSSSSSSSSSs,,,,                sSS         ")
print ("                             ssssSSSSSSSSSSSSSSSSSSSS@@@@s,     ,SS S,      ")
print ("                             `SSSSSSSSSSSSSSSSSSSSHHHHHSSSSSS`     S,S  ")  
print ("                               `SSSSSSSSSSSSSSSSSSSSSHHHHs``     ,SSS|     ")
print ("                                `SSSSSSSSSSSSSSSSSSSSSSSSHHs    ,SS` S    ")
print ("                                   SS``SSSSSSSSSSSSSSSSSSSSSSSSSSSSS`    ")
print ("                                  SS`  `S`SSSSSSSSSSSSSSSSSSSSS`````         ")
print ("                             ,   ,`        SSSSSSSSSSSSSSSSHHHHs             ")
print ("                             S,          ,sSSSSSSSSSSSSSSSSSHHHH`            ")
print ("                 ,           `Ss,   ,,ssSSSSSSSSSSSSSSSSSSSSHHHH`            ")
print ("                 S           ,SSSSSSSSSSSSSSSSSSSSSSSSSSSSHHHHH`             ")
print ("                 Ss     ,,sSSSSSSSSSSSSSSSSSSSSSSSSSSSSHHHHHH``              ")
print ("                  `SSsSSSSSSSSSSSSSSSSSSSSSSSSSSSSHHHHHHHH`                  ")
print ("           ,      sSSSSSSSSSSSSSSSSSSSSSSSSHHHHHHHHH```                      ")
print ("           S    sSSSSSSSSSSSSSSSSSSSSSHHHHHHH```      s`         ,           ")
print ("           SS,,SSSSSSSSSSSSSSSSSSHHHHHH``       ,,,,,SS,,,,    ,S            ")
print ("            `SSSSSSSSSSSSSSSHHHHHH`` ,     ,sSSSSSSSSSSSSSSSSSsSS            ")
print ("              SSSSSSSSSSSSHHHHH`     S, ,sSSSSSSSSSSSSSSSSSSSSSSSSs,         ")
print ("   )          SSSSSSSSSSSHHHHH`      `SSSSSSSSSHHHHHHHHHHHSSSSSSSSSSS,       ")
print ("  ((          SSSSSSSSSSSHHHHH       SSSSSSSSHHH`       `HHHHSSSSSSSSSS      ")
print ("  ) \         SSSSSSSSSSSSHHHH,     SSSSSSHHH`             `HHHSSSSSSSSS   s`")
print (" (   )        SSSSSSSSSSSSSHHHH,   SSSSSHHH`                HHHHSSSSSSSSsSS` ")
print (" )  ( (       SS`SSSSSSSSSSSHHHHH,SSSSSHHH`                ,HHHSSSSSSSSSS`   ")
print (" (  )  )   _,S`   SSSSSSSSSSSSHHHHHH,SSHH`                ,HHHSSSSSSSSSS     ")
print (" ) (  ( \,         `SSSSSSSSSSSSSHHHHHHH,,,,          ,,HHHHSSSSSSSSSSS`     ")
print ("(   )S )  )        ,SSSSSSSSSSSSSSSSSSHHHHHHHHHHHHHHHHHHHHSSSSSSSSSSS`       ")
print ("(   (SS  ( \     _sS`  ``SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS,       ")
print (" )  )SSSs ) )  ,      ,   `SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS``  `SS      ")
print ("  (   SSSSs/  ,S,    ,S,,sSSSSSSHHSSSSSSSSSSSSSSSSSSSSSSSSSS``              ")
print ("    \)_SSSSSSSSSSSSSSSSSSSSSSSHH`  SS        `SS,        `SS,                ")
print ("          SSSSSSSSSSSSSSSSSSH`      S          S           S                ")


print "You enter the dungeon and encounter a dragon!"
time.sleep(2)
response = raw_input("Would you like to fight or flee?")
if response == "flee":
	exit = raw_input("Type yes or no")
while response != 'fight':
   if exit != 'no' and  exit != 'yes':
       print "This is not a valid choice!"
       exit = raw_input("Type yes or no")
   elif exit == 'no':
       print "Get ready to fight!"
       time.sleep(2)
       response = 'fight'
   elif exit == 'yes':
       sys.exit()

while hero['health'] > 0 and dragon['health'] > 0:
	fight()
	if dragon['health'] == 0:
		print "Huzzah! You have defeated the dragon! You are showered with riches and titles!"
		time.sleep(2)
		break
	dragon_fight()
	if hero['health'] <= 0:
		more_power()
		
	# if dragon['health'] <= 0:
	# 	print "Huzzah! You have defeated the dragon! You are showered with riches and titles!"
	# 	time.sleep(2)

