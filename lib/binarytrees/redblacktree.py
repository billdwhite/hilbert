from bintree import BinaryTree, BinaryTreeNode

BLACK = 0
RED = 1

class RedBlackNode(BinaryTreeNode):
  def __init__(self, tree, key, nil):
    super(RedBlackNode, self).__init__(tree, key, nil)
    self.colour = BLACK
      
class RedBlackTree(BinaryTree):
  def __init__(self):
    super(RedBlackTree, self).__init__()

  def makeNode(self, key, nil):
    return RedBlackNode(self, key, nil)
  
  def insert(self, key):
    z = super(RedBlackTree, self).insert(key)
    z.colour = RED
    self.fixup(z)
    return z

  def delete(self, z):
    if z is self.nil:
      return z
    
    originalColour = z.colour
    if z.left is self.nil:
      x = z.right
      self.transplant(z, z.right)
    elif z.right is self.nil:
      x = z.left
      self.transplant(z, z.left)
    else:
      y = self.minimum(z.right)
      originalColour = y.colour
      x = y.right
      if y.parent is z:
        x.parent = y
      else:
        self.transplant(y, y.right)
        y.right = z.right
        y.right.parent = y
      self.transplant(z, y)
      y.left = z.left
      y.left.parent = y
      y.colour = z.colour
      
    if originalColour == BLACK:
      self.fixup(x)
    
  def fixup(self, z):
    # we have just inserted a red node, z
    while z.parent.colour == RED:
      # the operations are symmetric depending on if z.parent is a left or right child of z.parent.parent
      if z.parent is z.parent.parent.left:
        y = z.parent.parent.right
        if y.colour == RED:
          z.parent.colour = BLACK
          y.colour = BLACK
          z.parent.parent.colour = RED
          z = z.parent.parent
        else:
          if z is z.parent.left:
            z.parent.colour = BLACK
            z.parent.parent.colour = RED
            self.rotateRight(z.parent.parent)
          else:
            z = z.parent
            self.rotateLeft(z)
      else:
        y = z.parent.parent.left
        if y.colour == RED:
          z.parent.colour = BLACK
          y.colour = BLACK
          z.parent.parent.colour = RED
          z = z.parent.parent
        else:
          if z is z.parent.right:
            z.parent.colour = BLACK
            z.parent.parent.colour = RED
            self.rotateLeft(z.parent.parent)
          else:
            z = z.parent
            self.rotateRight(z)
    self.root.colour = BLACK
      
