#========================================
#Project Name: Room Type/Size
#Project Description: Tape Interface
#Date:	01/6/2018
#Programmer Name: Team Fire / Falkors
#========================================

import time
from UltrasonicSensor import UltrasonicSensor
from DB import DB
from Room import Room, Circle, Rectangle

#User validation
#Creates new DB User

def user():
	global db
	global arm_length
	username = input("Please enter your username:\n")
	
	checkUser = db.check_user(username)
	if checkUser == False:
		arm_length = input("Enter arm length from shoulder to wrist in centimeters:\n")
		arm_length = int(arm_length)
		UID = db.add_user(username, arm_length)
	else:
		UID = db.add_user(username)
		
	intial_rm(UID)

#resets global counter to zero
#establishes bldg and floor and updates db
def intial_rm(UID):
	global db
	#global counter
	#counter = 0
	HIDs = db.get_HIDs(UID)
	if not HIDs:
		HID = db.add_house(UID)
	else:
		i = input("You have {} Buildings, select one or enter 'n' to create a new house:\n".format(len(HIDs)))
		if i.lower() == "n":
			HID = db.add_house(UID)
		else:
			HID = HIDs[int(i) - 1]
	print("Basements are consider floor 0 and negative numbers for sub-basements and ground floor is equal to 1.")
	level = input("Please enter the floor number you want to edit:\n")
	
	FID = db.add_floor(HID, level)

	#room_count()
	room(FID)

#creates a room counter
#def room_count():
	#global counter 
	#counter += 1
	#room()

# declares room types
def room(FID):
	rm_type = input("Please enter 0 for circular room or 1 for rectangular room:\n")
	if rm_type == "0":
		room = rm_type_0()
	else:
		room = rm_type_1()
	db.add_room(room, FID)
	
	con()

#round room measuring tool
#grabs 2 data points using ultrasonic sensor and updates db table
def rm_type_0():
	global us
	global arm_length
	print("Please go to at or near the center of the room")
	print(" For all measurements please FIRST confirm the measurement then aim and wait 5 seconds.")
	input("Hit enter to take the initiate the measurement")
	time.sleep(2)
	a = us.getUltrasonicDistance()
	print(str(a) + " cm")
	print("Please turn 180 degrees and take another measurement")
	input("Hit enter to take the initiate the measurement")
	time.sleep(2)
	b = us.getUltrasonicDistance()
	print(str(b) + " cm")
	radius = (a + b + 2 * arm_length)/2

	name = input("Please enter room name")
	circ = Circle(radius, name)
	return circ
			
# rectangular room measuring tool
#grabs 4 data points using ultrasonic sensor and updates db table
def rm_type_1():
	global us
	global arm_length
	msr = []
	print(" For all measurements please FIRST confirm the measurement then aim and wait 5 seconds. ")
	input("Hit enter to take the initiate the measurement")
	time.sleep(2)
	a = us.getUltrasonicDistance()
	print(str(a) + " CM")
	msr.append(a)
	for i in range(3):	
		print("Please turn right 90 degrees and take another measurement.")
		input("Hit enter to take the initiate the measurement")
		time.sleep(2)
		b = us.getUltrasonicDistance()
		print(str(b) + " cm")
		msr.append(b)
		
	length = msr[0] + msr[2] + 2 * arm_length
	width = msr[1] + msr[3] + 2 * arm_length
	
	name = input("Please enter room name")
	
	rec = Rectangle(width, length, name)
	return rec

#continuation sequence for rooms and new buildings/floors
def con(): 
	q1 = input("Do you want to measure another room? (Y/N)")
	if q1 == "Y" or "y" or "Yes" or "yes":
		room(FID)
	else:
		q2 = input("Do you want to measure another building or floor? (Y/N)")
		if q2 == "Y" or "y" or "Yes" or "yes":
			intial_rm()
		else:
			print("Have a great day!")
			exit()

#main function			
def main():
	print("Welcome to WristTape!")
	user()

#inits main	
if __name__ == "__main__":
	counter = 0
	us = UltrasonicSensor()
	db = DB()
	arm_length = 0
	main()




