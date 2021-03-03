class Node:
    data = ''
    left = None
    right = None

max_nodes = 15
tree = [Node() for i in range(max_nodes)]
head = None
freePtr = 0

def initialise_tree():
    global tree, head, freePtr, max_nodes
    for i in range(max_nodes - 1):
        tree[i].left = i + 1
    tree[max_nodes - 1].left = None
    return tree


def insert_node(data):
    global tree, head, freePtr
    if freePtr is None:
        print('Insert failed - tree is full!')
        return
    newNodePtr = freePtr
    freePtr = tree[freePtr].left
    tree[newNodePtr].data = data
    tree[newNodePtr].left = None
    tree[newNodePtr].right = None

    if head is None:
        head = newNodePtr
        return
    curr_ptr = head
    while curr_ptr is not None:
        prev_ptr = curr_ptr
        if data < tree[curr_ptr].data:
            curr_ptr = tree[curr_ptr].left
            turned_left = True
        else:
            curr_ptr = tree[curr_ptr].right
            turned_left = False

    if turned_left:
        tree[prev_ptr].left = newNodePtr
    else:
        tree[prev_ptr].right = newNodePtr

def print_tree_inorder():
    global tree, head
    if head is None: return
    def recur(curr_ptr):
        if tree[curr_ptr].left is not None:
            recur(tree[curr_ptr].left)
        print(tree[curr_ptr].data)
        if tree[curr_ptr].right is not None:
            recur(tree[curr_ptr].right)
    recur(head)

def index_of(data):
    global tree, head
    curr_ptr = head
    while curr_ptr is not None:
        if data < tree[curr_ptr].data:
            curr_ptr = tree[curr_ptr].left
        elif data > tree[curr_ptr].data:
            curr_ptr = tree[curr_ptr].right
        else:
            return curr_ptr
    return -1

initialise_tree()
insert_node('red')
insert_node('blue')
print_tree_inorder()