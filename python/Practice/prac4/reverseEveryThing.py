# Create a simple Python program that reverses a word, sentence, or paragraph entered by the user.


def reverse_text(text):
    return text[::-1]

def main():
    print("Enter the text you want to reverse (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == '':
            break
        lines.append(line)
    full_text = '\n'.join(lines)
    reversed_text = reverse_text(full_text) 

    print("Reversed text:")
    print(reversed_text)

if __name__ == "__main__":
    main()