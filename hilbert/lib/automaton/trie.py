
class State(object):
  def __init__(self, name):
    self.name = name
    self.targets = {}
    self.initial = False
    self.terminal = False
        
  def getStates(self):
    states = [{"name": self.name, "initial": self.initial, "terminal": self.terminal}]
    for a, state in self.targets.iteritems():
      states = states + state.getStates()
    return states;
  
  def getTransitions(self):
    transitions = []
    for a, state in self.targets.items():
      transitions.append({"source":self.name, "target": state.name, "input": a})
      transitions = transitions + state.getTransitions()
    return transitions

class Automaton(object):
  def __init__(self):
    self.stateCounter = 0
    self.initState = self.newState()
    self.initState.initial = True
    
  def getDict(self, state=None):
    if state is None: state = self.initState
    D = {"states": state.getStates(), "transitions": state.getTransitions()}
    return D
    
  def newState(self):
    s = State(self.stateCounter)
    self.stateCounter = self.stateCounter + 1
    return s
    
def Trie(X):
  M = Automaton()
  for x in X:
    t = M.initState
    for a in x:
      print t.name, a
      p = t.targets.get(a, None)
      if p is None:
        p = M.newState()
        t.targets[a] = p
      t = p
    t.terminal = True
    print "final"
  return M
    
if __name__ == "__main__":
  M = Trie(["aaab", "aabb", "aba", "bb"])
  import json
  print json.dumps(M.getDict())


