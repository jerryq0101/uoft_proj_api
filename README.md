# Prerequisite Visualizer (UofT) - Flask API


### API for processing frontend queries for course trees

---

### Table of Contents
- [Description](#description)
- [Files](#files)
- [Key Features](#key-features)
- [Setup and Usage](#setup-and-usage)
  - [Dependencies](#dependencies)
  - [Scraping](#scraping)
  - [Loading the Neo4j Database](#loading-the-neo4j-database-with-course-data)
- [Results and Understanding](#results-and-understanding)

---

#### Description

This repository contains scripts that run a REST API to serve course queries to the database for the Frontend ReactJS application. These scripts are part of a larger project aimed at visualizing course prerequisites. (ADD LINKS TO OTHER REPOS)

#### Files

- `app.py` is the main Flask Resource processing the requests
- `neo4j_conn.py` facilitates the initial Neo4j connection for the REST API
- `traversal_util.py` helps parse Neo4j data, and implements course commonality checking and marking completion

