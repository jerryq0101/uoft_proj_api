import neo4j

class CourseNode():
    """
    type: "AND" or "OR" or "Course"
    children: list of CourseNode objects
    
    code: the course code of the course
    full_name: the full name of the course
    """
    def __init__(self, label, code=None, full_name=None, index=None):
        if label == "OR":
            self.label = "OR"
            self.index = index
            self.code = None
            self.full_name = None
        elif label == "AND":
            self.label = "AND"
            self.index = index
            self.code = None
            self.full_name = None
        elif label == "Course":
            self.label = "Course"
            self.code = code
            self.full_name = full_name
            self.index = None

        self.marked = False
        self.completed = False
        self.ready_to_take = False

        self.children = []


    def add_child(self, child):
        self.children.append(child)


# """
# find_course_children

# - code: course code
# - full_name: full name of the course

# - tx: run this function using session

# 1. Finds children of a course node using neo4j
# 2. Then filters the output to become dictionaries 
#     - Course dicts: {
#         "label": "Course",
#         "code": $code,
#         "full_name": $full_name
#     }
#     - AND / OR dicts: {
#         "label": "AND",
#         "index": some_int
#     }
# 3. Returns the array full of them

# """
# def find_course_children(
#         tx, 
#         code: str, 
#         full_name: str, 
#         root_code: str
# ):
    
#     results = tx.run(
#         """
#             MATCH (c:Course {code: $code})-[:Contains {root: $root_code}]->(child)
#             RETURN child, labels(child) AS child_labels
#         """,
#         code=code,
#         root_code=root_code
#     )

#     results = results.value()

#     # There is no need to filter this one because a prerequisite can't have an unidentified relationship with another prerequisite

#     children_dicts = []
#     for item in results:
#         # Should I even filter this depending on the child?
#         f_set_label = list(item._labels)[0]
#         print(f_set_label)
#         if f_set_label == "AND" or f_set_label == "OR":
#             index = item._properties["index"]
#             print(index)
#             print(type(index))

#             children_dicts.append({
#                 "label": f_set_label,
#                 "index": index
#             })
#         elif f_set_label == "Course":
#             code = item._properties["code"]
#             full_name = item._properties["full_name"]
#             children_dicts.append({
#                 "label": "Course",
#                 "code": code,
#                 "full_name": full_name
#             })

#     return children_dicts
    

# def find_and_children(tx, label:str, index:int, root_code:str):
#     assert(label == "AND", "label should be AND")

#     results = tx.run(
#         """
#             MATCH (a:AND {index: $index})-[:Contains {root: $root}]->(child)
#             RETURN child, labels(child) AS child_labels
#         """,
#         index=index,
#         root=root_code
#     )
#     results = results.value()

#     children_dicts = []
#     for item in results:
#         # Should I even filter this depending on the child?
#         f_set_label = list(item._labels)[0]
#         print(f_set_label)
#         if f_set_label == "AND" or f_set_label == "OR":
#             index = item._properties["index"]
#             print(index)
#             print(type(index))

#             children_dicts.append({
#                 "label": f_set_label,
#                 "index": index
#             })
#         elif f_set_label == "Course":
#             code = item._properties["code"]
#             full_name = item._properties["full_name"]
#             children_dicts.append({
#                 "label": "Course",
#                 "code": code,
#                 "full_name": full_name
#             })

#     return children_dicts


# def find_or_children(tx, label, index, root_code):
#     assert(label == "OR", "label should be OR")

#     results = tx.run(
#         """
#             MATCH (o:OR {index: $index})-[:Contains {root: $root}]->(child)
#             RETURN child, labels(child) AS child_labels
#         """,
#         index=index,
#         root=root_code
#     )
#     results = results.value()

#     children_dicts = []
#     for item in results:
#         # Should I even filter this depending on the child?
#         f_set_label = list(item._labels)[0]
#         if f_set_label == "AND" or f_set_label == "OR":
#             index = item._properties["index"]
#             # print(index)
#             # print(type(index))

#             children_dicts.append({
#                 "label": f_set_label,
#                 "index": index
#             })
#         elif f_set_label == "Course":
#             code = item._properties["code"]
#             full_name = item._properties["full_name"]
#             children_dicts.append({
#                 "label": "Course",
#                 "code": code,
#                 "full_name": full_name
#             })

#     return children_dicts


dict_course = {}
dict_AND = {}
dict_OR = {}

dict_neo4j_all = {}

def create_full_tree_from_apoc(session, course_I_want: str):
    result = session.execute_read(run_apoc_query, course_I_want)

    for record in result:
                nodes = record["nodes"]
                relationships = record["relationships"]

                parsed_nodes = [parse_node(node) for node in nodes]
                parsed_relationships = [parse_relationship(rel) for rel in relationships]
                
                
                print("Nodes:")
                for node in parsed_nodes:
                    print(f"  ID: {node['id']}")
                    print(f"  Labels: {', '.join(node['labels'])}")
                    print(f"  Properties: {node['properties']}")
                    print()

                    # Operations
                    neo4j_id = node["id"]
                    node_label = node["labels"][0]
                    node_properties = node["properties"]
                    
                    if node_label == "Course":
                        code = node_properties["code"]
                        full_name = node_properties["full_name"]
                        course_node = CourseNode(
                            label="Course",
                            code=code,
                            full_name=full_name,
                            index=None
                        )
                        dict_course[code] = course_node
                        dict_neo4j_all[neo4j_id] = course_node
                    elif node_label == "AND":
                        index = node_properties["index"]
                        and_node = CourseNode(
                            label="AND",
                            code=None,
                            full_name=None,
                            index=index
                        )
                        dict_AND[index] = and_node
                        dict_neo4j_all[neo4j_id] = and_node
                    elif node_label == "OR":
                        index = node_properties["index"]
                        or_node = CourseNode(
                            label="OR",
                            code=None,
                            full_name=None,
                            index=index
                        )
                        dict_OR[index] = or_node
                        dict_neo4j_all[neo4j_id] = or_node

                print("Relationships:")
                for rel in parsed_relationships:
                    print(f"  ID: {rel['id']}")
                    print(f"  Type: {rel['type']}")
                    print(f"  Start Node: {rel['start_node']}")
                    print(f"  End Node: {rel['end_node']}")
                    print(f"  Properties: {rel['properties']}")
                    print()

                    # Operations
                    start_node_neo4j_id = rel["start_node"]
                    end_node_neo4j_id = rel["end_node"]

                    start_node_obj = dict_neo4j_all[start_node_neo4j_id]
                    end_node_obj = dict_neo4j_all[end_node_neo4j_id]

                    start_node_obj.add_child(end_node_obj)

    return dict_course[course_I_want]


def create_prerequisite_tree_from_apoc(session, course_I_want: str):
    result = session.execute_read(run_apoc_query_first_level, course_I_want)

    for record in result:
                nodes = record["nodes"]
                relationships = record["relationships"]

                parsed_nodes = [parse_node(node) for node in nodes]
                parsed_relationships = [parse_relationship(rel) for rel in relationships]
                
                
                print("Nodes:")
                for node in parsed_nodes:
                    print(f"  ID: {node['id']}")
                    print(f"  Labels: {', '.join(node['labels'])}")
                    print(f"  Properties: {node['properties']}")
                    print()

                    # Operations
                    neo4j_id = node["id"]
                    node_label = node["labels"][0]
                    node_properties = node["properties"]
                    
                    if node_label == "Course":
                        code = node_properties["code"]
                        full_name = node_properties["full_name"]
                        course_node = CourseNode(
                            label="Course",
                            code=code,
                            full_name=full_name,
                            index=None
                        )
                        dict_course[code] = course_node
                        dict_neo4j_all[neo4j_id] = course_node
                    elif node_label == "AND":
                        index = node_properties["index"]
                        and_node = CourseNode(
                            label="AND",
                            code=None,
                            full_name=None,
                            index=index
                        )
                        dict_AND[index] = and_node
                        dict_neo4j_all[neo4j_id] = and_node
                    elif node_label == "OR":
                        index = node_properties["index"]
                        or_node = CourseNode(
                            label="OR",
                            code=None,
                            full_name=None,
                            index=index
                        )
                        dict_OR[index] = or_node
                        dict_neo4j_all[neo4j_id] = or_node

                print("Relationships:")
                for rel in parsed_relationships:
                    print(f"  ID: {rel['id']}")
                    print(f"  Type: {rel['type']}")
                    print(f"  Start Node: {rel['start_node']}")
                    print(f"  End Node: {rel['end_node']}")
                    print(f"  Properties: {rel['properties']}")
                    print()

                    # Operations
                    start_node_neo4j_id = rel["start_node"]
                    end_node_neo4j_id = rel["end_node"]

                    start_node_obj = dict_neo4j_all[start_node_neo4j_id]
                    end_node_obj = dict_neo4j_all[end_node_neo4j_id]

                    start_node_obj.add_child(end_node_obj)

    return dict_course[course_I_want]


def run_apoc_query(tx, course_code: str):
    query = """
    MATCH (start:Course {code: $course_code})
    CALL apoc.path.subgraphAll(start, {
        relationshipFilter: "Contains>",
        labelFilter: "+Course|AND|OR"
    })
    YIELD nodes, relationships
    RETURN nodes, relationships
    """
    result = tx.run(query, course_code=course_code)
    return [record for record in result]


def run_apoc_query_first_level(tx, course_code: str):
    query = """
    MATCH (start:Course {code: $course_code})
    CALL apoc.path.subgraphAll(start, {
        relationshipFilter: "Contains>",
        labelFilter: "+Course|AND|OR"
    })
    YIELD nodes, relationships
    WITH nodes, [rel IN relationships WHERE type(rel) = 'Contains' AND rel.root = $course_code] AS filtered_relationships
    RETURN nodes, filtered_relationships AS relationships
    """
    result = tx.run(query, course_code=course_code)
    return [record for record in result]


def parse_node(node):
    return {
        "id": node.element_id,
        "labels": list(node.labels),
        "properties": dict(node)
    }


def parse_relationship(rel):
    return {
        "id": rel.element_id,
        "type": rel.type,
        "start_node": rel.nodes[0].element_id,
        "end_node": rel.nodes[1].element_id,
        "properties": dict(rel)
    }



"""
mark_completion
Check and mark the completion of a course and junction nodes.

"""
def mark_completion(root: CourseNode, completed_courses_list: list[str]):
    completed_courses = completed_courses_set(completed_courses_list)

    def mark_completed_courses(node: CourseNode):
        if node.label == "Course":
            node.completed = node.code in completed_courses
        for child in node.children:
            mark_completed_courses(child)

    def update_parents(node: CourseNode):
        # First, recursively update all children
        for child in node.children:
            update_parents(child)
        
        # Then, update the current node based on its children
        if node.label == "OR":
            node.marked = any(child.completed or child.marked for child in node.children)
        elif node.label == "AND":
            # This line marks the node as true if all children are either completed or marked
            # It doesn't restrict children to be only all marked or all completed
            # Instead, it allows for a mix of completed and marked children
            node.marked = all(child.completed or child.marked for child in node.children)
        elif node.label == "Course":
            # If a node has no children, it is ready to be taken
            # If a node has children and all the children are marked, then the course node is ready to be taken 
            if node.children:
                if all(child.completed or child.marked for child in node.children):
                    node.ready_to_take = True

    # Step 1: Mark completed courses
    mark_completed_courses(root)

    # Step 2: Update parent nodes from bottom up
    update_parents(root)


"""
completed_courses_set

simply converts the list of completed courses into a set. Used in mark_completion as a helper function
"""
def completed_courses_set(completed_courses_list: list[str]):
    completed_courses = set(completed_courses_list)
    return completed_courses


# BFS works on this, but still don't know how to do the proper visualization yet
def tree_visualization(root: CourseNode):
    # Create an empty queue and enqueue the root node
    queue = []
    queue.append((root, 0))

    while queue:
        # Dequeue a node from the front of the queue
        (node, count) = queue.pop(0)

        # # Print the label of the current node
        # print(node.label)

        if node.label == "Course":
            print(node.code, " - Level: ", count)
        elif node.label == "AND":
            print("AND" + " index: " + str(node.index), " - Level: ", count)
        elif node.label == "OR":
            print("OR" + " index: " + str(node.index), " - Level: ", count)

        # Enqueue all the children of the current node
        for child in node.children:
            queue.append((child, count+1))

        print("\n")


"""
Convert from CourseNode tree to a dictionary for JSON serialization
"""
def course_node_to_dict(node: CourseNode):
    node_dict = {
        "label": node.label,
        "marked": node.marked,
        "ready_to_take": node.ready_to_take,
        "completed": node.completed,
    }

    if node.label == "Course":
        node_dict["code"] = node.code
        node_dict["full_name"] = node.full_name
    else:
        node_dict["index"] = node.index
    
    if node.children:
        node_dict["children"] = []
        for child in node.children:
            node_dict["children"].append(course_node_to_dict(child))
    
    return node_dict


# """
# Commonality Algorithm

# Algorithm to find the top most common course nodes between different courses.

# CONSIDER (using the non full prerequisite tree instead to do these checks)  
# * Check if there are other optimizations

# TODO: For this
# - Does this commonality algorithm work in practice? Assumption of if its dominant node in one tree, does it mean its also dominant in the other tree?
# - The purpose of this is to find commonality between the prerequisites trees of different courses. Simple maybe best? 


# What I'd think the algorithm should be like:

# Get all CourseNodes in each tree via traversal.

# Nested for loops scan for commonality of courseNodes.code s 

# Check for containment (when n1 is an ancestor of n2 in both trees, which likely usually will be the case that containment will be parallel in different trees) 

# Logic for check for containment 

# - if containment and there is no other instance of n2 outside of n1: then safely discard n2 as a repetitive commonality course node

# - if contaiment and there are instances of n2 outside of n1: then mark n2 as a prerequisite of n1 but don't discard the commonality course node

# - "outside" is defined n1 being the ancestor of n2

# (Although I talk here as commonality lists in tree pairs, I would like there to full consideration of commonality lists for all trees. E.g. this node might appear in A B C, this node might appear in A C...)

# """

# from collections import defaultdict

# def get_all_course_nodes(root):
#     nodes = []
#     def traverse(node):
#         if node.label == "Course":
#             nodes.append(node)
#         for child in node.children:
#             traverse(child)
#     traverse(root)
#     return nodes

# def is_ancestor(ancestor, descendant):
#     if ancestor == descendant:
#         return True
#     for child in ancestor.children:
#         if is_ancestor(child, descendant):
#             return True
#     return False

# def get_commonality(trees):
#     all_nodes = {tree_name: get_all_course_nodes(tree) for tree_name, tree in trees.items()}
#     common_courses = defaultdict(lambda: {'nodes': [], 'trees': set()})

#     for tree_name, nodes in all_nodes.items():
#         for node in nodes:
#             common_courses[node.code]['nodes'].append(node)
#             common_courses[node.code]['trees'].add(tree_name)

#     # Filter out courses that appear in only one tree
#     common_courses = {code: data for code, data in common_courses.items() if len(data['trees']) > 1}

#     # Check for containment
#     for course, data in common_courses.items():
#         for tree_name in data['trees']:
#             nodes_in_tree = [node for node in data['nodes'] if node in all_nodes[tree_name]]
#             for i, node1 in enumerate(nodes_in_tree):
#                 for node2 in nodes_in_tree[i+1:]:
#                     if is_ancestor(node1, node2):
#                         # Check if node2 appears outside of node1 in any tree
#                         appears_outside = any(
#                             not is_ancestor(n1, n2) 
#                             for t in data['trees'] 
#                             for n1, n2 in zip(
#                                 [n for n in data['nodes'] if n in all_nodes[t] and n.code == node1.code],
#                                 [n for n in data['nodes'] if n in all_nodes[t] and n.code == node2.code]
#                             )
#                         )
#                         if not appears_outside:
#                             data['nodes'].remove(node2)
#                         else:
#                             node2.is_prerequisite_of = node1

#     return common_courses