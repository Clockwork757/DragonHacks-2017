import time
from DB import DB

print "Welcome to WristTape!"

def user():
	username = input("Please enter your username")
	
	checkUser = #input sequel code to check if username exists
	if checkUser == False:
		#	insert username into database
			arm_length = input("Enter arm length from shoulder to wrist in centimeters:")
		#	insert arm_length into database
		tape_interface()
	else:
		tape_interface()

counter = 0
def intial_rm():
	global counter
	rm_count = counter
	bldg = input("Please enter the building number")
	# insert bldg # into DB
	print "Basements are consider floor 0 and negative numbers for sub-basements and ground floor is equal to 1."
	floor = input("Please enter the floor number")
	#insert floor# into DB
	return rm_count & room_count()

def room_count():
	rm_count += 1
	room()


def room():
	rm_type = input("Please enter 0 for circular room or 1 for rectangular room")
	if rm_type == "0":
		rm_type_0()
	else:
		rm_type_1()


def rm_type_0():
		print "Please go to at or near the center of the room"
		print " For all measurements please FIRST confirm the measurement then aim and wait 5 seconds. "
		input("Hit enter to take the intiate the measurement")
		time.sleep(2)
		a = getUltraSonicDistance()
		print a + " cm"
		print "Please turn 180 degrees and take another measurement"
		input("Hit enter to take the intiate the measurement")
		time.sleep(2)
		b = getUltraSonicDistance()
		print b + " cm"
		radius = (a + b + 2 * arm_length)/2

		#input sequel code for saving data

		con = input("Do you want to measure another room? (Y/N)")
		if con == "Y" or "y" or "Yes" or "yes":
			room()

		else:
			exit()
			

def rm_type_1():
		print " For all measurements please FIRST confirm the measurement then aim and wait 5 seconds. "
		input("Hit enter to take the intiate the measurement")
		time.sleep(2)
		a = getUltraSonicDistance()
		print a + " CM"
		print "Please turn right 90 degrees and take another measurement"
		input("Hit enter to take the intiate the measurement")
		time.sleep(2)
		b = getUltraSonicDistance()
		print b + " cm"
		print "Please turn right 90 degrees and take another measurement"
		input("Hit enter to take the intiate the measurement")
		time.sleep(2)
		c = getUltraSonicDistance()
		print c + " cm"
		print "Please turn right 90 degrees and take another measurement"
		input("Hit enter to take the intiate the measurement")
		time.sleep(2)
		d = getUltraSonicDistance()
		print d + " cm"
		
		length = a + c + 2 * arm_length
		width = b + d + 2 * arm_length

		#input data into DB sql cmd

		con = input("Do you want to measure another room? (Y/N)")
		if con == "Y" or "y" or "Yes" or "yes":
			room()
		else:
			exit()
