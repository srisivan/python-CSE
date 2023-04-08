# Write a program to calculate the frequencies of characters in user's string, and print them in alphabetical order.

# This program doesn't use dictionaries, and makes do with lists.

characters = []
unique_characters = []
frequency = []
char_count = 0

string = str(input("\n>> "))
string = string.lower()

for character in string:
    characters.append(character)

characters.sort()

unique_characters = sorted(set(characters))

print()

for ch in unique_characters:
    for ch_2 in string:
        if (ch == ch_2):
            char_count += 1

    frequency.append(char_count)

    char_count = 0

for (ch, count) in zip(unique_characters, frequency):
    print("%s: %d" % (ch, count))
