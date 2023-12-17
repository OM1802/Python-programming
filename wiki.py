import pyttsx3
import wikipedia

voice = pyttsx3.init()
search_query = input("PLEASE TYPE THE WIKIPEDIA SEARCH TERM: ")
result = wikipedia.summary(search_query, sentences=3)
print(result)
voice.say(result)
voice.runAndWait()
