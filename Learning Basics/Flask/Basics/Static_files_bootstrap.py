from flask import Flask,render_template
app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/')

@app.route('/')
def boot():
    return render_template('boot.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5555,debug = True)
