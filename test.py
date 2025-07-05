@app.route('/hold-job', methods=['POST'])
def hold_job_api():
    job_name = request.json.get("job_name")
    if not job_name:
        return jsonify({"error": "Missing job_name"}), 400
    hold_job(job_name)
    return jsonify({"message": f"Job '{job_name}' held successfully"})

@app.route('/offhold-job', methods=['POST'])
def offhold_job_api():
    job_name = request.json.get("job_name")
    if not job_name:
        return jsonify({"error": "Missing job_name"}), 400
    off_hold_job(job_name)
    return jsonify({"message": f"Job '{job_name}' released from hold"})
