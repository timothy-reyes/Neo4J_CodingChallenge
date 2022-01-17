# main.py
from flask import Flask, request
from neo4j import GraphDatabase
app = Flask(__name__)
driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "123456"))

@app.route('/basic_api/persons', methods=['GET', 'PUT', 'DELETE'])
def entities():
    if request.method == "GET":
        with driver.session() as session:
            body = session.read_transaction(get_persons)
        return {
            'body': body,
            'message': 'This endpoint should return a list of all persons',
            'method': request.method
        }
        driver.close()

    if request.method == "PUT":
        try:
            with driver.session() as session:
                emp_id = request.args.get("emp_id")
                name = request.args.get("name")
                session.write_transaction(add_person, name , emp_id)
                message = f"Person {emp_id} was created/updated with the name {name}"
        except:
            message = "Invalid request params. This PUT request requires a 'name' and an 'emp_id'"
        return {
            'message': message,
            'method': request.method,
		    'body': request.values
        }
        driver.close()

    if request.method == "DELETE":
        with driver.session() as session:
            session.write_transaction(delete_persons)
        return {
            'message': 'Database Wiped',
            'method': request.method,
		    'body': request.values
        }
        driver.close()


def add_person(tx, name, emp_id):
    tx.run("MERGE (n:Person {emp_id: $emp_id}) "
    	   "ON CREATE SET n.name = $name "
    	   "ON MATCH SET n.name = $name ",
           name=name, emp_id=emp_id)

def delete_persons(tx):
    tx.run("MATCH (n) WHERE (n:Person) DETACH DELETE n")
    return "Database Cleared"


def get_persons(tx):
    result = tx.run("MATCH (a:Person) RETURN a.name , a.emp_id ORDER BY a.emp_id")
    return ["name: " + record["a.name"] + " emp_id: " + record["a.emp_id"] for record in result]

