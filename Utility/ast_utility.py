import ast
import zss

#maybe rename??
class FunctionVisitor(ast.NodeTransformer):
    def __init__(self):
        self.node_number=0
        self.function_nodes = []  # List of function names
        self.class_list = []  # List of class names encapsulating functions

    def generic_visit(self, node):
        self.node_number+=1
        return super().generic_visit(node)

    def visit_ClassDef(self, node):
        # Add class name to list
        self.class_list.append(node.name)

        self.generic_visit(node)

        # Remove class name from list after visiting all children nodes
        self.class_list.pop()

    def visit_FunctionDef(self, node):
        # Rename the node using the class name encapsulating the hierarchy
        node.name = ".".join(self.class_list + [node.name])

        self.function_nodes.append(node)
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
  