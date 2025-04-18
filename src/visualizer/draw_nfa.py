from graphviz import Digraph

def draw_nfa(nfa, filename='nfa_graph'):
    
    dot = Digraph(format='png')
    dot.attr(rankdir='LR') 

    state_id_map = {}  
    state_counter = [0]


    def get_id(state):
        if state not in state_id_map:
            state_id_map[state] = f"S{state_counter[0]}"
            state_counter[0] += 1
        return state_id_map[state]

    visited = set()
    stack = [nfa.initial]

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)

        curr_id = get_id(current)
        for label, target in [(current.label if current.label else 'ε', current.edge1), ('ε', current.edge2)]:
            if target:
                target_id = get_id(target)
                dot.edge(curr_id, target_id, label=label)
                stack.append(target)

  
    for state, sid in state_id_map.items():
        if state == nfa.accept:
            dot.node(sid, shape='doublecircle')
        else:
            dot.node(sid, shape='circle')

    dot.node('start', shape='point')
    dot.edge('start', get_id(nfa.initial), label='start')

    dot.render(filename, view=True) 