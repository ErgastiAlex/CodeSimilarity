from Utility import ast_utility
from Utility import diff_method
import ast

def get_embedding(tree,num_of_embedding=5,use_split_embedding=False):
    if(use_split_embedding):
        embedding=ast_utility.ASTEmbeddingSplitNode(num_of_embedding)
    else:
        embedding = ast_utility.ASTEmbedding(num_of_embedding)
    embedding.visit(tree)
    return embedding.embeddings

def get_all_embeddings(tree_visitor,num_of_embedding=5,use_split_embedding=False):
    functions_embedding=[]
    functions_embedding.append(get_embedding(tree_visitor.global_code,num_of_embedding,use_split_embedding))

    for function in tree_visitor.function_list:
        functions_embedding.append(get_embedding(function,num_of_embedding,use_split_embedding))
    
    return functions_embedding

def get_all_trees(tree_visitor):
    trees=[]
    trees_dim=[]
    trees.append(tree_visitor.global_code)
    trees_dim.append(tree_visitor.global_code_node_count)
    for i in range(len(tree_visitor.function_list)):
        trees.append(tree_visitor.function_list[i])
        trees_dim.append(tree_visitor.function_node_count[i])
        
    return trees,trees_dim

class ParseException(Exception):
    pass

class FunctionRepresentation():
    def __init__(self, function_tree, function_tree_dim,function_embedding):
        self.function_embedding = function_embedding
        self.function_tree = function_tree
        self.function_tree_dim = function_tree_dim

class Code():
    def __init__(self,code_file,code_group="",code_name="",num_of_embedding=5,use_split_embedding=False):
        self.code_file=code_file
        self.code_group=code_group

        tree=None
        try:
            tree = ast.parse(code_file.read())
        except:
            raise ParseException("Error parsing code")
            
        tree_visitor=ast_utility.ASTParser()
        tree_visitor.visit(tree)

        self.__functions_representation=[]

        trees,trees_dim=get_all_trees(tree_visitor)
        embeddings=get_all_embeddings(tree_visitor,num_of_embedding,use_split_embedding)

        assert len(trees)==len(embeddings)
        assert len(trees)==len(trees_dim)

        for i in range(len(trees)):
            self.__functions_representation.append(FunctionRepresentation(trees[i],trees_dim[i],embeddings[i]))


    def get_trees(self):
        return [function_rep.function_tree for function_rep in self.__functions_representation]
    
    def get_trees_dim(self):
        return [function_rep.function_tree_dim for function_rep in self.__functions_representation]
    
    def get_embeddings(self):
        return [function_rep.function_embedding for function_rep in self.__functions_representation]


    def code_similarity(self,other_code,diff_class=diff_method.Diff_embedding):
        index=0
        functions_dim_count=[]
        functions_similarity=[]

        for function_rep in self.__functions_representation:
            max_similarity, max_simiarity_function2=Code.__get_most_similar_function(function_rep,other_code,diff_class)

            functions_dim_count.append(diff_class.count(function_rep))
            functions_similarity.append(max_similarity)

            index+=1
        
        return sum([f_sim*f_count for f_sim,f_count in zip(functions_similarity,functions_dim_count)])/sum(functions_dim_count)
    
    
    def __get_most_similar_function(function_rep,code,diff_class):
        max_similarity=0
        max_simiarity_function2=None

        for function2_rep in code.__functions_representation:

            similarity=diff_class.diff(function_rep,function2_rep)

            if(similarity>max_similarity):
                max_similarity=similarity
                max_simiarity_function2=function2_rep

        return max_similarity,max_simiarity_function2
