#######################################################################################################################################
#######################################################################################################################################
##################################################### Import Libraries -- Do Not Change ###############################################
#######################################################################################################################################
#######################################################################################################################################

import itertools
import os
from iota import Iota

#######################################################################################################################################
#######################################################################################################################################
########################################## Initialise User Variables -- Change Values Accordingly #####################################
#######################################################################################################################################
#######################################################################################################################################

length = 5 # number of chars missing from seed 
numberOfAddresses = 3 # Number of addresses to generate and check for a match. 
known_seed_value = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" #Known Seed characters (partial)
known_recieving_value = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" # Known recieving address (full)

#######################################################################################################################################
#######################################################################################################################################
############################################### Initialise Program Variables -- Do Not Change #########################################
#######################################################################################################################################
#######################################################################################################################################

#API Variable
iotaNode = "http://localhost:14265" # use local computer for calculations

#Character set and reverse dictionary Variables
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ9' # All possibilities for IOTA seed
rdict = dict([ (x[1],x[0]) for x in enumerate(chars) ]) # define reverse lookup dict. This gives number values to the possible characters in the seed. 

#Log Variable
j = 0 #variable for saving logs. Initialisation needs to occur here. 

#######################################################################################################################################
#######################################################################################################################################
############################################## Create Seed Permutations -- Do Not Change ##############################################
#######################################################################################################################################
#######################################################################################################################################

def perm(n, seq, Start_value):
    print("Bruteforcer Running...")
    all_combos = itertools.product(seq, repeat=n)
    for p in itertools.islice(all_combos, Start_value, None): #start at START_VALUE and stop at None (the end)
        perm_result = "".join(p)
        seed = known_seed_value + perm_result        
        addressGenerator(seed)
        
#######################################################################################################################################
#######################################################################################################################################
############################################ Create Recieving Address Permutations -- Do Not Change ###################################
#######################################################################################################################################
#######################################################################################################################################

def addressGenerator(seed):
	api = Iota(iotaNode, seed) # The iota nodes IP address must always be supplied, even if it actually isn't used in this case.
	gna_result = api.get_new_addresses(count=numberOfAddresses) # This is the function to generate the address.
	addresses = gna_result['addresses']
	i = 0 #int for number of addresses
	while i < numberOfAddresses:
		address = [addresses[i]]
		i += 1
		if address[0] == known_recieving_value: # If the address is equal to the recieving address then.. (Address without checksum)
			print("Bruteforcer Finished")
			print("The seed is: " + seed)
			file = open("seed.txt","w") #Open file. 
			file.write("Bingo. The seed is: " + seed) #print out bingo and the correct seed. 
			file.close() #Close the file to save changes. 
			exit() #if it finds the correct address stop the program. 
	global j # References j from initialisation. 
	j = j + 1 # increase j by 1. 	
	if j == 1000: #if 1000 seeds have been checked. Close the file and the re-open so that the changes can be seen. 
		file = open("log.txt","w") #Open file and overwrite it (overwrite so that the size doesn't get too large)
		file.write("Checked up to Seed: " + seed)
		file.close()
		j = 0 #Set j back to 0. 

#######################################################################################################################################
#######################################################################################################################################
############################################## Get The Seed Index Value -- Do Not Change ##############################################
#######################################################################################################################################
#######################################################################################################################################

def get_index(string_value):
	sum = 0 #set sum equal to zero.
	for i in range(0, length): #create a loop between 0 and length (in this situation length is equal to 13 so loop will go up to 12)
		if i == length-1: #if loop reaches the last character in the string
			sum += rdict[string_value[i]] + 1 #add the value of that character to the sum 
		else:
			sum += ((rdict[string_value[i]])) * (27**(length-i-1)) #add the value of that character to the sum 
	return sum

#######################################################################################################################################
#######################################################################################################################################
####################################################### Program Start -- Do Not Change ################################################
#######################################################################################################################################
#######################################################################################################################################

print("")
print("################################################################################################")
print("####################################### IOTA Bruteforcer #######################################")
print("################################################################################################")
print("")

#Figure out whether to start from the first seed value of whether to begin from a previously saved seed value within the log.txt file. 
if os.stat("log.txt").st_size == 0: #if the log file is empty
	start_value = 0 #set the start value of the seed to index 0 - i.e. start at the beginning.
	print("No seed found. Starting from first seed value.")
else: #if there is a seed value in the log file
	file = open("log.txt","r") #Open file. 
	file_seed_value = file.read() #read the file contents.
	print ("Seed found. Previously have " + file_seed_value) 
	file.close() #Close the file to save changes. 
	seed_product_string = file_seed_value[-length:]
	print ("The previous variable part of the seed value was: " + seed_product_string)
	res = get_index(seed_product_string)
	start_value =  res #define the index value of the start value for the seed. 

perm(length, chars, start_value) #Run the permutations


