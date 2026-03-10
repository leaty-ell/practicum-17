def create_dictionary(n):
    """
    Creates Russian-English dictionary.
    
    Arguments:
        n: number of pairs
    
    Returns:
        dict: Russian-English dictionary
    """
    dictionary = {}
    for i in range(n):
        pair = input().split()
        russian = pair[0]
        english = pair[1]
        dictionary[russian] = english
    return dictionary


def translate_phrase(phrase, dictionary):
    """
    Translates phrase using dictionary.
    
    Arguments:
        phrase: string to translate
        dictionary: translation dictionary
    
    Returns:
        string: translated phrase
    """
    words = phrase.split()
    result = []
    
    for word in words:
        if word in dictionary:
            result.append(dictionary[word])
        else:
            result.append(word)
    
    return " ".join(result)


def main():
    """Main function"""
    n = int(input())
    dictionary = create_dictionary(n)
    phrase = input()
    result = translate_phrase(phrase, dictionary)
    print(result)


if __name__ == "__main__":
    main()
