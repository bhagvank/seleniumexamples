import sqlite3  
  
con = sqlite3.connect("customers.db")  
print("Customers Database opening")  
  
con.execute("create table Customers (customerid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")  
  
print("Customer Table created successfully")  
  
con.close()  
