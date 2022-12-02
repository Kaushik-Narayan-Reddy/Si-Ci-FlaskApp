from flask import Flask, render_template, request

def compound_interest(P,t,r,n):
    if n!=0:
        A = P*pow(1+((r/100)/n),(n*t))
    if n==0:
        A = 0
        print("Given n value is not applicable")
    return A


def simple_interest(P,t,r):
    B = P+((P*r*t)/100)
    # r = r/100
    # A = P*(1+(r*t))
    # print(B)
    return B

app = Flask(__name__)
# app.config.from_object(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def result():
    #taking the user input
    var_1 = request.form.get("var_1", type=float, default=0)
    var_2 = request.form.get("var_2", type=float, default=0)
    var_3 = request.form.get("var_3", type=float, default=0)
    var_4 = request.form.get("var_4", type=float, default=0)
    operation = request.form.get("operation")
    if(operation == 'Simple Interest'):
        result = simple_interest(var_1,var_2,var_3)
    elif(operation == 'Compound Interest'):
        if var_4!=0:
            result = compound_interest(var_1,var_2,var_3,var_4)
        else:
            var_4=1
            result = compound_interest(var_1,var_2,var_3,var_4)
    entry = result
    return render_template('index.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
