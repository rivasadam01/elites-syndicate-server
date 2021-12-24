from elites import app


@app.route('/api/test', methods=['GET'])
def test_route():
    return 'Hello World!'
