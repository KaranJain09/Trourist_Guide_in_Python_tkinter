import sqlite3


class Database:
    def add_user(self ,name, email, dob, gender, phone, password):
        # establish connection to sqlite database
        conn = sqlite3.connect("signup.db")
        cursor = conn.cursor()
        query = "INSERT INTO REGISTER(u_name,u_email,u_dob,u_gender,u_phone,u_password) values(?,?,?,?,?,?)"
        cursor.execute(query, (name, email, dob, gender, phone, password))
        # commit the changes to database
        conn.commit()
        print("data successfully stored")
        # verify that the data has been inserted into 'REGISTER' table
        conn.execute("select * from REGISTER")
        result = cursor.fetchall()
        print(result)

        # close connection to sqlite database
        cursor.close()
        conn.close()
