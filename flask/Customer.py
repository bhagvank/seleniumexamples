from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template("home.html");  
 
@app.route("/add")  
def add():  
    return render_template("addCustomer.html")  
 
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            address = request.form["address"]  
            with sqlite3.connect("customers.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Customers (name, email, address) values (?,?,?)",(name,email,address))  
                con.commit()  
                msg = "Customer successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the Customer to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close()  
 
@app.route("/view")  
def view():  
    con = sqlite3.connect("customers.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Customers")  
    rows = cur.fetchall()  
    return render_template("viewCustomer.html",rows = rows)

if __name__ =='__main__':
    app.run(debug = True) 
