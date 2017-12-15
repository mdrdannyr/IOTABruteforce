import itertools
from iota import Iota


length = 13 # Enter number of chars missing from seed 
numberOfAddresses = 3 # Enter Number of addresses to generate from the seed and check for a match. 


chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ9' # All possibilities for IOTA seed
iotaNode = "http://localhost:14265" # use local computer for calculations
j = 0 #variable for saving logs. Initialisation needs to occur here. 

def perm(n, seq):
    print("Bruteforcer Running...")
    for p in itertools.product(seq, repeat=n):
        perm_result = "".join(p)
        
        
        seed = "Enter_Known_Seed_Characters" + perm_result #Change if it is in a different pattern.        
        

        addressGenerator(seed)



def addressGenerator(seed):
	api = Iota(iotaNode, seed) # The iota nodes IP address must always be supplied, even if it actually isn't used in this case.
	gna_result = api.get_new_addresses(count=numberOfAddresses) # This is the function to generate the address.
	addresses = gna_result['addresses']
	i = 0 #int for number of addresses
	while i < numberOfAddresses:
		address = [addresses[i]]
		i += 1
		if address[0] == "Enter_Receiving_Address": # If the address is equal to the recieving address then.. (Address without checksum)
			print("Bruteforcer Finished")
			print("The seed is: " + seed) 
			file = open("log.txt","w") #Open file. 
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


print("######## IOTA Bruteforcer ########")
perm(length, chars) #Run the permutations




