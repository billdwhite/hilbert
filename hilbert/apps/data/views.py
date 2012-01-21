# Create your views here.
from django.http import HttpResponse
import json
from lib.binarytrees.bintree import BinaryTree
from lib.binarytrees.avltree import AvlTree
from lib.binarytrees.redblacktree import RedBlackTree
from lib.binarytrees import randomtrees

N = 100
def bintree_json(request):
  tree = BinaryTree()
  randomtrees.randomTreeInserts(tree, N)
  response_dict = randomtrees.getDictTree(tree, tree.root)
  return HttpResponse(json.dumps(response_dict), mimetype='application/json')
  
def avltree_json(request):
  tree = AvlTree()
  randomtrees.randomTreeInserts(tree, N)
  response_dict = randomtrees.getDictTree(tree, tree.root)
  return HttpResponse(json.dumps(response_dict), mimetype='application/json')

def redblacktree_json(request):
  tree = RedBlackTree()
  randomtrees.randomTreeInserts(tree, N)
  response_dict = randomtrees.getDictTree(tree, tree.root)
  return HttpResponse(json.dumps(response_dict), mimetype='application/json')
