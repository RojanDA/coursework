# Create a Python program that counts the number of words, characters, and optionally sentences in a given block of text.

import re
from collections import Counter

def text_analysist(text):

    cleand_text = text.strip()

    words = cleand_text.split()
    num_words = len(words)

    num_chars = len(cleand_text)
    char_with_no_spaces = len(cleand_text.replace(" ", ""))

    sentences = re.split(r'.!?+(?:\s|$)', cleand_text)

    num_sentences = len([s for s in sentences if s.split() != ''])

    word_freq = Counter ( 
        word.lower().strip(".,!?;:") for word in words
    )

    unique_word_count = len(word_freq)

    return {
        "num_words": num_words,
        "num_chars": num_chars,
        "char_with_no_spaces": char_with_no_spaces,
        "num_sentences": num_sentences,
        "unique_word_count": unique_word_count,
        "word_freq": word_freq
    }

def save_results(results, filename="results.txt"):
    with open(filename, 'w') as f:
        f.write("text analysis results:\n")
        f.write(f"Number of words: {results['num_words']}\n")
        f.write(f"Number of characters (including spaces): {results['num_chars']}\n")
        f.write(f"Number of characters (excluding spaces): {results['char_with_no_spaces']}\n")
        f.write(f"Number of sentences: {results['num_sentences']}\n")
        f.write(f"Number of unique words: {results['unique_word_count']}\n")
        f.write("Word frequencies:\n")

        for word, freq in results['word_freq'].items():
            f.write(f"{word}: {freq}\n")

    print(f"Results saved to {filename}")

def main():
    print("Enter your text (type 'exit' to finish or press Enter twice to finish: ):")
    lines = []
    while True:
        line = input()
        if line.lower() == 'exit' or line == '':
            break
        lines.append(line)
    text = "\n".join(lines)
    results = text_analysist(text)
    save_results(results)
    print ("congratulation")

if __name__ == "__main__":
    main()