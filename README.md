# IOTABruteforce

A program to find an IOTA seed based on the receiving address. 

This program is for people who have sent money to a recieving address, but unfortunately have lost part of their seed. 

# Required to run the program:

- The known characters of your seed (i.e. 75 characters) 
- The Receiving address (i.e. where you sent your IOTA to)
- The Receiving address index (i.e. how many receiving addresses did you generate in your wallet and what number in that list was the address to which the IOTA was sent.). 



## Number of possibilities for seeds are as follows: 

Each character can be made up from [A-Z9] giving a total count of 27 possibilities for each character. 

Total number of seeds are therefore:

                        27^N * Y

N = Numbers of characters missing from the seed and 
Y is equal to the index number of your receiving address. 



# Requirements: 
Python 3.6 or 3.5 or 2.7.
pyota 

apt-get install python 3.6 
pip install pyota[ccurl] 

(The ccurl is optional but it is stated that this decreases the amount taken to carry out cryptographic calculations by up to 60X). 


#References: 


(https://github.com/iotaledger/iota.lib.py)


