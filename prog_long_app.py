from flask import Flask
app = Flask(__name__)

in_memory_datastore = {
   "COBOL" : {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL" : {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL" : {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
}

@app.route('/',methods=["GET"])
def hello():
   return "Hello World"


@app.route('/programming_languages',methods=["GET"])
def list_programming_languages():
   return {"programming_languages":list(in_memory_datastore.values())}

'''
if __name__ == "__main__":
    app.run(debug=True)

'''

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)

