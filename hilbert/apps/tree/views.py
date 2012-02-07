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

def index(request, treename="binarysearchtree"):
  numnodes = request.GET.get("N", DefaultN)
  sequence = request.GET.get("seq", '')
  t = django.template.loader.get_template("tree.html")
  log.info(sequence)
  contextmap = {}
  contextmap["title"] = "Tree"
  contextmap["treename" ] = treename
  contextmap["sequence"] = sequence
  contextmap["numnodes"] = numnodes
  treenames = trees.keys()
  treenames.sort()
  contextmap["treenames"] = treenames
  return HttpResponse(t.render(Context(contextmap)))

def data(request, treename="binarysearchtree"):
  numnodes = request.GET.get("N", DefaultN)
  sequence = request.GET.get("seq", '')
  tree = trees[treename]()
  if len(sequence) > 0:
    log.info(sequence)
    for x in sequence.split(','):
      tree.insert(int(x))
  else:
    randomtrees.randomTreeInserts(tree, int(numnodes))
  response_dict = randomtrees.getDictTree(tree, tree.root)
  
  return HttpResponse(json.dumps(response_dict), mimetype='application/json')
