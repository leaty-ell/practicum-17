def process_word_frequencies(text):
    """
    Function processes input text and returns words sorted by frequency.
    1. Counts the frequency of each word in the text
    2. Sorts words by frequency in descending order
    
    Arguments:
        text (str): Input string containing words separated by spaces
    
    Returns:
        list: List of words sorted by decreasing frequency of occurrence
    """
    words = text.split()
    frequencies = {}
    
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    
    items = list(frequencies.items())
  
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    
    sorted_words = []
    for word, frequency in items:
        sorted_words.append(word)
    
    return sorted_words


def main():
    """
    Main function of the program.
    Gets input from user and displays words sorted by frequency.
    """
    print("Enter a string with words:")
    input_text = input()
