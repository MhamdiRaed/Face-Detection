import networkx as nx
import matplotlib.pyplot as plt

def DFS(graph,start ,end):
    visited=set()
    stack=[start]
    while stack:
        current=stack.pop()
        if current ==end:
            return True 
        if current not in visited:
            visited.add(current)
            stack.extend([neighbor for neighbor in graph[current] if neighbor not in visited])
    return False


graph = {'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E'['H'],'F':[],'G':[],'H':[]}
start='A'
end='H'
if DFS(graph,start,end):
    print(f"{end} a ete trouve dans le graphe a partir de {start}")
else:
    print(f"{end} n a pas ete trouve dans le graphe a partir de {start}")


G = nx.Graph(graph)


nx.draw(G, with_labels=True)

plt.show()