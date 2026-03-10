def create_shape_dictionary(n):
    """
    Creates dictionary of objects and their shapes.
    
    Arguments:
        n: number of shape categories
    
    Returns:
        dict: object -> shape
    """
    shapes = {}
    for i in range(n):
        line = input().split()
        shape = line[0]
        objects = line[1:]
        
        for obj in objects:
            shapes[obj] = shape
    
    return shapes


def main():
    """Main function"""
    n = int(input())
    shapes = create_shape_dictionary(n)
    target = input()
    
    if target in shapes:
        print(shapes[target])
    else:
        print(target)


if __name__ == "__main__":
    main()
