#from v - apt install python3-graphviz
#normal - pip install graphviz

from graphviz import Digraph

def generate_graph():
    dot = Digraph()

    # Define nodes
    dot.node('A', 'Input Text')
    dot.node('B', 'Split Text into Words')
    dot.node('C', 'Word <= 3 Characters\nUppercase')
    dot.node('D', 'Word > 3 Characters\nRemove Vowels')
    dot.node('E', 'Transformed Words List')
    dot.node('F', 'Join Words into String')
    dot.node('G', 'Output Text')

    # Define edges
    dot.edge('A', 'B')
    dot.edge('B', 'C', label='if len(word) <= 3')
    dot.edge('B', 'D', label='if len(word) > 3')
    dot.edge('A', 'E')
    dot.edge('B', 'E')
    dot.edge('F', 'E')
    dot.edge('F', 'A')    
    dot.edge('C', 'E')
    dot.edge('D', 'E')
    dot.edge('E', 'F')
    dot.edge('F', 'G')

    return dot

# Generate and render the graph
graph = generate_graph()
graph.render('comprehension_graph', format='png', view=True)

