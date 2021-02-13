from flask import Flask, render_template, request, jsonify
from models.models import Guest
import json

app = Flask(__name__)


# basic route
@app.route('/')
def index():
    return jsonify({'hello': 'world'})

