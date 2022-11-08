# from https://github.com/pombredanne/python-ast-visualizer/blob/master/astvisualizer.py
import ast
import graphviz as gv
import subprocess
import numbers
import re
from uuid import uuid4 as uuid
import optparse
import sys
import pydot 

class GraphVisualization(ast.NodeVisitor):
    def __init__(self,graph_name="", graph_type="graph", graph_format="png"):
        self.graph_name = graph_name
        self.graph=pydot.Dot(graph_name, graph_type=graph_type)
        self.parent=[]
        self.node_counter=0
    
    def generic_visit(self, node):
        graph_node = pydot.Node(self.node_counter, label=node.__class__.__name__)
        self.graph.add_node(graph_node)
        if self.parent:
            self.graph.add_edge(pydot.Edge(self.parent[-1], graph_node))
        self.node_counter+=1
        self.parent.append(graph_node)
        
        super().generic_visit(node)
        self.parent.pop()
    
    def visualize(self):
        self.graph.write_png(self.graph_name+".png")
        try:
            subprocess.Popen(['xdg-open', '..\test.png'])
        except:
            pass
        
