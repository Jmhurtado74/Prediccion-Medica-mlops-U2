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

        # Lógica de diagnóstico considerando edad, fiebre y dolor
        if fiebre < 37 and edad < 12:
            estado = "NIÑO SANO"
        elif fiebre < 37:
            estado = "NO ENFERMO"
        elif 37 <= fiebre < 38 and dolor == 0:
            estado = "ENFERMEDAD LEVE"
        elif 38 <= fiebre < 39:
            if edad > 60:
                estado = "ENFERMEDAD AGUDA (RIESGO ALTO)"
            else:
                estado = "ENFERMEDAD AGUDA"
        else:
            estado = "ENFERMEDAD CRÓNICA"

        return render_template('index.html', resultado=f"Diagnóstico: {estado}")
    except Exception as e:
        return f"Error en los datos ingresados: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)