from main import *


def test_isnotAVL():
    node1 = AVLNode(90)
    node2 = AVLNode(3)
    node3 = AVLNode(9, right=node2, left=node1)
    tree = Tree(node3)
    assert tree.isAVL() is False


def test_isAVL():
    node1 = AVLNode(1)
    node2 = AVLNode(3)
    node3 = AVLNode(2, right=node2, left=node1)
    node4 = AVLNode(7)
    node5 = AVLNode(6, right=node4, left=node3)
    tree = AVLTree(node5)
    assert tree.isAVL() is True


def test_isBalanced():
    node1 = AVLNode(3)
    node2 = AVLNode(5)
    node3 = AVLNode(1)
    node4 = AVLNode(9)
    node2.left = node1
    node2.right = node4
    node2.left.left = node3
    tree = AVLTree(node2)
    assert tree.isBalanced() is True


def test_isNotBalanced():
    node6 = AVLNode(-21)
    node5 = AVLNode(-2, left=node6)
    node1 = AVLNode(3, left=node5)
    node4 = AVLNode(9)
    node2 = AVLNode(5, left=node1, right=node4)
    tree = Tree(node2)
    assert tree.isBalanced() is False


def test_isnotBalanced2():
    node5 = AVLNode(5)
    node6 = AVLNode(6)
    node2 = AVLNode(2, right=node5)
    node4 = AVLNode(4, left=node6)
    node1 = AVLNode(1, left=node4)
    node7 = AVLNode(8, left=node1, right=node2)
    node7.left = node1
    node7.right = node2
    node7.left.left = node4
    node7.right.right = node5
    node7.left.left.left = node6
    tree = Tree(node7)
    assert tree.isBalanced() is False


def test_deleteMax():
    node1 = AVLNode(3)
    node2 = AVLNode(237974)
    node3 = AVLNode(9)
    node4 = AVLNode(1)
    node5 = AVLNode(4)
    node6 = AVLNode(2)
    avl_tree = AVLTree(node6)
    avl_tree.insert(node4)
    avl_tree.insert(node5)
    avl_tree.insert(node3)
    avl_tree.insert(node1)
    avl_tree.insert(node2)
    avl_tree.deleteMax()
    assert avl_tree.find(node2.val) is False and avl_tree.isAVL() is True


def test_deleteMin():
    node1 = AVLNode(3)
    node2 = AVLNode(237974)
    node3 = AVLNode(9)
    node4 = AVLNode(1)
    node5 = AVLNode(4)
    node6 = AVLNode(2)
    avl_tree = AVLTree(node6)
    avl_tree.insert(node4)
    avl_tree.insert(node5)
    avl_tree.insert(node3)
    avl_tree.insert(node1)
    avl_tree.insert(node2)
    avl_tree.deleteMin()
    assert avl_tree.find(node4.val) is False and avl_tree.isAVL() is True


def test_getMax():
    node1 = AVLNode(3)
    node2 = AVLNode(237974)
    node3 = AVLNode(9)
    node4 = AVLNode(1)
    node5 = AVLNode(4)
    node6 = AVLNode(2)
    avl_tree = AVLTree(node6)
    avl_tree.insert(node4)
    avl_tree.insert(node5)
    avl_tree.insert(node3)
    avl_tree.insert(node1)
    avl_tree.insert(node2)
    assert avl_tree.getMaxNode().val == 237974


def test_getMin():
    node1 = AVLNode(3)
    node2 = AVLNode(237974)
    node3 = AVLNode(9)
    node4 = AVLNode(1)
    node5 = AVLNode(4)
    node6 = AVLNode(2)
    avl_tree = AVLTree(node6)
    avl_tree.insert(node4)
    avl_tree.insert(node5)
    avl_tree.insert(node3)
    avl_tree.insert(node1)
    avl_tree.insert(node2)
    assert avl_tree.getMinNode().val == 1


def test_insert():
    node1 = AVLNode(6)
    node2 = AVLNode(3)
    node3 = AVLNode(2)
    node2.left = node3
    node2.right = node1
    avl_tree = AVLTree(node2)
    node4 = AVLNode(7)
    avl_tree.insert(node4)
    assert avl_tree.isAVL() is True and avl_tree.find(node4.val) is True and avl_tree.isBalanced() is True


def test_found():
    node1 = AVLNode(6)
    node2 = AVLNode(3)
    node3 = AVLNode(2)
    node2.left = node3
    node2.right = node1
    avl_tree = AVLTree(node2)
    node4 = AVLNode(7)
    avl_tree.insert(node4)
    assert avl_tree.find(2) is True


def test_notfound():
    node1 = AVLNode(6)
    node2 = AVLNode(3)
    node3 = AVLNode(2)
    node2.left = node3
    node2.right = node1
    avl_tree = AVLTree(node2)
    node4 = AVLNode(7)
    avl_tree.insert(node4)
    assert avl_tree.find(99) is False


def test_getAndUpdateHeight():
    node1 = AVLNode(6)
    node2 = AVLNode(3)
    node3 = AVLNode(2)
    before = node2.getHeight()
    node2.left = node3
    node2.right = node1
    avl_tree = AVLTree(node2)
    node4 = AVLNode(7)
    avl_tree.insert(node4)
    after = avl_tree.getRoot().getHeight()
    assert before == 1 and after == 3


def test_minDiff():
    node1 = AVLNode(3)
    node2 = AVLNode(237974)
    node3 = AVLNode(9)
    node4 = AVLNode(1)
    node5 = AVLNode(4)
    node6 = AVLNode(2)
    avl_tree = AVLTree(node6)
    avl_tree.insert(node4)
    avl_tree.insert(node5)
    avl_tree.insert(node3)
    avl_tree.insert(node1)
    avl_tree.insert(node2)
    assert avl_tree.getRoot().minDiff() == 1


def test_delete():
    node1 = AVLNode(4)
    node2 = AVLNode(5)
    node3 = AVLNode(3)
    node4 = AVLNode(1)
    node5 = AVLNode(9)
    avl_tree = AVLTree(node3)
    avl_tree.insert(node1)
    avl_tree.insert(node2)
    avl_tree.insert(node4)
    avl_tree.insert(node5)
    avl_tree.delete(node2.val)
    assert avl_tree.find(node2.val) is False and avl_tree.isAVL() is True and avl_tree.isBalanced() is True


def test_emptyInsert():
    avl_tree = AVLTree()
    node1 = AVLNode(2)
    node2 = AVLNode(3)
    avl_tree.insert(node1)
    avl_tree.insert(node2)
    assert avl_tree.find(node1.val) is True and avl_tree.find(node1.val) is True and avl_tree.isAVL() is True


def test_insertVal():
    avl_tree = AVLTree()
    node1 = AVLNode(2)
    node2 = AVLNode(3)
    avl_tree.insert(node1)
    avl_tree.insert(node2)
    avl_tree.insert_val(6)
    assert avl_tree.find(6) is True and avl_tree.isAVL() is True