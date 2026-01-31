def alphabeta(node, depth, alpha, beta, maximizingPlayer, tree):
    print("Visiting:", node)

    if node not in tree:
        return node

    if maximizingPlayer:
        for child in tree[node]:
            val = alphabeta(child, depth+1, alpha, beta, False, tree)
            if alpha >= beta:
                print("Pruned at:", child)
                break
    else:
        for child in tree[node]:
            val = alphabeta(child, depth+1, alpha, beta, True, tree)
            if beta <= alpha:
                print("Pruned at:", child)
                break


tree = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F']
}

print("Alpha Beta Traversal Order:")
alphabeta('A', 0, -999, 999, True, tree)
print("\nMain Output: A B D E C F")