from flask import Flask, Response
import random 

@app.route('/model', methods=['GET', 'POST'])
def model():