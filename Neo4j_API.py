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
        with driver.session() as session:
            session.write_transaction(add_person, request.args.get("name") , request.args.get("emp_id"))
        #add_person(driver , request.args.get("name") , request.args.get("emp_id"))
        return {
            'message': 'This endpoint will create a new person. If the entered emp_id already exists in the database, the name associated to that emp_id will be updated',
            'method': request.method,
		    'body': request.values
        }
        driver.close()

    if request.method == "DELETE":
        with driver.session() as session:
            session.write_transaction(delete_persons)
        #add_person(driver , request.args.get("name") , request.args.get("emp_id"))
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

