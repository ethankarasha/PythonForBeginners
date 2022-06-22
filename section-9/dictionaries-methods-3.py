internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
print(internet_celebrities)

 
same = internet_celebrities.copy()
internet_celebrities.clear()
print(internet_celebrities)
print(same) 

