def create_antonym_dictionary(n):
    """
    Creates dictionary of antonyms.
    
    Arguments:
        n: number of pairs
    
    Returns:
        dict: word -> its antonym
    """
    antonyms = {}
    for i in range(n):
        pair = input().split()
        word1 = pair[0]
        word2 = pair[1]
        antonyms[word1] = word2
        antonyms[word2] = word1
    return antonyms


def main():
    """Main function for task 3."""
    n = int(input())
    antonyms = create_antonym_dictionary(n)
    target = input()
    
    if target in antonyms:
        print(antonyms[target])
    else:
        print(target)


if __name__ == "__main__":
    main()
