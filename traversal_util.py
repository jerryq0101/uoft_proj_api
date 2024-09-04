import neo4j
import itertools

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
            elif not node.children:
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


"""
Output nodes based on their verticies of connection
"""
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


"""
Commonality Algorithm

To mark the common courses between many different course trees.

Strategy:
- List of root nodes of all course trees 
- Find the list of course nodes that exist in every single course tree
- For every course node, see if that same code course node exists in any other course tree
    - set of unique course codes which map to a set containing the root nodes of the course trees that it exists in
- Take the intersection of the different sets
    - e.g. if I want to take the intersection of S_1, S_2. I will loop the map, and see if each item is in both S_1 and S_2
- Take every possible intersection of different sets and make a list of the data
- Filter for desired output

"""
def find_all_course_nodes(root: CourseNode):
    all_nodes = []

    def traverse(node):
        if node.label == "Course":
            all_nodes.append(node)
        for child in node.children:
            traverse(child)

    traverse(root)
    return all_nodes


def commonality_algorithm(root_nodes: list[CourseNode]):
    list_of_course_codes = {}
    
    # Each root_code: str -> all_course_nodes: list[CourseNode]
    for root in root_nodes:
        list_of_course_codes[root.code] = find_all_course_nodes(root)
    
    print(list_of_course_codes)

    unique_set_course_codes = {}

    # For each full list of course codes
    for root_code, lst in list_of_course_codes.items():
        
        # for each node in each full list of course codes
        #   
        for node in lst:
            
            if node.code not in unique_set_course_codes:
                unique_set_course_codes[node.code] = set()
            
            unique_set_course_codes[node.code].add(root_code)
    
    
    # filter the list of set size > 1
    filtered_unique_set_course_codes = {k: v for k, v in unique_set_course_codes.items() if len(v) > 1}
    
    # Take all possible intersections of commonalities (largest to smallest)
    combinations = {}
    pwr_to_sub = {}

    for code, root_set in filtered_unique_set_course_codes.items():

        # Put all possible subsets of root_set as keys
        root_pwr_set = powerset(root_set)
        
        # filter powerset to exclude length 1 and exclude itself
        filtered_root_pwr_set = [subset for subset in root_pwr_set if len(subset) > 1 and frozenset(subset) != frozenset(root_set)]
        
        pwr_to_sub[frozenset(root_set)] = filtered_root_pwr_set


        # Add code to each filtered_root_pwr_set and also the root (Since the power set excludes the root)
        for set_combo in filtered_root_pwr_set:
            f_set_combo = frozenset(set_combo)
            if f_set_combo not in combinations:
                combinations[f_set_combo] = set()
            
            combinations[f_set_combo].add(code)
        
        if frozenset(root_set) not in combinations:
            combinations[frozenset(root_set)] = set()
        combinations[frozenset(root_set)].add(code)

    print("Intersections and their course commonalities:", combinations)
    print("set to its powerset:")
    for k,v in pwr_to_sub.items():
        print (k, v)

    # Find the elements that appear in the root_set
    # Find elements that appear in each of the subsets 
    # if element appears in root_set AND subset, then delete the one in the subset
    for intersection, subsets in pwr_to_sub.items():
        if intersection in combinations:
            biggest_commonality = combinations[intersection]
            
            for subset in subsets:
                if frozenset(subset) in combinations:
                    smaller_commonality = combinations[frozenset(subset)]
                    # Remove courses from smaller_commonality that are in biggest_commonality
                    filtered_commonality = [course for course in smaller_commonality if course not in biggest_commonality]
                    if filtered_commonality:
                        combinations[frozenset(subset)] = filtered_commonality
                    else:
                        del combinations[frozenset(subset)]
    
    return construct_dict(convert_frozenset_serializable(combinations), check_containment(combinations))


def powerset(s):
    return [set(combo) for r in range(len(s) + 1) for combo in itertools.combinations(s, r)]


def construct_dict(commonality_dict, containment_relationships):
    return {
        "commonality_list": commonality_dict,
        "containment_dict": containment_relationships
    }
    

def convert_frozenset_serializable(combinations):
    # Combinations is a dict with frozenset keys and set values
    new_dict = {}
    for key, value in combinations.items():
        new_dict[str(list(key))] = list(value)
    
    return new_dict


def check_containment(combinations):
    
    containment_dict = {}
    
    for key, value in combinations.items():
        intersecting_courses = set(key)
        common_courses = value
        for item in intersecting_courses:
            if item in common_courses:
                # this means that all the other elements != item in intersecting courses contains course "item"
                # add containment notice into dict
                for other_course in intersecting_courses:
                    if other_course != item:
                        if other_course not in containment_dict:
                            containment_dict[other_course] = set()
                        containment_dict[other_course].add(item)
    
    
    converted_containment_dict = {}
    for key, value in containment_dict.items():
        converted_containment_dict[str(key)] = list(value)
    
    return converted_containment_dict