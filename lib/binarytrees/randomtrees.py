from avltree import AvlTree
from bintree import BinaryTree
from redblacktree import RedBlackTree
import os, sys


def getEdges(tree, node):
  if node == tree.nil:
    return []
  else:
    nodes = [(node, node.left), (node, node.right)]
    nodes = nodes + getEdges(tree, node.left) + getEdges(tree, node  .right)
    return nodes

def writeDotGraph(out, tree):
  #if not tree.root.left and not tree.root.right:
  #  return out
  nilcounter = 0
  edges = getEdges(tree, tree.root)
  for x,y in edges:
    if y == tree.nil:
      nilcounter = nilcounter + 1
      ykey = '"NIL' + str(nilcounter) + '"'
      print >> out, ykey, '[shape=none, label=""];'
      print >> out, x.key, '->', ykey, '[style="invis"];'
    else:
      if hasattr(y, 'colour'):
        if y.colour:
          print >> out, y.key, '[color=RED];'
        else:
          print >> out, y.key, '[color=BLACK];'
      print >> out, x.key, '->', y.key, ';'
  
def printDotGraph(name, tree):
  f = open(name + ".dot", 'w')
  print >> f, 'digraph', name, '{'
  writeDotGraph(f, tree)
  print >> f, '}'
  f.close()
  os.system('dot ' + name + '.dot -Tsvg -o ' + name + '.svg')

  

import random

def run(trees, N):
  sofar = set()
  print "adding", N, "nodes"
  for i in range(N):
    x = random.randint(1,N*10)
    while x in sofar:
      x = random.randint(1,N*10)
    sofar.add(x)
    for name, tree in trees.items():
      tree.insert(x)
  for name, tree in trees.items():
    printDotGraph(name + "_before", tree)
  print "applying", N*100, "random insert and deletes"
  """
  for i in range(N*10):
    if i % 2 == 0:
      x = random.choice(list(sofar))
      sofar.remove(x)
      for name, tree in trees.items():
        tree.deleteByKey(x)
    else:
      x = random.randint(1,N*10)
      while x in sofar:
        x = random.randint(1,N*10)
      sofar.add(x)
      for name, tree in trees.items():
        tree.insert(x)
  for name, tree in trees.items():
    printDotGraph(name + "_after", tree)
  """

def randomTreeInserts(tree, N):
  sofar = set()
  print "adding", N, "nodes"
  keys = range(N)
  random.shuffle(keys)
  for key in keys:
    tree.insert(key)
  
def getDictTree(tree, node):
  children = []
  if node.left is not tree.nil or node.right is not tree.nil:
    for child in [node.left, node.right]:
      if child is not tree.nil:
        children.append(getDictTree(tree, child))
      else:
        children.append({"key":"none", "children":[]})
  nodedict = {}
  if hasattr(node, "colour"):
    nodedict["colour"] = node.colour
  nodedict["key"] = node.key
  nodedict["children"] = children
  return nodedict

if __name__ == "__main__":
  N = 300
  trees = {
    "bintree": BinaryTree(), 
    "redblacktree": RedBlackTree(),
    "avltree": AvlTree()
  }
  run(trees, 150)
  import json
  for name, tree in trees.items():
    f = open('/Users/tims/workspace/datavis/data/' + name + '.json','w')
    f.write(json.dumps(getDictTree(tree, tree.root), indent=True))
    f.close()

