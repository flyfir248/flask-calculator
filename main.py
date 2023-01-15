from flask import Flask, request, render_template
app = Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        # Get the values and operator from the form
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operator = request.form['operator']

        # Perform the calculation
        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            result = num1 / num2
        else:
            return 'Invalid operator'
        return render_template('template.html', result=result)

    else:
        return render_template('template.html')

if __name__ == '__main__':
    app.run()