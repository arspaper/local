import base64
from flask import Flask, render_template, request

app = Flask(__name__)

allowed_stuff = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    d1 = filename.lower().split('.')[-1]
    return d1 in allowed_stuff


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', images=None, error='Нет файла для загрузки.')

        file = request.files['file']
        if file and allowed_file(file.filename):
              
            image_data = base64.b64encode(file.read()).decode('utf-8')
              
            image_type = file.filename.rsplit('.', 1)[1].lower()
            images = [f"data:image/{image_type};base64,{image_data}"]
            return render_template('index.html', images=images)

        return render_template('index.html', images=None, error='Недопустимый файл.') 
    return render_template('index.html', images=None)

if __name__ == '__main__':
    app.run(debug=True)
