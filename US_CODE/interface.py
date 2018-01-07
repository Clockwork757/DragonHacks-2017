#========================================
#Project Name: Room Type/Size
#Project Description: Tape Interface
#Date:	01/6/2018
#Programmer Name: Team Fire / Falkors
#========================================

import time
from UltrasonicSensor import UltrasonicSensor
from DB import DB

#User validation
#Creates new DB User

def user():
	username = input("Please enter your username")
	
	checkUser = db.checkUser()
	if checkUser == False:
		#	insert username into database
			arm_length = input("Enter arm length from shoulder to wrist in centimeters:")
		#	insert arm_length into databasee
		intial_rm()
	else:
		intial_rm()

#resets global counter to zero
#establishes bldg and floor and updates db
def intial_rm():
	global counter
	counter = 0
	bldg = input("Please enter the building number")
	# insert bldg # into DB
	print "Basements are consider floor 0 and negative numbers for sub-basements and ground floor is equal to 1."
	floor = input("Please enter the floor number")
	#insert floor# into DB
	room_count()

#creates a room counter
def room_count():
	global counter 
	counter += 1
	room()

# declares room types
def room():
	rm_type = input("Please enter 0 for circular room or 1 for rectangular room")
	if rm_type == "0":
		rm_type_0()
	else:
		rm_type_1()

#round room measuring tool
#grabs 2 data points using ultrasonic sensor and updates db table
def rm_type_0():
	print "Please go to at or near the center of the room"
	print " For all measurements please FIRST confirm the measurement then aim and wait 5 seconds. "
	input("Hit enter to take the initiate the measurement")
	time.sleep(2)
	a = us.getUltraSonicDistance()
	print a + " cm"
	print "Please turn 180 degrees and take another measurement"
	input("Hit enter to take the initiate the measurement")
	time.sleep(2)
	b = getUltraSonicDistance()
	print b + " cm"
	radius = (a + b + 2 * arm_length)/2

	#input sequel code for saving data

	con()
			
# rectangular room measuring tool
#grabs 4 data points using ultrasonic sensor and updates db table
def rm_type_1():
	msr = []
	print " For all measurements please FIRST confirm the measurement then aim and wait 5 seconds. "
	input("Hit enter to take the intiate the measurement")
	time.sleep(2)
	a = us.getUltraSonicDistance()
	print a + " CM"
	msr.append(a)
	for i in range(4):	
		print "Please turn right 90 degrees and take another measurement"
		input("Hit enter to take the intiate the measurement")
		time.sleep(2)
		b = us.getUltraSonicDistance()
		print b + " cm"
		msr.append(b)
		
	length = msr[0] + msr[2] + 2 * arm_length
	width = msr[1] + msr[3] + 2 * arm_length

	#input data into DB sql cmd
		
	con()

#continuation sequence for rooms and new buildings/floors
def con() 
	q1 = input("Do you want to measure another room? (Y/N)")
	if q1 == "Y" or "y" or "Yes" or "yes":
		room_count()
	else:
		q2 = input("Do you want to measure another building or floor? (Y/N)")
		if q2 == "Y" or "y" or "Yes" or "yes":
			intial_rm()
		else:
			print "Have a great day!"
			exit()

#main function			
def main():
	print "Welcome to WristTape!"
	user()

#inits main	
if __name__ == "__main__":
	counter = 0
	us = UltrasonicSensor()
	db = DB()
	main()




