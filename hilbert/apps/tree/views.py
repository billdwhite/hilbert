import django
from django.template import Context, Template
from django.http import HttpResponse
import json
from lib.binarytrees.bintree import BinaryTree
from lib.binarytrees.avltree import AvlTree
from lib.binarytrees.redblacktree import RedBlackTree
from lib.binarytrees import randomtrees

import logging
log = logging.getLogger(__name__)

DefaultN = 100
trees = {
  "binarysearchtree": BinaryTree,
  "avltree": AvlTree,
  "redblacktree": RedBlackTree
}

def index(request, treename="binarysearchtree", inserts=None, N=None):
  if N is None: N = DefaultN
  t = django.template.loader.get_template("tree.html")
  contextmap = {}
  contextmap["title"] = "Tree"
  contextmap["treename" ] = treename
  contextmap["num_nodes"] = N
  treenames = trees.keys()
  treenames.sort()
  contextmap["treenames"] = treenames
  return HttpResponse(t.render(Context(contextmap)))

def data(request, treename="binarysearchtree", inserts=None, N=None):
  if N is None: N = DefaultN
  tree = trees[treename]()
  if inserts is None:
    randomtrees.randomTreeInserts(tree, int(N))
  else:
    log.info(inserts)
    for x in inserts.split('.'):
      tree.insert(x)
  response_dict = randomtrees.getDictTree(tree, tree.root)
  return HttpResponse(json.dumps(response_dict), mimetype='application/json')
