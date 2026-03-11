from collections import Counter


def get_freq(text):
    """
    Counts word frequencies and records first occurrence indices.
    
    Arguments:
        text: input string with words separated by spaces
    
    Returns:
        tuple: (Counter of frequencies, dict of first occurrences)
    """
    words = text.split()
    freq = Counter(words)
    
    first_occurrence = {}
    for i, word in enumerate(words):
        if word not in first_occurrence:
            first_occurrence[word] = i
    
    return freq, first_occurrence


def sort_words_by_frequency(text):
    """
    Sorts words by frequency in descending order.
    Words with same frequency keep original order.
    
    Arguments:
        text: input string with words separated by spaces
    
    Returns:
        str: sorted words joined by spaces
    """
    freq, first_idx = get_freq(text)
    
    sorted_words = sorted(
        freq.keys(),
        key=lambda x: (-freq[x], first_idx[x])
    )
    
    return ' '.join(sorted_words)


def main():
    """Main function of the program."""
    text = input().strip()

    result = sort_words_by_frequency(text)
    print(result)


if __name__ == "__main__":
    main()
