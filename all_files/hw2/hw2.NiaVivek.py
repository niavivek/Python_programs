
#importing module to prevent display of password
import getpass
#global variable to display message to user about the password
msg_for_user = ""

def prompt_user():
	"""
	Method to prompt user for a password input. It checks for 4 conditions and displays
	the strength of the password.
	"""
	global msg_for_user
	#variable to store input from user
	password_input = ""
	#continue till user types finish
	while(password_input != "finish"):
		#reset value for message
		msg_for_user = ""
		#http://stackoverflow.com/questions/21533539/input-raw-input-echoing-input-as-asterisks
		#this module does not display the input from user
		try:
			password_input = getpass.getpass("Please enter a password: ")
		except:
			print("\nProgram interrupted.")
			break
		count_validity = 0 # variable to count the number of conditions met
		if(password_input == ""): # if user presses just enter
			print("Please enter a valid password.")
			continue
		if(nonvalid_char_check(password_input) == True):#if input from user contains a space, prompt the user for 
		#another input
			print("Please enter a valid password. Non-valid characters are not allowed in the password.")
			continue
		#if user types finish end program
		if(password_input == "finish"):
			break
		#check for strength of password and update the number of conditions met
		if(upper_lower_check(password_input)):
			count_validity += 1
		if(digit_check(password_input)):
			count_validity += 1
		if(special_char_check(password_input)):
			count_validity += 1
		if(len_check(password_input)):
			count_validity += 1
		#dictionary for displaying the strength of the password
		dict_validity = {0:"Very weak", 1: "Weak", 2:"Medium strength",3:"High medium strength",4:"Strong"}
		print("Your password is ",dict_validity[count_validity])
		print(msg_for_user)
		#check if password is present in the list of common passwords
		check_file(password_input)
#method to check if space is present in the input
def nonvalid_char_check(password):
	for chars in password:
		if((ord(chars) < 33) or (ord(chars) > 126)):#return true if the input contains space or any other invalid chars
			return True
	return False	

#method to check if the input contains upper and lower case characters
def upper_lower_check(password):
	global msg_for_user
	val_upper = 0 # counter for upper case characters
	val_lower = 0 # counter for lower case characters
	for chars in password: # for all characters in the password
		if(chars.isupper()): # check if char is upper case
			val_upper = 1
		elif(chars.islower()): # check if char is lower case
			val_lower = 1
		else:
			continue
		if(val_lower == 1 and val_upper == 1):#if input contains 1 upper and 1 lower case char - one condition is met
			#update global variable
			msg_for_user += "Your password contains at least one uppercase and at least one lowercase letter\n"
			return True
	msg_for_user += "Your password does not contain at least one uppercase and at least one lowercase letter\n"
	return False
#method to check if the input contains a digit
def digit_check(password):
	global msg_for_user
	for chars in password:# for all characters in the password
		if(chars.isdigit()):#check for digits
			msg_for_user += "Your password contains at least one digit\n"
			return True
	msg_for_user += "Your password does not contain at least one digit\n"
	return False
#method to check if the input contains a special character
def special_char_check(password):
	global msg_for_user
	#list of special characters in ASCII values
	special_values = [33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,96,123,124,125,126]
	for chars in password:#for all chars in password
		if(ord(chars) in special_values): # check if ASCII values match
			msg_for_user += "Your password contains at least one character that is not a letter or a digit\n"
			return True
	msg_for_user += "Your password does not contain at least one character that is not a letter or a digit\n"
	return False
#method to check the length of the password
def len_check(password):
	global msg_for_user
	#update global variable based on the length of the input
	if(len(password) >= 6):
		msg_for_user += "Your password has a length of at least six characters\n"
		return True
	else:
		msg_for_user += "Your password does not have a length of at least six characters\n"
		return False

#check if password is present in the file containing common password	
def check_file(password):
	#convert password to lower case
	pass_lowercase = password.lower()
	all_pass = []#list to contain all passwords from the file
	with open("common.txt","r") as common_file:
		# read values from the file
		for lines in common_file:
			all_pass.append(lines.strip())
		#call method to use binary search
		result, comparison = bin_search(pass_lowercase, all_pass)
		if(result == True):
			print("Password is in the list of common passwords.")
		else:
			print("Password is not in the list of common passwords.")
		#print number of comparisons in the binary search and the number of passwords in the list
		print("Number of comparisons = {}. Number of items in list = {}".format(comparison, len(all_pass)))

def bin_search(password, pass_list):
	"""
	1. Let min index = 0 and max index = n-1.
	2. Compute the mid index average of max and min as an integer.
	3. If array[mid] equals password, search is complete or if min index is > max index, all the indices have been searched
	4. If the mid value was too low, that is, array[mid] < password, then set min index = mid index + 1.
	5. Otherwise, the mid index was too high. Set max index = mid index - 1.
	6. Go back to step 2.
	"""
	comp_count = 0 # counts the number of comparisons
	min_index = 0
	max_index = len(pass_list) - 1
	while(min_index <= max_index): # continue till min index is less than or equal to max index
		comp_count += 1 # increase comparison counter
		mid_index = int((max_index + min_index)/2) # calculate mid value
		#print(mid_index," mid ",max_index," max ",min_index, " min")
		if(pass_list[mid_index] == password): # if mid value is equal to password, the value is found
			return True, comp_count
		#If the mid value was too low, that is, array[mid] < password, then set min index = mid index + 1.
		elif(pass_list[mid_index] < password):
			min_index = mid_index + 1
		#Otherwise, the mid index was too high. Set max index = mid index - 1.
		else:
			max_index = mid_index - 1
	return False, comp_count # return false and the number of comparisons done


def main():
	prompt_user()

if __name__ == '__main__':
	main()