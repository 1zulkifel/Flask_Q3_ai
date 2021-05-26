from flask import Flask, jsonify
app=Flask(__name__)
@app.route("/")
def index():
    students= [
        {'id':1,'name':'Ali','course':'A.I'},
        {'id':2,'name':'khan','Age':'12'},
        {'id':3,'name':'waleed'},
        {'id':4,'name':'Zulkifel','Father Name':'khan'},
        {'id':5,'name':'Ahmad','city':'chitral'}

    ]
    return jsonify({"PIAIC Student":students})
app.run(debug=True)