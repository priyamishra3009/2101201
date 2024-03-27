import requests
from flask import Flask, jsonify

app = Flask(__name__)

WINDOW_SIZE = 10
stored_numbers = []

def fetch_numbers_from_third_party(number_id):
    url = f"http://20.244.56.144/test/{number_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def calculate_average_of_numbers(numbers_list):
    numbers_list = [int(num) for num in numbers_list]
    if len(numbers_list) == 0:
        return None
    return sum(numbers_list) / len(numbers_list)

def update_and_get_states_for_numbers(number_id):
    global stored_numbers
    previous_state = stored_numbers.copy()
    numbers = fetch_numbers_from_third_party(number_id)
    if numbers is not None:
        stored_numbers.extend(numbers)
        stored_numbers = list(set(stored_numbers))
        if len(stored_numbers) > WINDOW_SIZE:
            stored_numbers = stored_numbers[-WINDOW_SIZE:]
    current_state = stored_numbers.copy()
    return previous_state, current_state

@app.route('/numbers/<number_id>')
def handle_number_request(number_id):
    previous_state, current_state = update_and_get_states_for_numbers(number_id)
    average = calculate_average_of_numbers(current_state[-WINDOW_SIZE:])
    response = {
        "windowPrevState": previous_state,
        "windowCurrState": current_state,
        "numbers": current_state[-len(previous_state):],
        "avg": average
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
