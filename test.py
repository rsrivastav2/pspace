from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    selected_value = request.args.get('selected')  # Get the selected value from the query parameters

    if selected_value == 'option1':
        data = [{'id': 1, 'name': 'Result 1'}, {'id': 2, 'name': 'Result 2'}]
    elif selected_value == 'option2':
        data = [{'id': 3, 'name': 'Result 3'}, {'id': 4, 'name': 'Result 4'}]
    else:
        data = []

    return jsonify(data)
