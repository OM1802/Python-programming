#code for loops in python 
i=-5
for i in range(-4,5):
 print (i)
i=i+1

Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
i=0
for i in range(0,5):
 print(Genres[i])

Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
rating= PlayListRatings[0]
while(rating>=6):
    print(rating)
    i=i+1
    rating=PlayListRatings[i]

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)

Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
New = []
i=0
while i<len(Animals):
    j=Animals[i]
    if(len(j)==7):
        New.append(j)
    i=i+1
print(New)
