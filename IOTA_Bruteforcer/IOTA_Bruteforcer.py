#######################################################################################################################################
#######################################################################################################################################
##################################################### Import Libraries -- Do Not Change ###############################################
#######################################################################################################################################
#######################################################################################################################################

from multiprocessing import Pool, Value, Lock, cpu_count
import itertools
import os
from iota import Iota
from ctypes import c_int

#######################################################################################################################################
#######################################################################################################################################
########################################## Initialise User Variables -- Change Values Accordingly #####################################
#######################################################################################################################################
#######################################################################################################################################

length = 13 # number of chars missing from seed 
numberOfAddresses = 3 # Number of addresses to generate and check for a match. 
known_seed_value = "GNYGKKCFHLPEBEGGIUQIDFW9VGWKSRIQBNDCYLTZXHTBWMPIIHHMFTGMPU9JRXUJETWS" #Known Seed characters (partial)
known_recieving_value = "VCNJAOLU9UNNOTVIWQOMGBESECWQNNIOTJDTRTEXWNLXUBFOVANTJPAWSTDKDDNPQQV9UIFQGDNDJALZJ" # Known recieving address (full)
cores_all_physical = False #If running on a machine where all the cores are physical set to true. IF unsure, leave as False. 

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

#Counter Variable for log.txt and lock initialisation for multi-processor processing
counter = Value(c_int)  # defaults to 0
counter_lock = Lock()

#Calculate number of processes that will be used as workers in the pool. 
if cores_all_physical == False:
	CPU_count = cpu_count() // 2 #Get number of logical cores then divide by two to get number of physical cores (assuming 2 threads per core) then Floor the value.  
else: 
	CPU_count = cpu_count() #Set number of processes equal to the number of cores given by the function. 

#######################################################################################################################################
#######################################################################################################################################
############################################## Get The Seed Start Value -- Do Not Change ##############################################
#######################################################################################################################################
#######################################################################################################################################

def get_seed_start_value(): #Figure out whether to start from the first seed value of whether to begin from a previously saved seed value within the log.txt file. 
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
		start_value = get_index(seed_product_string)
	return start_value

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
######################################################### Pool function -- Do Not Change ##############################################
#######################################################################################################################################
#######################################################################################################################################

def pool(p): # Take the variable part of the seed, convert it into normal string then add it to the known seed characters and send it on to the addressGenerator. 
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
	#print("Checking seed: " + seed)
	while i < numberOfAddresses:
		address = [addresses[i]]
		#print("   checking address : " + str(address[0]))
		i += 1
		if address[0] == known_recieving_value: # If the address is equal to the recieving address then.. (Address without checksum)
			print("Bruteforcer Finished")
			print("The seed is: " + seed)
			file = open("seed.txt","w") #Open file. 
			file.write("Bingo. The seed is: " + seed) #print out bingo and the correct seed. 
			file.close() #Close the file to save changes. 
			 #if it finds the correct address stop the program. 
	increment(seed) #increase counter by 1 and check if seed needs to be saved into log. 

#######################################################################################################################################
#######################################################################################################################################
################################################### Counter for log -- Do Not Change ##################################################
#######################################################################################################################################
#######################################################################################################################################

def increment(seed):
    with counter_lock:
        counter.value += 1 
        #print (str(counter.value))   
        if counter.value == 1000: #if 1000 seeds have been checked. 
            file = open("log.txt","w") #Open file and overwrite it (overwrite so that the size doesn't get too large)
            file.write("Checked up to Seed: " + seed)
            file.close()
            counter.value = 0 #Set counter back to 0. 

#######################################################################################################################################
#######################################################################################################################################
####################################################### Program Start -- Do Not Change ################################################
#######################################################################################################################################
#######################################################################################################################################

if __name__ == "__main__":

	print("")
	print("################################################################################################")
	print("####################################### IOTA Bruteforcer #######################################")
	print("################################################################################################")
	print("")
	print("Bruteforcer Running...")

	Start_value = get_seed_start_value() #Get the seed start value
	all_combos = itertools.product(chars, repeat=length) #Produce all the combinations 
	data = itertools.islice(all_combos, Start_value, None) #save the itertools value as a variable for Pool use. Start the seed at Start_value and stop at None (the end)
	for i in Pool(processes=CPU_count).imap(pool,data,chunksize=1): #use CPU_count number of processors. Send data to function pool. Chunksize 1 makes sure that each process only takes one seed. Ensures that the log file will be correct. 
		if not os.stat("seed.txt").st_size == 0: #if the seed file size is not 0 (i.e. a seed has been found)
			exit() #exit the program
			
