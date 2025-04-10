
from flask import Flask, request , jsonify

app =  Flask(__name__)

# @app.route(rule='/apisum',methods=["POST"])
# def calculate_sum():
#     data = request.get_json()
#     a_val = float(dict(data)["a"])
#     b_val = float(dict(data)["b"])
#     return jsonify(a_val + b_val)

@app.route(rule='/apimulti' , methods=["POST"])
def multiplication():

    '''request.get_json(): This function retrieves the JSON data sent in the POST
      request body and converts it into a Python dictionary.'''
    data = request.get_json()

    '''dict(data): Converts the JSON data into a Python dictionary.
    data["x"] and data["y"]: These lines extract the values of x and y from the JSON data.
    float(...): Converts the extracted values to floating-point numbers.'''
    x_val = float(dict(data)["x"])
    y_val = float(dict(data)["y"])

    '''a_val + b_val: This adds the two values together.
    jsonify(...): Converts the result into a JSON format and returns it as the API response.'''
    return jsonify(x_val * y_val)

if __name__ == "__main__":
    app.run(debug=True)
