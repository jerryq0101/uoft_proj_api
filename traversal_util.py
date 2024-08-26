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

        self.children = []


    def add_child(self, child):
        self.children.append(child)



def get_first_level_children(driver):
    """
    Returns the first level children of the root_code
    """
    driver.verify_connectivity()
    with driver.session(database="neo4j", default_access_mode=neo4j.READ_ACCESS) as session:
        
        # Get the first level children of the root_code
        # current_node = root
        result = session.run(
            """
            MATCH (c:Course {code: $code})-[:Contains {root: $code}]->(child)
            RETURN child, labels(child) AS child_labels
            """,
            code="MAT235Y1"
        )

        result = result.value()
        for item in result:
            f_set_label = list(item._labels)[0]
            print(f_set_label)
            index = item._properties["index"]
            print(index)
            print(type(index))


"""
find_course_children

- code: course code
- full_name: full name of the course

- tx: run this function using session

1. Finds children of a course node using neo4j
2. Then filters the output to become dictionaries 
    - Course dicts: {
        "label": "Course",
        "code": $code,
        "full_name": $full_name
    }
    - AND / OR dicts: {
        "label": "AND",
        "index": some_int
    }
3. Returns the array full of them

"""
def find_course_children(
        tx, 
        code: str, 
        full_name: str, 
        root_code: str
):
    
    results = tx.run(
        """
            MATCH (c:Course {code: $code})-[:Contains {root: $root_code}]->(child)
            RETURN child, labels(child) AS child_labels
        """,
        code=code,
        root_code=root_code
    )

    results = results.value()

    # There is no need to filter this one because a prerequisite can't have an unidentified relationship with another prerequisite

    children_dicts = []
    for item in results:
        # Should I even filter this depending on the child?
        f_set_label = list(item._labels)[0]
        print(f_set_label)
        if f_set_label == "AND" or f_set_label == "OR":
            index = item._properties["index"]
            print(index)
            print(type(index))

            children_dicts.append({
                "label": f_set_label,
                "index": index
            })
        elif f_set_label == "Course":
            code = item._properties["code"]
            full_name = item._properties["full_name"]
            children_dicts.append({
                "label": "Course",
                "code": code,
                "full_name": full_name
            })

    return children_dicts
    

def find_and_children(tx, label:str, index:int, root_code:str):
    assert(label == "AND", "label should be AND")

    results = tx.run(
        """
            MATCH (a:AND {index: $index})-[:Contains {root: $root}]->(child)
            RETURN child, labels(child) AS child_labels
        """,
        index=index,
        root=root_code
    )
    results = results.value()

    children_dicts = []
    for item in results:
        # Should I even filter this depending on the child?
        f_set_label = list(item._labels)[0]
        print(f_set_label)
        if f_set_label == "AND" or f_set_label == "OR":
            index = item._properties["index"]
            print(index)
            print(type(index))

            children_dicts.append({
                "label": f_set_label,
                "index": index
            })
        elif f_set_label == "Course":
            code = item._properties["code"]
            full_name = item._properties["full_name"]
            children_dicts.append({
                "label": "Course",
                "code": code,
                "full_name": full_name
            })

    return children_dicts


def find_or_children(tx, label, index, root_code):
    assert(label == "OR", "label should be OR")

    results = tx.run(
        """
            MATCH (o:OR {index: $index})-[:Contains {root: $root}]->(child)
            RETURN child, labels(child) AS child_labels
        """,
        index=index,
        root=root_code
    )
    results = results.value()

    children_dicts = []
    for item in results:
        # Should I even filter this depending on the child?
        f_set_label = list(item._labels)[0]
        if f_set_label == "AND" or f_set_label == "OR":
            index = item._properties["index"]
            # print(index)
            # print(type(index))

            children_dicts.append({
                "label": f_set_label,
                "index": index
            })
        elif f_set_label == "Course":
            code = item._properties["code"]
            full_name = item._properties["full_name"]
            children_dicts.append({
                "label": "Course",
                "code": code,
                "full_name": full_name
            })

    return children_dicts


"""
create_tree

Instance Variables: 
- parent_node: the parent node of the current node being processed
- root_code: the code of the course to start the traversal from
- type: AND v OR v Course

    # For a course:
    - code, full_name

    # For a junction:
    - index
"""
def create_tree(
        parent_node: CourseNode, 
        root_course_string: str,
        label: str,
        # For a course
        code: str,
        full_name: str,
        # For a AND OR (not sure if the type of index is a string or a thing )
        index: int,
        session,
    ):
    """
    Replicates the tree structure of the course prerequisites
    """

    # check if this is a junction or a course
        # if it is a course:
        # create a course code object, add it to the parent children list
        # Find its children and call this function for each child
            # Find its children by seeking the (c:Course {code: $code})-[:Contains {root: $root}]->(something) relationship 
            # do processing for the list of children

        # if it is a junction (AND / OR)
        # create a junction object, add it to the parent children list
        # Find its children and call this function for each child
            # Find its children by seeking the (a:AND {index: $index})-[:Contains {root: $root}]->(something) relationship
            # do processing for its children

    children_dicts = []

    common_node = None

    if label == "Course":
        # Current node
        course_node = CourseNode(label="Course", code=code, full_name=full_name, index=None)
        common_node = course_node

        # append it to the parent's array
        parent_node.children.append(course_node)

        # find its children
        # children_dicts should be objects with label, index (AND OR), code, full_name (Course). Selective based on type
        children_dicts = session.execute_read(
            find_course_children,
            code, 
            full_name, 
            root_course_string
        )

    elif label == "AND":
        # Current node
        and_node = CourseNode(label="AND", index=index, full_name=None, code=None)
        common_node = and_node

        # find its children dicts
        children_dicts = session.execute_read(
            find_and_children,
            label, 
            index,
            root_course_string
        )

    elif label == "OR":
        # Current node
        or_node = CourseNode(label="OR", index=index, full_name=None, code=None)
        common_node = or_node

        # append it parent's array
        parent_node.children.append(or_node)

        # find its children dicts
        children_dicts = session.execute_read(
            find_or_children,
            label, 
            index,
            root_course_string
        )

    if children_dicts: 
        # Process children dicts
        for child in children_dicts:
            if child["label"] == "AND" or child["label"] == "OR":
                create_tree(
                    parent_node=common_node, 
                    root_course_string=root_course_string, 
                    label=child["label"], 
                    code=None, 
                    full_name=None, 
                    index=child["index"],
                    session=session
                )
            elif child["label"] == "Course":
                create_tree(
                    parent_node=common_node, 
                    root_course_string=root_course_string, 
                    label=child["label"], 
                    code=child["code"], 
                    full_name=child["full_name"], 
                    index=None,
                    session=session
                )
    elif not children_dicts:
        # Start building the base node's prerequisites
        # If a Children dicts array has size 0, we need to start building the current node's prerequisites
        # the root node then switches to the current node and goes downward
        # I can handle this after building for the first level prerequisite

        # say I am at a leaf of the prerequisite tree
        parent_node = common_node
        root_course_string = code
        # a leaf cannot be a AND or OR. Thus, we try to find the course children
        children_dicts = session.execute_read(
            find_course_children,
            code, 
            full_name, 
            root_course_string
        )
        for child in children_dicts:
            if child["label"] == "AND" or child["label"] == "OR":
                create_tree(
                    parent_node=common_node, 
                    root_course_string=root_course_string, 
                    label=child["label"], 
                    code=None, 
                    full_name=None, 
                    index=child["index"],
                    session=session
                )
            elif child["label"] == "Course":
                create_tree(
                    parent_node=common_node, 
                    root_course_string=root_course_string, 
                    label=child["label"], 
                    code=child["code"], 
                    full_name=child["full_name"], 
                    index=None,
                    session=session
                )
        if not children_dicts:
            return


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
            # A course is marked if it's completed or if all its children are marked
            node.marked = node.completed or (node.children and all(child.marked for child in node.children))

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
Commonality Algorithm

Algorithm to find the top most common course nodes between different courses.

CONSIDER (using the non full prerequisite tree instead to do these checks) - it felt so slow ngl, 
* Check if there are other optimizations

TODO: For this
- Does this commonality algorithm work in practice? Assumption of if its dominant node in one tree, does it mean its also dominant in the other tree?
- The purpose of this is to find commonality between the prerequisites trees of different courses.


Logic: If at the top level there is common course node, then their children are also common, so we just care about the top level.

Actually here is what I need for a commonality algorithm.

Find the list of common nodes in CourseNode trees. (just do convert all a tree's node into list form, then do a set intersection)

Reduce common nodes between specific trees to the "dominant" nodes that cover the largest area for each tree.
(Effectively checking if different common nodes contain each other) 

Also check if one course tree contains another course tree entirely. => If it does its over. 

label these common nodes between specific trees unique colors

"""


# Example usage:
# trees = [course_a_tree, course_b_tree, course_c_tree]
# commonality = get_commonality(trees)
# for course, data in commonality.items():
#     print(f"Common course: {course}")
#     print(f"Color: RGB{data['color']}")
#     print(f"Appears in trees: {data['trees']}")
#     print("Nodes:", [node.code for node in data['nodes']])
#     print()

# Example usage:
# trees = [course_a_tree, course_b_tree, course_c_tree]
# course_names = ["Course A", "Course B", "Course C"]
# present_commonality(trees, course_names)