# Prerequisite Visualizer (UofT) - Flask API


### API for processing frontend queries for course trees

---

### Table of Contents
- [Description](#description)
- [Files and Features](#Files-and-featuers)
- [Setup and Usage](#setup-and-usage)
- [Results and Understanding](#results-and-understanding)

---

### Description

This repository contains scripts that run a REST API to serve course queries to the database for the Frontend ReactJS application. These scripts are part of a larger project aimed at visualizing course prerequisites. (ADD LINKS TO OTHER REPOS)

### Files and features

- `app.py` is the main Flask Resource processing the requests
- `neo4j_conn.py` facilitates the initial Neo4j connection for the REST API
- `traversal_util.py` helps parse Neo4j data, and implements course commonality checking and marking completion

### Setup and Usage

These scripts only should be used if there exists a Neo4j database setup like in [here](https://github.com/jerryq0101/uoft_proj_data_collect).


Setup directory as below.
```
# Install Dependencies (pip or other)

Flask==3.0.3
Flask-RESTful==0.3.10
gunicorn==23.0.0
neo4j==5.23.1
python-dotenv==1.0.1
```

```
# In your .env file
N4J_DB_URI = "your neo4j database uri"
N4J_DB_PASS = "your neo4j database password"
```

Then, run app.py locally to test the API.

#### Example 1
Make a sample request:

PUT `http://127.0.0.1:5000/helloworld/john`
with the following body:
{
  name: "TEST"
  money: 100
  family: 100
}

#### Example 2

If you do have a Courses Neo4j instance set up like [this](https://github.com/jerryq0101/uoft_proj_data_collect?tab=readme-ov-file#loading-the-neo4j-database-with-course-data), then you can also try to GET the details of a specific course.

GET `http://127.0.0.1:5000/course/MAT240H1`

Should return 
`{"code": "MAT240H1", "full_name": "MAT240H1: Algebra I"}`

#### Example 3

You can also try out the POST method (using Postman or other)
POST `http://127.0.0.1:5000/course/`
With Body 
`{
    "completed_courses": ["MAT135H1"],
    "desired_courses": ["MAT337H1", "MAT157Y1"],
    "tree_choice": "full"}`

Should return:
`{
    "course_trees": [
        {
            "label": "Course",
            "marked": false,
            "ready_to_take": false,
            "completed": false,
            "code": "MAT337H1",
            "full_name": "MAT337H1: Introduction to Real Analysis",
            "children": ...`

### Results and Understanding

To briefly summarize for CourseQueries from the frontend:

a GET Request will make a simple Neo4j MATCH (:Course {code: $code}) query, returning a simple dict with course details.

a POST request will process the request body (completed_courses, desired_courses, and tree_choice) to compute common courses and mark completed courses, returning a nested dictionary with a tree structure.