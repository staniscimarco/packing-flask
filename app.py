from flask import Flask, jsonify, render_template, send_from_directory

app = Flask(__name__)

# Stato iniziale delle workstation
workstations = {i: "green" for i in range(1, 81)}
previous_states = workstations.copy()  # Per tenere traccia degli stati precedenti

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/workstations', methods=['GET'])
def get_workstations():
    return jsonify(workstations)

@app.route('/workstation/<int:id>', methods=['GET'])
def view_workstation(id):
    if id in workstations:
        return render_template('workstation.html', id=id, status=workstations[id], logo_url='/static/images/images.png')
    return "Workstation not found", 404

@app.route('/workstation_simple/<int:id>', methods=['GET'])
def view_workstation_simple(id):
    if id in workstations:
        return render_template('workstation_simple.html', id=id, status=workstations[id], logo_url='/static/images/images.png')
    return "Workstation not found", 404

@app.route('/workstation/<int:id>/anomaly', methods=['POST'])
def signal_anomaly(id):
    if id in workstations:
        workstations[id] = "red"
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 404

@app.route('/workstation/<int:id>/reset', methods=['POST'])
def reset_anomaly(id):
    if id in workstations:
        workstations[id] = "green"
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 404

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/check_alarm', methods=['GET'])
def check_alarm():
    global previous_states
    alarm_needed = any(workstations[id] == "red" and previous_states[id] != "red" for id in workstations)
    previous_states = workstations.copy()
    return jsonify({"alarm": alarm_needed})

if __name__ == '__main__':
    app.run(debug=True)



