import mysql.connector


def insert(mydb):
    mycursor = mydb.cursor()
    sql = "INSERT INTO plante (ID, nom, indication, partie_utilisee, prix) VALUES (%s, %s, %s, %s, %s)"
    val = (int(input("ID?")), input("nom?"), input("indication?"), input("partie utilisée?"), float(input("prix?")))
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except mysql.connector.errors.IntegrityError:
        print("ID ERROR!")
