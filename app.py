'''
Help Desk - Flask app.
'''

from flask import Flask, render_template, request, jsonify
from helpdesk import Helpdesk

app = Flask(__name__)
hd = Helpdesk()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tickets', methods=['GET'])
def get_tickets():
    return jsonify({'tickets': hd.get_tickets(), 'total': hd.get_total()})


@app.route('/tickets', methods=['POST'])
def add_ticket():
    data = request.get_json()
    client = data.get('client')
    description = data.get('description')
    priority = int(data.get('priority'))

    if not client or not description or priority not in [1, 2, 3, 4]:
        return jsonify({'error': 'Invalid data'}), 400

    node = hd.add_ticket(client, description, priority)
    return jsonify(node.to_dict())


@app.route('/tickets/next', methods=['DELETE'])
def attend_next():
    node = hd.attend_next()
    if node is None:
        return jsonify({'error': 'Queue is empty'}), 400
    return jsonify(node.to_dict())


@app.route('/tickets/<ticket_id>', methods=['GET'])
def search_ticket(ticket_id):
    node = hd.search_ticket(ticket_id)
    if node is None:
        return jsonify({'error': 'Ticket not found'}), 404
    return jsonify(node.to_dict())


@app.route('/tickets/<ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    data = request.get_json()
    new_priority = int(data.get('priority'))

    if new_priority not in [1, 2, 3, 4]:
        return jsonify({'error': 'Invalid priority'}), 400

    node = hd.update_priority(ticket_id, new_priority)
    if node is None:
        return jsonify({'error': 'Ticket not found'}), 404
    return jsonify(node.to_dict())


@app.route('/history', methods=['GET'])
def get_history():
    return jsonify({'history': hd.get_history()})


if __name__ == '__main__':
    app.run(debug=True)