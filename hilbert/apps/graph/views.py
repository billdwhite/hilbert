import django
from django.template import Context, Template
from django.http import HttpResponse
import json
import random

import logging
log = logging.getLogger(__name__)

DefaultN = 100

def index(request):
  numnodes = request.GET.get("N", DefaultN)
  sequence = request.GET.get("seq", '')
  t = django.template.loader.get_template("graph.html")
  log.info(sequence)
  contextmap = {}
  contextmap["title"] = "Graph"
  return HttpResponse(t.render(Context(contextmap)))

def data(request):
  numnodes = request.GET.get("N", DefaultN)
  sequence = request.GET.get("seq", '')
  graph = {}
  nodes = list({"name":name,"group": name%5} for name in range(numnodes))
  links = []
  for i in range(numnodes):
    link = {}
    link['source'] = 0
    link['target'] = nodes[i]['name']
    link['value'] = random.choice(range(5)) + 1
    links.append(link)
  for i in range(numnodes):
    link = {}
    link['source'] = random.choice(nodes)['name']
    link['target'] = random.choice(nodes)['name']
    link['value'] = random.choice(range(5)) + 1
    links.append(link)
  graph['nodes'] = nodes
  graph['links'] = links
  
  return HttpResponse(json.dumps(graph), mimetype='application/json')
