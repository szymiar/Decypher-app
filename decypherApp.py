#! python3
import pyperclip, sys, pprint

## rozwiąz problem tablicy ze wyrzuca poza zakres , try i except index error, i wtedy reszte
## od zera dodajesz






# In this section program asks for entering the sentence that needs to be decoded
def enteringSentence():
	while True:
		try:
			decision1 = int(input())
		except ValueError:
			print("Please enter a number")
		
		if decision1 == 1:
			sentence = pyperclip.paste()
			table = prepareSentence(sentence)
			break
		elif decision1== 2:
			sentence = input("Please enter the sentence:  ")
			table = prepareSentence(sentence)
			break
		else:
			print("Type 1 or 2")
			continue
	return table   #Returns sentence with separated words 
	
	
#This method will change given sentence into table of strings
def prepareSentence(sentence):
	sentenceLower = sentence.lower()
	table = list(sentenceLower)
	return table

#This method will decode the message with your shift
def decode(table,shift):
	j = 0
	for i in table:
		try:
			z = alphabet.index(i)
		except ValueError:
			j+=1
			continue
		table[j] = shifting(z, shift)
		j+=1
	return table
	

#This method will display all of the possible shifts( if u find a good dictionary,
#Your program will find existing words itself
def displayAllPosibilities(table):
	for i in table:
		z = alphabet.index(i)
		

#This method will return shifted letter
def shifting(index,shift):   
	index+=shift
	try:
		shiftedLetter = alphabet[index]
	except IndexError:
		
	return shiftedLetter

#This method wil display decoded sentence
def displayDecoded(table):
	pyperclip.copy(''.join(table))
	print(pyperclip.paste())
	
	

##This is main function heh
def Main():
	print("This program will decode a caesar's cypher for you")
	print("Type 1 to copy the sentence from your clipboard, or type 2 to enter the sentence")

	zdanie = enteringSentence()
	print("Enter your shift")
	while True:
		try:
			shft = int(input())
			break
		except ValueError:
			print("Enter number")
	tablica = decode(zdanie, shft)
	displayDecoded(tablica)
	


	
alphabet = ["a","b","c","d","e","f","g","h","i",
			"j","k","l","m","n","o","p","q","r",
			"s","t","u","v","w","x","y","z"]

polishAlphabet = ["a","ą","b","c","ć","d","e","ę","f","g","h","i",
				"j","k","l","ł","m","n","ń","o","ó","p","q","r","s",
				"ś","t","u","v","w","x","y","z","ź","ż"]
				


Main()