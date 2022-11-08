import ast
from Utility import ast_utility
from Utility import ast_visualizer

ast_tree1 = ast.parse(open("Example/code_example4.py").read())
ast_tree2 = ast.parse(open("Example/code_example2.py").read())
tree1_visitor = ast_utility.FunctionVisitor()
tree1_visitor.visit(ast_tree1)

tree2_visitor = ast_utility.FunctionVisitor()
tree2_visitor.visit(ast_tree2)
print(1-ast_utility.diff(
    tree1_visitor.function_nodes[0], tree2_visitor.function_nodes[0])/tree1_visitor.node_number)
    

visualize=ast_visualizer.GraphVisualization("ast_tree1")
visualize.visit(tree1_visitor.function_nodes[0])
visualize.visualize()

visualize=ast_visualizer.GraphVisualization("ast_tree2")
visualize.visit(tree2_visitor.function_nodes[0])
visualize.visualize()