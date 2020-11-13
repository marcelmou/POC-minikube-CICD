from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '5465142684121x6dwdcqws168'


#Die Klasse calcForm verwendet die flask_wtf-Bibliothek um das Webformular zu generieren
class calcForm(FlaskForm):
    number1 = FloatField('Zahl 1', validators=[DataRequired()])
    number2 = FloatField('Zahl 2', validators=[DataRequired()])
    submit = SubmitField('Berechnen')

#Die Funktion calculate(var1,var2) führt eine Rechenoperation mit den übergebenen Parameter aus.
#Der RETURN der Funktion ist das Ergebnis der Rechenoperation.
def calculate(var1,var2):
    result = var1+var2
    return result;

#app.route definiert die Location und die verwendeten HTTP-Methods
@app.route('/', methods=['GET', 'POST'])

#Die View-Funktion index() baut das angezeigte HTML-Dokument inkl. Formular.
#Falls HTTP-Methoden ausgeführt werden, werden weitere Funktionen aufgerufen
def index():
    #Formular aufbauen mit der Klasse calcForm
    form = calcForm(request.form)

    #Handlungsstrang wenn ein HTTP-POST ausgeführt wird
    if request.method == 'POST':
        value = calculate(form.number1.data,form.number2.data)
        print(value)

    #Handlungsstrang wenn ein HTTP-GET ausgeführt wird
    if request.method == 'GET' and request.args.get('number1') is not None:
        value = calculate(float(request.args.get('number1')),float(request.args.get('number2')))
        print(value)

    #Return: die HTML Datei, die auf Basis des Templates webForm.html geparst wird
    return render_template('webForm.html', title='Calculate', form=form)

#Main-Funktion
if __name__ == "__main__":
    app.run()
