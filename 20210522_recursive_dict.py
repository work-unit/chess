import chess
import time


class Tree:
    def __init__(self, board):
        self.board = board
        self.children = []

    def addNode(self, obj):
        self.children.append(obj)


class Node:
    def __init__(self, parent, board):
        self.parent = parent
        self.board = board
        self.children = []

    def addNode(self, obj):
        self.children.append(obj)


def build_tree(parent, level):
    if level == MAX_LEVEL:
        return

    if len(list(parent.board.legal_moves)) == 0:
        #probability = jonah_model(board_copy)
        probability = 0.5 # placeholder until I integrate with Jonah
        leaves[level].append(probability)

    # Build up children nodes
    for move in parent.board.legal_moves:
        board_copy = parent.board.copy()
        board_copy.push(move)
        parent.addNode(Node(parent, board_copy))
        if board.is_checkmate():
            probability = 1
        else:
            #probability = jonah_model(board_copy)
            probability = 0.5 # placeholder until I integrate with Jonah
        tree_dict[level].append(probability)  # This is Jonah's prediction, I put 0.5 as a place holder
        if level == MAX_LEVEL - 1:
            leaves[level].append(probability)

    for node in parent.children:
        build_tree(node, level+1)


if __name__ == '__main__':
    print("Running Main")
    start_time = time.time()
    MAX_LEVEL = 3  # Up to 4 is 10 seconds
    tree_dict = {k: [] for k in range(MAX_LEVEL)}
    leaves = {k: [] for k in range(MAX_LEVEL)}
    board = chess.Board()
    root = Tree(board)
    build_tree(root, 0)
    print(tree_dict.keys())
    print('leaves:', leaves)
    print('leaves length:', len(leaves))
    end_time = time.time()
    print('Total Time Run:', end_time - start_time)
