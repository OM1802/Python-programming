#PLEASE MAKE SURE THAT YOU HAVE INSTALLED THE "pyttsx3 and wikipedia module" BEFORE RUNNING THIS PROGRAM

import pyttsx3 #importing pyttsx3 to conver the output into audio
import wikipedia #importting wikipedia to search. The information given are updated to January, 2023

voice = pyttsx3.init()
search_query = input("PLEASE TYPE THE WIKIPEDIA SEARCH TERM: ")
result = wikipedia.summary(search_query, sentences=3)
print(result)
voice.say(result)
voice.runAndWait()
