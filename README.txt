run documentation

download Neo4J Desktop and import project #Tim needs to learn how to export a Neo4J project

download API project files
cd to project directory
python -m venv venv
. venv/Scripts/activate
pip install Flask
export FLASK_APP=Neo4j_API.py
export FLASK_ENV=development
flask run
pip install requirements.txt

