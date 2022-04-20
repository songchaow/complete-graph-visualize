import graphviz
import numpy as np
import cmath

# an example graph
graph_matrix = np.random.rand(20,20)

node_labels = np.random.rand(20)

def float_to_color(a:float):
    theta = a * np.pi / 2
    # return cmath.sin(theta), cmath.cos(theta), 1.0
    
    # use HSV color instead
    return "{:.3f}".format(a) + " 1.000 1.000"
    
def float_to_color2(a:float):
    theta = a * np.pi / 2
    # return cmath.sin(theta), cmath.cos(theta), 1.0
    
    # use HSV color instead
    return "{:.3f}".format(a) + " 1.000 0.5"

g = graphviz.Digraph('G', filename='hello.gv')

# globa attributes
g.attr(scale='3')

# create nodes
for node_idx, node_label in enumerate(node_labels):
    color_rgb = float_to_color(node_label)  
    # set the attribute of the current node
    g.attr('node', shape='circle', fontsize='5', margin="0,0", width="0.1", height="0.1")
    g.attr('node', color=color_rgb)
    # create node
    # g.node(str(node_idx), str(node_label))
    g.node(str(node_idx))


# create edges
for (idx_start,idx_end), val in np.ndenumerate(graph_matrix):
    #  set the attribute of the current edge (mainly to alter the edge width)
    # g.attr(size='0.5')

    # create edge
    # g.edge(str(idx_start),str(idx_end), label=str(val))
    color_rgb2 = float_to_color2(val)
    g.attr('edge', arrowsize='0.05', penwidth=str(0.2*val), color=color_rgb2)
    g.edge(str(idx_start),str(idx_end))


with open('graph.dot', 'w') as f:
    f.write(g.source)

# TODO:
# 1. 箭头本身实心 减小大小，最好去掉
# 2. 字体变小
# 3. 研究一下线的厚度， size好像是全局？？