import ast
import zss

class ASTParser(ast.NodeTransformer):
    def __init__(self):
        self.global_code_node_count=0 #number of nodes in global code
        self.global_code=None #AST of the global code

        self.function_node_count=[] #Number of nodes in each function
        self.function_list = []  # List of function names

        self.class_list = []  # List of class names encapsulating functions



    def generic_visit(self, node):
        if len(self.function_list) == 0:
            self.global_code_node_count += 1
        else:
            self.function_node_count[-1] += 1
        return super().generic_visit(node)

    def visit_Module(self, node):
        self.global_code=node
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.global_code.body.remove(node)
        
        # Add class name to list
        self.class_list.append(node.name)

        self.generic_visit(node)

        # Remove class name from list after visiting all children nodes
        self.class_list.pop()

    def visit_FunctionDef(self, node):
        # Rename the node using the class name encapsulating the hierarchy
        node.name = ".".join(self.class_list + [node.name])

        self.function_list.append(node)
        self.function_node_count.append(0)

        self.generic_visit(node)

    def visit_Name(self, node):
        del node.id
        del node.ctx
        self.generic_visit(node)
        return node

    def visit_Subscript(self, node):
        del node.slice
        del node.ctx
        #Remove the node "name" from subscript if it is the only child
        if(isinstance(node.value,ast.Name)):
            del node.value
        self.generic_visit(node)
        return node

    def visit_args(self,node):
        del node.vararg
        del node.kwarg
        del node.defaults
        del node.kwonlyargs
        del node.kw_defaults
        self.generic_visit(node)
        return node


class ASTEmbedding(ast.NodeVisitor):
    def __init__(self,k):
        self.k=k
        self.embeddings = dict()
        self.current_embedding_nodes = []
        self.current_embedding = ""

    def generic_visit(self, node):
        self.current_embedding_nodes.append(type(node).__name__)
        super().generic_visit(node)
        embedding = ".".join(self.current_embedding_nodes[-self.k:])
        if(len(self.current_embedding_nodes)>=self.k):
            self.embeddings[embedding] = self.embeddings.get(embedding, 0) + 1
        self.current_embedding_nodes.pop()

class ASTEmbeddingSplitNode(ast.NodeVisitor):
    def __init__(self,k):
        self.k=k
        self.embeddings = dict()
        self.child_count = []
        self.current_embedding_nodes = []
        self.current_embedding = ""

    def generic_visit(self, node):
        self.current_embedding_nodes.append(type(node).__name__)

        self.child_count.append(len(list(ast.iter_child_nodes(node))))

        if(self.child_count[-1]>1):
            self.current_embedding_nodes.append("SplitNode")
        
        super().generic_visit(node)

        if(len(self.current_embedding_nodes)>=self.k):
            embedding = ".".join(self.current_embedding_nodes[-self.k:])
            self.embeddings[embedding] = self.embeddings.get(embedding, 0) + 1
        
        self.current_embedding_nodes.pop()
        if(self.child_count[-1]>1):
            self.current_embedding_nodes.pop()
        self.child_count.pop()


def diff(a, b):
    assert a is not None
    assert b is not None
    def _str_dist(i, j):
        return 0 if i == j else 1
    def _get_label(n):
        return type(n).__name__
    def _get_children(n):
        if not hasattr(n, 'children'):
            n.children = list(ast.iter_child_nodes(n))
        return n.children
    

    res = zss.simple_distance(
        a, b, get_children=_get_children, get_label=_get_label)
    return res

def jaccard(x, y) -> int:
    num = 0.0
    den = 0.0

    keys = x.keys() | y.keys()

    for k in keys:
        m1 = x.get(k,0)
        m2 = y.get(k,0)

        num += min(m1, m2)
        den += max(m1, m2)

    return num/den





  