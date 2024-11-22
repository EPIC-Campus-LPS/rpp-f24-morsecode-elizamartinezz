
import pydub
import os
import glob
from pydub import AudioSegment
from pydub.playback import play

#morseShort= AudioSegment.from_mp3("morseshort.mp3")
#morseLong = AudioSegment.from_mp3("morselong.mp3")
try:
    morseShort = AudioSegment.from_mp3("morseshort.mp3")
    morseLong = AudioSegment.from_mp3("morselong.mp3")
    print("Audio files loaded successfully.")
except FileNotFoundError:
    print("Error: Audio files not found.")

word = input("Enter a word to play in morse code: ")
##dictionary for the letters
morse_code = {
	'A' : '. -',
	'B' :'-...',
	'C': '-.-.',  
	'D': '-..',
	'E': '.',
    'F': '..-.',  
    'G': '--.',   
    'H': '....',  
    'I': '..',    
    'J': '.---',
    'K': '-.-',   
    'L': '.-..',  
    'M': '--',    
    'N': '-.',    
    'O': '---',
    'P': '.--.',  
    'Q': '--.-',  
    'R': '.-.',   
    'S': '...',   
    'T': '-',
    'U': '..-',   
    'V': '...-',  
    'W': '.--',   
    'X': '-..-',  
    'Y': '-.--',
    'Z': '--..',
    '1': '.----', 
    '2': '..---', 
    '3': '...--', 
    '4': '....-', 
    '5': '.....',
    '6': '-....', 
    '7': '--...', 
    '8': '---..', 
    '9': '----.', 
    '0': '-----'
}
	


count = 0
#count keeps track of how many times the loop continues
while count<len(word): #while count less than the length of test (0, 1, 2, 3)
	if word[count].upper() in morse_code:
		t = morse_code[word[count].upper()]
		print(t)
		for ch in t: #loops through every character in test
			if ch == ".":
				play(morseShort)
				print("short")
			if ch == "-":
				play(morseLong)
				print("long")
		count += 1
