from flask import Flask, request
app = Flask(__name__)

@app.route('/testing') # you can probably even put testing.py here
def testing():
    vars = request.args
    return ','.join(map(str,vars))

if __name__ == "__main__":
    app.run()
