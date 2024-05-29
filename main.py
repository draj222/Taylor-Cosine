from math import pi

#Create function for factorial
#It is required in the Taylor Series
'''
The general formula for factorials is:
n! = n(n-1)(n-2)...*3*2*1
'''
def factorial(n):
    if n == 0:
        return 1 
    #The factorial of 0 is 1, so if f=0, we want to return 1
    else:
        return n * factorial(n-1) 
    #using the general formula, and keep calling until n = 0
    

def coterminal(angle):
    # Reduce angle to be within 0 to 2*pi
    angle %= (2*pi)

    if angle > 0 and angle < (pi/2):  # Q1
        angle = angle
    elif angle > (pi/2) and angle < pi:  # Q2
        angle = pi - angle
    elif angle >= pi and angle < ((3*pi)/2):  # Q3
        angle = angle - pi
    elif angle >= ((3*pi)/2) and angle < (2*pi):  # Q4
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


while True:
    angle_type = input("Radians (r) or Degrees (d): ")
    angle_input = input("Enter the angle, or 'pi' for π: ")
    angle_input = angle_input.replace('pi', str(pi)) 
    #replace pi with the actual value of pi
    #This line will take a string, and try to calculate the problem 
    '''
    For example, if angle_input is 5*pi,
    it will evaluate it as a math problem.
    Then, it will return it as a String
    '''

    try:
        angle_input = eval(angle_input)
   
    
    
    except Exception as message:
        print("Invalid: ", message) 
        #This will print out what is wrong to the user
        continue 
        #This will allow the program to continue to run

    '''
    This is to handle errors.
    Python's Exception block catches errors
    '''


    if angle_type.lower() == 'd':  
        angle_radians = angle_input * (pi/180) 
        # Convert degrees to radians 
        coterminal_angle = coterminal(angle_radians)
        
        sign = 1
        adjusted_angle = angle_input % 360
        if adjusted_angle > 90 and adjusted_angle <= 270:
            sign = -1
        
        taylored = taylor_series(coterminal_angle)
        print("%.15f" % (sign*taylored))

    elif angle_type.lower() == 'r':
        coterminal_angle = coterminal(angle_input) 

        sign = 1
        adjusted_angle = angle_input % (2*pi)
        if adjusted_angle > (pi/2) and adjusted_angle <= ((3*pi)/2):
            sign = -1

        taylored = taylor_series(coterminal_angle)
        if (sign*taylored) == -0.000000000000000:
            sign = 1
        print("%.15f" % (sign*taylored))