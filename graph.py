import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import math

def draw_graph(graph, labels=None, graph_layout='spring',
               node_size=500, node_color='blue', node_alpha=0.5,
               node_text_size=5, edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3, text_font='sans-serif'):

    G=nx.Graph()

    for edge in graph:
        G.add_edge(edge[0], edge[1])

    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)

    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, alpha=node_alpha, node_color=node_color, cmap=plt.cm.Blues)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness, alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G,graph_pos,font_size=node_text_size, font_family=text_font)

    if labels is None:
        labels = range(len(graph))
        print(labels)
    plt.show()

from load_data import get_movies
df = get_movies()
cur_df = df[df.Year == 2018]
cur_df.set_index('TMDB_ID')
graph = []
b_vals = []
for (index, row) in cur_df.iterrows():
    cur_tmbd = row['TMDB_ID']
    colour = row['Bechdel_Rating']
    recs = row['Recommendations']
    for rec in recs:
        graph.append((cur_tmbd,rec))
        b_vals.append(str(colour))

draw_graph(graph)

