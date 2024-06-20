from flask import Flask, request, jsonify
import util
import util_pune
import util_delhi

app = Flask(__name__)

################# Banglore #############################

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        response = jsonify({
            'locations': util.get_location_names()
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        error_message = f'Error in /get_location_names: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 500

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = util.get_estimated_price(location, sqft, bhk, bath)

        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except KeyError as e:
        error_message = f'Missing key in form data: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 400

    except ValueError as e:
        error_message = f'Invalid value in form data: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 400

    except Exception as e:
        error_message = f'Internal server error: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 500

    ################# PUNE #############################

@app.route('/get_location_names_pune', methods=['GET'])
def get_location_names_pune():
    try:
        response = jsonify({
            'locations': util_pune.get_location_names_pune()
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        error_message = f'Error in /get_location_names_pune: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 500

@app.route('/predict_home_price_pune', methods=['POST'])
def predict_home_price_pune():
    try:
        sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = util_pune.get_estimated_price_pune(location, sqft, bhk, bath)

        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except KeyError as e:
        error_message = f'Missing key in form data: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 400

    except ValueError as e:
        error_message = f'Invalid value in form data: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 400

    except Exception as e:
        error_message = f'Internal server error: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 500





################# DELHI #############################

@app.route('/get_location_names_delhi', methods=['GET'])
def get_location_names_delhi():
    try:
        response = jsonify({
            'locations': util_delhi.get_location_names_delhi()
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        error_message = f'Error in /get_location_names_delhi: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 500

@app.route('/predict_home_price_delhi', methods=['POST'])
def predict_home_price_delhi():
    try:
        sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = util_delhi.get_estimated_price_delhi(location, sqft, bhk, bath)

        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except KeyError as e:
        error_message = f'Missing key in form data: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 400

    except ValueError as e:
        error_message = f'Invalid value in form data: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 400

    except Exception as e:
        error_message = f'Internal server error: {str(e)}'
        print(error_message)
        return jsonify({'error': error_message}), 500




if __name__ == "__main__":
    print("Starting price prediction server...")
    try:
        util.load_saved_artifacts()
        util_pune.load_saved_artifacts_pune()
        util_delhi.load_saved_artifacts_delhi()
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting server: {str(e)}")






    ########### PUNE ############################
    # try:
    #     util_pune.load_saved_artifacts_pune()
    #     app.run(debug=True)
    # except Exception as e:
    #     print(f"Error starting server: {str(e)}")
