from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predecir', methods=['POST'])
def predecir():
    try:
        edad = int(request.form['edad'])
        fiebre = float(request.form['fiebre'])
        dolor = int(request.form['dolor'])

        if fiebre < 37:
            estado = "NO ENFERMO"
        elif 37 <= fiebre < 38 and dolor == 0:
            estado = "ENFERMEDAD LEVE"
        elif 38 <= fiebre < 39:
            estado = "ENFERMEDAD AGUDA"
        else:
            estado = "ENFERMEDAD CRÓNICA"

        return render_template('index.html', resultado=f"Diagnóstico: {estado}")
    except:
        return "Error en los datos ingresados."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
