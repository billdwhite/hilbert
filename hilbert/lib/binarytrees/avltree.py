from bintree import BinaryTree, BinaryTreeNode

class AvlTreeNode(BinaryTreeNode):
  def __init__(self, tree, key, nil):
    super(AvlTreeNode, self).__init__(tree, key, nil)
    self.height = 1 if nil else 0 # if we are provided with a nil this node is not nil.

class AvlTree(BinaryTree):
  def __init__(self):
    super(AvlTree, self).__init__()

  def makeNode(self, key, nil):
    return AvlTreeNode(self, key, nil)

  def insert(self, key):
    z = super(AvlTree, self).insert(key)
    self.fixup(z.parent)
    return z

  def delete(self, z):
    z = super(AvlTree, self).delete(z)
    self.updateHeight(z.parent.left)
    self.updateHeight(z.parent.right)
    self.fixup(z.parent)
    return z
    
  def fixup(self, x):
    while x is not self.nil:
      self.updateHeight(x)
      balance = x.right.height - x.left.height
      if abs(balance) > 1:
        x = self.rotate(x, balance)
      else:
        x = x.parent
    return x
    
  def rotate(self, x, balance):
    if balance > 1:
      # right branch bigger
      if x.right.right.height - x.right.left.height < 0:
        # right left branch bigger
        self.rotateRight(x.right)
      self.rotateLeft(x)
    elif balance < -1:
      # left branch bigger
      if x.left.right.height - x.left.left.height > 0:
        # left right branch is bigger
        self.rotateLeft(x.left)
      self.rotateRight(x)
    
    self.updateHeight(x.parent.left)
    self.updateHeight(x.parent.right)
    self.updateHeight(x.parent)
    return x.parent

  def updateHeight(self, x):
    if x is not self.nil:
      x.height = max(x.left.height, x.right.height) + 1
    return x.height
    
  def calcHeights(self, x):
    if x is self.nil:
      return 0
    else:
      x.height = max(self.calcHeights(x.left), self.calcHeights(x.right)) + 1
      return x.height
    
  def verify(self):
    verified = True
    if self.root.left and not self.root.left.verify():
      return False
    if self.root.right and not self.root.right.verify():
      return False
    
    leftHeight = self.root.left.height if self.root.left else 0
    rightHeight = self.root.right.height if self.root.right else 0
    self.height = max(leftHeight, rightHeight) + 1
    self.balance = leftHeight - rightHeight
    if abs(self.balance) > 1:
      print "ERROR balance at node", self.root.data, "is", self.balance
      print self
      return False
    else:
      return True
      






