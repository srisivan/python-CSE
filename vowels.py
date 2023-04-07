# A program to accept an input string from the user, print "Accepted" if it consists entirely of vowels, "Rejected" otherwise.

vowels = ['A', 'E', 'I', 'O', 'U']

def get_message(string):
    
    flag = 0
    
    for character in string:
        if character not in vowels:
            flag = 1
            break

    if (flag == 0):
        return 1
    else:
        return 0


message = str(input(">> "))

message = message.upper()
result = get_message(message)

if (result == 1):
    print("Accepted.")
else:
    print("Rejected.")
