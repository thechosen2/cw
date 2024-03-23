winstring = '''Red Wins
Red Wins
Red Wins
Red Wins
Red Wins
Red Wins
Red Wins
Blue Wins
Blue Wins
Red Wins
Red Wins
Red Wins
Blue Wins
Red Wins
Blue Wins
Red Wins
Red Wins
Red Wins
Blue Wins
Red Wins
Red Wins
Red Wins
Red Wins
Blue Wins
Red Wins
Red Wins
Red Wins
Red Wins
Blue Wins
Red Wins
Blue Wins
Red Wins
Red Wins
Blue Wins
Red Wins
Red Wins
Blue Wins
Red Wins
Red Wins
Red Wins
Blue Wins
Red Wins
Red Wins
Red Wins
Red Wins
Red Wins
Red Wins
Red Wins
Blue Wins
Blue Wins'''
red = 0
blue = 0
t= winstring.split(' ')
for ele in t:
    if 'Red' in ele:
        red +=1
    elif 'Blue' in ele:
        blue +=1
print(red)
print(blue)