class AVLNode():
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        if self.right is None and self.left is None:
            self.height = 1
        else:
            self.height = max(self.left.getHeight() if self.left else 0, self.right.getHeight() if self.right else 0) + 1

    def getHeight(self) -> int:
        if self is None:
            return 0
        return self.height

    def updateHeight(self) -> None:
        self.height = 1 + max(self.right.getHeight() if self.right else 0, self.left.getHeight() if self.left else 0)

    def getDiff(self) -> int:
        left_diff = self.left.getHeight() if self.left else 0
        right_diff = self.right.getHeight() if self.right else 0
        return left_diff - right_diff

    def minDiff(self) -> int:
        return self.__minDiff(self)

    def __minDiff(self, tmp):
        if tmp is None:
            return float('inf')
        left_diff = self.__minDiff(tmp.left)
        right_diff = self.__minDiff(tmp.right)
        left_val = tmp.left.val if tmp.left else float('inf')
        right_val = tmp.right.val if tmp.right else float('inf')
        return min(left_diff, right_diff, abs(left_val - tmp.val), abs(right_val - tmp.val))

    def __str__(self):
        if self.left is None and self.right is None:
            return f"Node: {self.val}"
        if self.left is None:
            return f"Node: {self.val}, Right child: {self.right.val}"
        if self.right is None:
            return f"Node: {self.val}, Left child: {self.left.val}"
        return f"Node: {self.val}, Left child: {self.left.val} and right child: {self.right.val}"


class Tree:
    def __init__(self, root) -> None:
        self.root = root

    def in_order_traversal(self, tmp):
        if tmp is None:
            return []
        left_result = self.in_order_traversal(tmp.left)
        right_result = self.in_order_traversal(tmp.right)
        return left_result + [tmp] + right_result

    def pre_order_traversal(self, tmp):
        if tmp is None:
            return []
        left_result = self.in_order_traversal(tmp.left)
        right_result = self.in_order_traversal(tmp.right)
        return [tmp] + left_result + right_result

    def post_order_traversal(self, tmp):
        if tmp is None:
            return []
        left_result = self.in_order_traversal(tmp.left)
        right_result = self.in_order_traversal(tmp.right)
        return left_result + right_result + [tmp]

    def isBalanced(self) -> bool:
        return self.__isBalanced(self.root)

    def __isBalanced(self, tmp) -> bool:
        if not tmp:
            return True
        left_height = tmp.left.getHeight() if tmp.left else 0
        right_height = tmp.right.getHeight() if tmp.right else 0
        if abs(left_height - right_height) <= 1 and self.__isBalanced(tmp.left) and self.__isBalanced(tmp.right):
            return True
        return False

    def isAVL(self) -> bool:
        return self.__isAVL(self.root)

    def __isAVL(self, tmp) -> bool:
        if tmp is None:
            return True

        if not self.isBalanced():
            return False

        if (tmp.left and tmp.left.val > tmp.val) or (tmp.right and tmp.right.val < tmp.val):
            return False

        return self.__isAVL(tmp.left) and self.__isAVL(tmp.right)


class AVLTree(Tree):
    def __init__(self, root=None):
        if Tree(root).isAVL() or root is None:
            self.root = root
        else:
            raise ValueError("Can't make an AVL-tree from non balanced root")

    def getRoot(self) -> AVLNode:
        return self.root

    def leftRotate(self, node) -> AVLNode:
        x = node.right
        node.right = x.left if x else None

        if x: x.left = node

        node.updateHeight()
        if x: x.updateHeight()

        return x

    def rightRotate(self, node) -> AVLNode:
        x = node.left
        node.left = x.right if x else None

        if x: x.right = node

        node.updateHeight()
        if x: x.updateHeight()

        return x

    def rightBigRotate(self, node) -> AVLNode:
        node.left = self.leftRotate(node.left)
        return self.rightRotate(node)

    def leftBigRotate(self, node) -> AVLNode:
        node.right = self.rightRotate(node.right)
        return self.leftRotate(node)

    def insert_val(self, val) -> None:
        new_node = AVLNode(val)
        self.root = self.__insert(self.root, new_node)

    def insert(self, node) -> None:
        self.root = self.__insert(self.root, node)

    def __insert(self, node: AVLNode, new_node: AVLNode) -> AVLNode:
        if node is None:
            return new_node

        if new_node.val < node.val:
            node.left = self.__insert(node.left, new_node)
        else:
            node.right = self.__insert(node.right, new_node)

        if node.left:
            node.left.updateHeight()
        if node.right:
            node.right.updateHeight()

        node.updateHeight()
        diff = node.getDiff()

        if diff > 1:
            # Левое поддерево дисбалансировано
            if new_node.val < node.left.val:
                return self.rightRotate(node)  # правое вращение
            elif new_node.val >= node.left.val:
                return self.rightBigRotate(node)  # большой левый поворот

        if diff < -1:
            # Правое поддерево дисбалансировано
            if new_node.val > node.right.val:
                return self.leftRotate(node)  # левое вращение
            elif new_node.val <= node.right.val:
                return self.leftBigRotate(node)  # большой правый поворот

        return node

    def getBalance(self) -> bool:
        return self.root.getDiff()

    def getMinNode(self) -> AVLNode:
        return self.__getMinNode(self.root)

    def __getMinNode(self, tmp: AVLNode) -> AVLNode:
        if tmp is None or tmp.left is None:
            return tmp

        return self.__getMinNode(tmp.left)

    def getMaxNode(self) -> AVLNode:
        return self.__getMaxNode(self.root)

    def __getMaxNode(self, tmp: AVLNode) -> AVLNode:
        if tmp is None or tmp.right is None:
            return tmp

        return self.__getMaxNode(tmp.right)

    def find(self, key: int) -> bool:
        return self.__find(self.root, key)

    def __find(self, node: AVLNode, key: int) -> bool:
        if node is None:
            return False
        if key < node.val:
            return self.__find(node.left, key)
        elif key > node.val:
            return self.__find(node.right, key)
        else:
            return True

    def deleteMax(self) -> None:
        tmp = self.getMaxNode()
        if tmp is not None:
            self.root = self.__delete(self.root, tmp.val)
        else:
            raise KeyError("Element not found")

    def deleteMin(self) -> None:
        tmp = self.getMinNode()
        if tmp is not None:
            self.root = self.__delete(self.root, tmp.val)
        else:
            raise KeyError("Element not found")

    def delete(self, key: int) -> None:
        if self.find(key):
            self.root = self.__delete(self.root, key)
        else:
            raise KeyError(f"Key {key} not found")

    def __delete(self, node: AVLNode, key: int) -> AVLNode:
        if node is None:
            raise KeyError(f"Key {key} not found")

        if key < node.val:
            node.left = self.__delete(node.left, key)
        elif key > node.val:
            node.right = self.__delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self.__getMinNode(node.right)
            min_val = min_node.val
            node.val = min_val
            node.right = self.__delete(node.right, min_val)

        node.updateHeight()
        diff = node.getDiff()

        if diff > 1:
            # Левое поддерево дисбалансировано
            if node.left.getDiff() >= 0:
                return self.rightRotate(node)  # правое вращение
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)  # лево-право поворот

        if diff < -1:
            # Правое поддерево дисбалансировано
            if node.right.getDiff() >= 0:
                return self.leftRotate(node)  # левое вращение
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)  # право-лево поворот

        return node

    def __str__(self) -> str:
        str_arr = [[] for _ in range(self.root.getHeight())]
        self.__str__helper(self.root, str_arr, 0)
        str_arr = ["; ".join(elem) for elem in str_arr]
        return '\n'.join(str_arr)

    def __str__helper(self, tmp: AVLNode, str_arr: list[list[str]], level: int) -> None:
        if tmp is not None:
            str_arr[level].append(str(tmp))
            self.__str__helper(tmp.left, str_arr, level + 1)
            self.__str__helper(tmp.right, str_arr, level + 1)
        return
