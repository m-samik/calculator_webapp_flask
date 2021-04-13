from flask import Flask, render_template, request
app = Flask("mytest")


@app.route('/home')
def home():
    return "<b> My Home Page </b>"


@app.route('/')
def form():
    formrender = render_template("calci.html")
    return formrender

# Get Request Method

# @app.route('/req')
# def req():
#     if request.method == "GET":
#         data = request.args.get("name")
#         return data


@app.route('/answer', methods=['POST'])
def req():
    if request.method == "POST":
        data = request.form.get("name")
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        operend = request.form.get("operation")
        if operend == "add":
            number = int(num1) + int(num2)
        elif operend == "sub":
            number = int(num1) - int(num2)
        elif operend == "mul":
            number = int(num1) * int(num2)
        elif operend == "div":
            number = int(num1) / int(num2)
        formrender = render_template(
            "calci.html", value=str(number), name=data)
        print(data)
        return formrender


@app.route('/req/<name>')
def dynrou(name):
    return name.lower()


@app.route('/test')
def test():
    return render_template("test.html")


app.run(host="0.0.0.0", port=80, debug=True)
