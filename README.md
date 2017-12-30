# IOTABruteforce

A program to find an IOTA seed based on the receiving address. 

This program is for people who have sent money to a receiving address, but unfortunately have lost part of their seed.

## Instructions: 

- The first thing to do which is essential is remove all text from the seed.txt file. If there is data in the seed.txt file, the program will not run as it will think that the seed has already been found.
- If there is already a seed in the log.txt file, the program will run continue from that seed. If there is no seed in the log file it will start from the first possible seed value (AAAAA). 
- The IOTA_Bruteforcer.py is the main program to run. There is a section in here with the outlined variables which the user has to edit. Please note that the program is multiprocessing (i.e. runs on multiple processes). This is to increase the speed. 
  
  Note: Be aware of your systems maximum number size (sys.maxsize). If the previously saved seed in log.txt has an index value greater than this, the program may not function properly. 
```
python3
```
```
import sys
```
```
sys.maxsize
```
 
- The program will save every 1000th seed checked into the log.txt file. If a matching seed is found, it will be saved into the seed.txt file. 
- To find out how many seeds have been checked run the get_seed_index.py file (no input is needed - it will retrieve the seed from the log.txt file). 

#### Commands to run the program: 

- Ensure the user has permissions to write to the log.txt file and seed.txt file. 
```
python3 IOTA_Bruteforcer.py
```
- To check how many seeds have been checked. (run in another terminal) 
```
python3 get_seed_index.py
```

## Required to run the program:

- The known characters of your seed (i.e. 75 characters) 
- The Receiving address (i.e. where you sent your IOTA to)
- The Receiving address index (i.e. how many receiving addresses did you generate in your wallet and what number in that list was the address to which the IOTA was sent.). 
- (If running on linux, ensure the user has permissions to write to the log file) 


## Requirements: 
- Python 3.6 or 3.5 or 2.7.

- pyota 

### Commands to install:
```
apt-get install python3.6 
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

## Information - Calculating how many seeds you've checked from the seed value 

Due to memory / hard disk issues, and wanting the program to be as efficient as possible, the script overwrites the log file instead of appending it and does not have a lot of progress information. The only information the user recieves in terms of progress is the seed last checked which is saved into the log file. 

To calculate how many seeds have been checked using this seed value please see the below: 

Assuming the latest iteration of seed has a variable section of: ABCD 

Total seeds checked = 27<sup>3</sup> * (A-1) + 27<sup>2</sup> * (B-1) + 27<sup>1</sup> * (C-1) + 27<sup>0</sup> * D 

Where each characters value is the index value between A-Z9. i.e:

A = 1

B = 2 

...

9 = 27 

Therefore the seed value: AEDC would be equal to 3000 seeds checked. i.e:  

27<sup>3</sup> * (1-1) + 27<sup>2</sup> * (5-1) + 27<sup>1</sup> * (4-1) + 27<sup>0</sup> * 3 = 3000

## References: 


https://github.com/iotaledger/iota.lib.py

https://github.com/bahamapascal/IOTA-Balanace-Checker

