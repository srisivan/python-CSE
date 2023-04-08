# Write a program to calculate the frequencies of characters in a string and print them in alphabetical order.

# This program uses dictionaries.

characters = []
character_freq = {}
character_count = 0

string = str(input("\n>> "))

for character in string:
    characters.append(character)

characters.sort()

for ch in characters:
    character_freq.update({ch: 0})

for character in string:
    for character_2 in string:
        if (character == character_2):
            character_count += 1


        character_freq[character] = character_count

    character_count = 0


print()
for ch, freq in character_freq.items():
    print("%s: %d" % (ch, freq))
