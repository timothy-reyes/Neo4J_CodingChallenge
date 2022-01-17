#!/bin/bash
#build virtual env
python -m venv venv
#start virtual env
. venv/Scripts/activate
#install requirements
pip install Flask
pip install neo4j-driver
#setup flask API
export FLASK_APP=Neo4j_API.py
export FLASK_ENV=development
#start API service
flask run