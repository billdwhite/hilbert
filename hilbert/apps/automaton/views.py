import django
from django.template import Context, Template
from django.http import HttpResponse
import json
import random
from lib.automaton import trie

import logging
log = logging.getLogger(__name__)

DefaultN = 100

def index(request):
  t = django.template.loader.get_template("automaton.html")
  contextmap = {}
  contextmap["title"] = "Automaton"
  return HttpResponse(t.render(Context(contextmap)))

def data(request):
  M = trie.Trie(["aba", "aca"])
  return HttpResponse(json.dumps(M.getDict()), mimetype='application/json')
