def Check_Vow(string, letters):

    string = string.casefold()

    count = {}.fromkeys(letters, 0)

    for character in string:

        if character in count:

            count[character] += 1   

    return count

vowels = 'misp'

string = input("please enter the string: ")

print (Check_Vow(string, vowels))
