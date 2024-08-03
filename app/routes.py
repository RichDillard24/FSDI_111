from flask import Flask
    #oop
app = Flask(__name__) # create an instance of Flask class (an object)

@app.get("/")       # flask decorato that "wraps" our view function
def index():        #view function
    me ={           #python3 dictionary (key-value pairs)
        "first_name": "Richard",
         "last_name": "Dillard",
         "hobbies": "Music",
         "is_online": True
         }
    return me           # returning a dict from a view function auto-coverts to JNOS!