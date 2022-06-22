first = {"Queen": "Bohemian Rhapsody", 
        "Bee Gees": "Stayin' Alive", 
        "U2": "One", 
        "Michael Jackson":  "Billie Jean", 
        "The Beatles": "Hey Jude", 
        "Bob Dylan": "Like A Rolling Stone"}

print(len(first))

artists = first.keys()
for key in artists:
    print(key)

print(first.values())

pairs = first.items()
for items in pairs:
    print(items)

print(first.get("Promise of the Real", "Promise of the Real is mid."))

