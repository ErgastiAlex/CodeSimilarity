import ast
from Utility import ast_utility
from Utility import ast_visualizer

ast_tree1 = ast.parse(open("Example/code_example.py").read())
ast_tree2 = ast.parse(open("Example/code_example2.py").read())
ast_tree3 = ast.parse(open("Example/code_example3.py").read())

tree1_visitor = ast_utility.FunctionVisitor()
tree1_visitor.visit(ast_tree1)

tree2_visitor = ast_utility.FunctionVisitor()
tree2_visitor.visit(ast_tree2)

tree3_visitor = ast_utility.FunctionVisitor()
tree3_visitor.visit(ast_tree3)

visualize=ast_visualizer.GraphVisualization("img/ast_tree1")
visualize.visit(tree1_visitor.function_nodes[0])
visualize.visualize()

visualize=ast_visualizer.GraphVisualization("img/ast_tree2")
visualize.visit(tree2_visitor.function_nodes[0])
visualize.visualize()

visualize=ast_visualizer.GraphVisualization("img/ast_tree3")
visualize.visit(tree3_visitor.function_nodes[0])
visualize.visualize()



embeddings1=ast_utility.ASTEmbedding(3)
embeddings1.visit(tree1_visitor.function_nodes[0])

embeddings2=ast_utility.ASTEmbedding(3)
embeddings2.visit(tree2_visitor.function_nodes[0])

embeddings3=ast_utility.ASTEmbedding(3)
embeddings3.visit(tree3_visitor.function_nodes[0])

tree_sim=1-ast_utility.diff(
    tree1_visitor.function_nodes[0], tree2_visitor.function_nodes[0])/tree1_visitor.node_number
jaccard_sim=ast_utility.jaccard(embeddings1.embeddings, embeddings2.embeddings)

print(f"Similarity with code 0 and 1, Jaccard_similarity: {round(jaccard_sim,2)}\t Tree_similarity: {round(tree_sim,2)}")

tree_sim=1-ast_utility.diff(
    tree2_visitor.function_nodes[0], tree3_visitor.function_nodes[0])/tree2_visitor.node_number
jaccard_sim=ast_utility.jaccard(embeddings2.embeddings, embeddings3.embeddings)

print(f"Similarity with code 1 and 2, Jaccard_similarity: {round(jaccard_sim,2)}\t Tree_similarity: {round(tree_sim,2)}")


import json
print(json.dumps(embeddings1.embeddings, indent=4))