import pandas as pd
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Read the Excel file
df = pd.read_excel('clients.xlsx')

# Convert DataFrame to dictionary
data = df.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clients')
def get_clients():
    return jsonify(data)

@app.route('/search')
def search_clients():
    query = request.args.get('q')
    if query:
        filtered_data = [client for client in data if query.lower() in str(client['Name']).lower() or query.lower() in str(client['VoterID']).lower()]
    else:
        filtered_data = data
    return jsonify(filtered_data)

