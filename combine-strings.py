# you have two strings merge them letter after letter and if one is shorter add it to the rest
#[WIP]

def main():
    str1 =  "challenge"
    str2 =  "cave"

    new_word = []
    if len(str1) > len(str2):
        longest = str1
        shortest =  list(str2)
    elif len(str2) > len(str1):
        longest = str2
        shortest = list(str1)
    elif len(str1) == len(str2):
        longest = str1
        shortest = list(str2)

    shortest.reverse()
    for letter in list(longest):
        new_word.append(letter)
        if len(shortest) != 0:
           new_word.append(shortest.pop())

    # return new_word
    print(''.join(new_word))

if __name__ == '__main__':
    main()
