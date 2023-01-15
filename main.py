from flask import Flask, request

app = Flask(__name__)

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

        return str(result)
    return '''
        <form method="post">
        
            <input type="text" name="num1" placeholder="Enter a number">
            <br>
            <input type="text" name="num2" placeholder="Enter another number">
            <br>
            <select name="operator">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">*</option>
                <option value="divide">/</option>
            </select>
            <br><br>
            <input type="submit" value="Calculate">
        </form>
    '''

if __name__ == '__main__':
    app.run()