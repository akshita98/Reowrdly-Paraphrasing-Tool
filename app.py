import os
from flask import Flask, jsonify, render_template, request
from api.rephrase import rephraseText

template_dir = os.path.join(os.path.dirname(__file__), 'template')
api_dir = os.path.join(os.path.dirname(__file__), 'api')
print(template_dir)
print(api_dir)

app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'rewordly'

@app.route('/', methods=['GET', 'POST'])
def index():
    rephrased_text = ""
    if request.method == 'POST':
        input_text = ""

        # Attempt to get JSON data
        try:
            data = request.get_json()
            input_text = data['text']
        except:
            pass
        
        # If JSON data not found, try form data
        if not input_text:
            input_text = request.form.get('text')

        if input_text:
            rephrased_text = rephraseText(input_text)
            print(rephrased_text)
            
    return render_template('index.html', rephrased_text=rephrased_text)

import os
from flask import Flask, jsonify, render_template, request
from api.rephrase import rephraseText

template_dir = os.path.join(os.path.dirname(__file__), 'template')
api_dir = os.path.join(os.path.dirname(__file__), 'api')
print(template_dir)
print(api_dir)

app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'rewordly'

@app.route('/', methods=['GET', 'POST'])
def index():
    rephrased_text = ""
    if request.method == 'POST':
        input_text = ""

        # Attempt to get JSON data
        try:
            data = request.get_json()
            input_text = data['text']
        except:
            pass
        
        # If JSON data not found, try form data
        if not input_text:
            input_text = request.form.get('text')

        if input_text:
            rephrased_text = rephraseText(input_text)
            print(rephrased_text)
            
    return render_template('index.html', rephrased_text=rephrased_text)


@app.route('/help')
def help_page():
    return render_template('help.html')

@app.route('/faq')
def faq_page():
    return render_template('FAQ.html')

if __name__ == "__main__":
    app.run(debug=True)
