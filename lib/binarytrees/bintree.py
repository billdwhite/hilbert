class BinaryTreeNode(object):
  def __init__(self, tree, key, nil):
    self.tree = tree    
    self.key = key
    self.parent = nil
    self.left = nil
    self.right = nil

class BinaryTree(object):
  def __init__(self):
    self.nil = self.makeNil()
    self.root = self.nil
  
  def makeNil(self):
    nil = self.makeNode("nil", None)
    nil.parent = nil
    nil.left = nil
    nil.right = nil
    return nil
    
  def makeNode(self, key, nil):
    node = BinaryTreeNode(self, key, nil)
    return node
  
  def insert(self, key):
    z = self.makeNode(key, self.nil)
    y = self.nil
    x = self.root
    while x is not self.nil:
      y = x
      if x.key == z.key: # we enforce unique keys
        return
      elif z.key < x.key:
        x = x.left
      else: # x.key > z.key
        x = x.right

    if y is self.nil:
      self.root = z
    elif z.key < y.key:
      y.left = z
    else:
      y.right = z
    z.parent = y
    return z
    
  def find(self, key):
    x = self.root
    while x is not self.nil and key != x.key:
      if key < x.key:
        x = x.left
      elif key > x.key:
        x = x.right
    return x

  def deleteByKey(self, key):
    x = self.find(key)
    self.delete(x)
    
  def delete(self, x):
    if x is self.nil:
      return x

    if x.left is self.nil:
      self.transplant(x, x.right)
    elif x.right is self.nil:
      self.transplant(x, x.left)
    else:
      y = self.minimum(x.right)
      if y.parent is not x:
        self.transplant(y, y.right)
        y.right = x.right
        y.right.parent = y
      self.transplant(x, y)
      y.left = x.left
      y.left.parent = y
    return x

  def minimum(self, x):
    y = x
    while x.left is not self.nil:
      y = x
      x = x.left
    return y

  def transplant(self, x, y):
    # move y to x and set the parent links properly.
    if x.parent is self.nil:
      self.root = y
    else:
      if x.parent.left is x:
        x.parent.left = y
      else:
        x.parent.right = y

    if y is not self.nil:
      y.parent = x.parent
      
  def rotateLeft(self, x):
    y = x.right
    x.right = y.left
    if y.left is not self.nil:
      y.left.parent = x

    y.parent = x.parent
    if x.parent is self.nil:
      self.root = y
    elif x.parent.left is x:
      x.parent.left = y
    else:
      x.parent.right = y

    y.left = x
    x.parent = y

  def rotateRight(self, y):
    x = y.left
    y.left = x.right
    if x.right is not self.nil:
      x.right.parent = y

    x.parent = y.parent
    if y.parent is self.nil:
      self.root = x
    elif y.parent.left is y:
      y.parent.left = x
    else:
      y.parent.right = x

    x.right = y
    y.parent = x  
        
  def verify(self, x, seenNodes=None):
    if seenNodes == None:
      seenNodes = []
    if x in seenNodes:
      raise Exception("Loop found. Already seen " + str(x.key) + ". Seen nodes = " + str(list(x.key for x in seenNodes)))
    else:
      seenNodes.append(x)
      if x.left is not self.nil:
        self.verify(x.left, seenNodes)
      if x.right is not self.nil:
        self.verify(x.right, seenNodes)
        
        