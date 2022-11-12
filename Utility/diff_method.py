from Utility import ast_utility
class Diff_tree():
    def diff(a,b):
        return 1-ast_utility.diff(a.function_tree,b.function_tree)/a.function_tree_dim
    
    def count(a):
        return a.function_tree_dim
    

class Diff_embedding():
    def diff(a,b):
        return ast_utility.jaccard(a.function_embedding,b.function_embedding)

    def count(a):
        return sum(a.function_embedding.values())