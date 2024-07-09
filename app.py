from flask import Flask, render_template, request, jsonify
from math import pi

app = Flask(__name__)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def coterminal(angle):
    angle %= (2*pi)
    if angle > 0 and angle < (pi/2):
        angle = angle
    elif angle > (pi/2) and angle < pi:
        angle = pi - angle
    elif angle >= pi and angle < ((3*pi)/2):
        angle = angle - pi
    elif angle >= ((3*pi)/2) and angle < (2*pi):
        angle = (2*pi) - angle
    return angle

def taylor_series(angle, iterations=17, tolerance=1e-10):
    if (angle % pi) == (pi/2) or (angle % pi) == ((3*pi)/2):
        return 0.0
    cos = 0
    for a in range(iterations):
        term = ((-1)**a) * (angle ** (2*a)) / factorial(2*a)
        cos += term
    if abs(cos) <= tolerance:
        return 0.0
    else:
        return cos

@app.route('/')
def index():
    return render_template('intro.html')

@app.route('/calculator')
def calculator():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    angle_type = request.form['angle_type']
    angle_input = request.form['angle_input'].replace('pi', str(pi))
    
    try:
        angle_input = eval(angle_input)
    except Exception as e:
        return jsonify({'error': str(e)})
    
    if angle_type == 'd':
        angle_radians = angle_input * (pi/180)
        coterminal_angle = coterminal(angle_radians)
        sign = 1
        adjusted_angle = angle_input % 360
        if adjusted_angle > 90 and adjusted_angle <= 270:
            sign = -1
        taylored = taylor_series(coterminal_angle)
        result = sign * taylored
    elif angle_type == 'r':
        coterminal_angle = coterminal(angle_input)
        sign = 1
        adjusted_angle = angle_input % (2*pi)
        if adjusted_angle > (pi/2) and adjusted_angle <= ((3*pi)/2):
            sign = -1
        taylored = taylor_series(coterminal_angle)
        result = sign * taylored
    
    return jsonify({'result': "%.15f" % result})

if __name__ == '__main__':
    app.run(debug=True)
