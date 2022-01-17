# Neo4J_CodingChallenge
Coding Challenge for Neo4J Interview

Requirements:
 - Active DBMS on neo4j://localhost:7687
 - Username: neo4j
 - Password: 123456

INSTRUCTIONS:
  1. immediately after cloning the repository, run setup.sh from the repository root directory
    - sets up python virtual env
    - activates virtual env
    - pip installs dependencies 
    - sets up Flask API environment variable requirements
    - runs Flask API service
    If successful, you should see "Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)"
  2. using your preferred HTTP request method (I used postman for testing) you have access to the following request options

  GET: http://localhost:5000/basic_api/persons
  - get a list of all currently registered persons


  PUT: http://localhost:5000/basic_api/persons?emp_id={{emp_num}}&name={{name}}
  - create new person. If emp_id already exists in the database, it will update the name associated with that emp_id rather than duplicate the record


  DELETE: http://localhost:5000/basic_api/persons
  - Deletes all persons in the DB. 