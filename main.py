
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
  return 'hello,World!'

if __name=='__main__' :
 app.run()
