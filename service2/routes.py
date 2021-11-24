from flask import Flask, Response
import random 
	
@app.route('/make', methods=['GET'])
def make():
    makes = ["BMW", "Mercedes", "Audi",]
    make = random.choice(makes)
    return Response(make, mimetype="text/plain")