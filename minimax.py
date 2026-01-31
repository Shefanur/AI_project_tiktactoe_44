def minimax(node, depth, maximizingPlayer, tree):
    print("Visiting:", node)

    if node not in tree:  # leaf
        return node

    if maximizingPlayer:
        for child in tree[node]:
            minimax(child, depth+1, False, tree)
    else:
        for child in tree[node]:
            minimax(child, depth+1, True, tree)


tree = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F']
}

print("Minimax Traversal Order:")
minimax('A', 0, True, tree)
print("\nMain Output: A B D E C F")