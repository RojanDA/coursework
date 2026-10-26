# Write a Python program that uses match-case to categorize 
# an input character as a vowel, consonant,
# digit, or special character.


def cate_char(char):

    char = char.lower()

    match char:

        case 'a'|'e'|'i'|'0'|'u':
           category = 'vowel'
        case 'b'|'c'|'d'|'f'|'g'|'h'|'j'|'k'|'l'|'m'|'n'|'p'|'q'|'r'|'s'|'t'|'v'|'w'|'x'|'y'|'z':
            category = 'consonant'
        case '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9' :
            category = 'number'
        case _:
            category = 'symbol'
    return category


x=1
while x != 0:
 char = input("any character: ")
 if len(char) == 1:
    category = cate_char(char)
    print(f"the caracter '{char}' is a {category}")
    break
 else:
    print("please enter a single char")
        
