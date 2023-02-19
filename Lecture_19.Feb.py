from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world0():
    return "<h1>Hello, World!</h1>"  

@app.route("/Hello, World1")
def hello_world1():
    return "<h1>Hello, World1!</h1>" 

@app.route("/Hello, World2")
def hello_world2():
    return "<h1>Hello, World2!</h1>" 

@app.route("/test")
def test():
    a = 8 + 9
    return 'This is my Function to run {}'.format(a)

@app.route("/test2")
def test2():
   data =  request.args.get('x')
   return 'this is data input from my url {}'.format(data)

@app.route('/addition')
def addition():
    x =  int(request.args.get('x'))
    y =  int(request.args.get('y'))
    result = x + y
    return 'the sum of {} and {} is {}'.format(x,y,result)

@app.route('/sub')
def sub():
    x =  int(request.args.get('x'))
    y =  int(request.args.get('y'))
    result = x - y
    return 'the sum of {} and {} is {}'.format(x,y,result)

@app.route('/multi')
def multi():
    x =  int(request.args.get('x'))
    y =  int(request.args.get('y'))
    result = x * y
    return 'the sum of {} and {} is {}'.format(x,y,result)

@app.route('/division')
def division():
    x =  int(request.args.get('x'))
    y =  int(request.args.get('y'))
    result = x / y
    return 'the sum of {} and {} is {}'.format(x,y,result)

if __name__=="__main__":
    app.run(host="0.0.0.0")
