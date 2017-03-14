-from flask import Flask
cmd=sys.argv
app = Flask(__name__)

@app.route(cmd)
def hello(): 
    return "Hello from Dockerized Flask App!!"

if __name__ == "__main__":
            app.run(debug=True,host='0.0.0.0')
