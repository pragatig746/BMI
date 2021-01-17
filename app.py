from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = round(weight / ((height/100) ** 2), 2)
        if bmi < 18.5:
            x = "Underweight"
        elif bmi > 18.5 and bmi < 24.9:
            x = "Normal Weight"
        elif bmi > 25 and bmi < 29.9:
            x = "Overweight"
        elif bmi > 30:
            x = "Obese"

        return "your BMI is: " + str(bmi) +  " and you come in the category of " + x
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
