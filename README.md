# IOTABruteforce

A program to find an IOTA seed based on the receiving address. 

This program is for people who have sent money to a receiving address, but unfortunately have lost part of their seed. 

## Required to run the program:

- The known characters of your seed (i.e. 75 characters) 
- The Receiving address (i.e. where you sent your IOTA to)
- The Receiving address index (i.e. how many receiving addresses did you generate in your wallet and what number in that list was the address to which the IOTA was sent.). 


## Requirements: 
- Python 3.6 or 3.5 or 2.7.

- pyota 

# Commands to install:
```
apt-get install python 3.6 
```
```
pip install pyota[ccurl] 
```
(The ccurl is optional but it is stated that this decreases the amount of time taken to carry out cryptographic calculations by up to 60X). 

## Information - Number of possibilities for seeds are as follows: 

Each character can be made up from upper-case letters A-Z and the digit 9 giving a total count of 27 possibilities for each character. 

Total number of seeds are therefore:

27<sup>N</sup> * I

Where, N = Numbers of characters missing from the seed;

I = Index number of your receiving address. 


## References: 


https://github.com/iotaledger/iota.lib.py

https://github.com/bahamapascal/IOTA-Balanace-Checker

