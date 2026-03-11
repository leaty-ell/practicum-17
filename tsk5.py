def build_family_tree(n):
    """
    Builds family tree from parent-child relationships.
    
    Arguments:
        n: number of relationships
    
    Returns:
        dict: parent -> list of children
    """
    tree = {}
    
    for i in range(n):
        parent, child = input().split()
        
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = [child]
        
        if child not in tree:
            tree[child] = []
    
    return tree


def count_descendants(name, tree):
    """
    Recursive function to count all descendants.
    
    Arguments:
        name: person name
        tree: family tree
    
    Returns:
        int: number of descendants
    """
    if name not in tree:
        return 0
    
    count = 0
    for child in tree[name]:
        count = count + 1
        count = count + count_descendants(child, tree)
    
    return count


def main():
    """Main function"""
    n = int(input())
    tree = build_family_tree(n)
    target = input()
    
    result = count_descendants(target, tree)
    print(result)


if __name__ == "__main__":
    main()
