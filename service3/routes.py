from flask import Flask, Response
import random 

@app.route('/type', methods=['GET'])
def type():
    types = ["Hatchback", "Saloon", "SUV",]
    type = random.choice(types)
    return Response(type, mimetype="text/plain")