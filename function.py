import mysql.connector


def insert(mydb, mycursor):
    sql = "INSERT INTO plante (ID, nom, indication, partie_utilisee, prix) VALUES (%s, %s, %s, %s, %s)"
    val = (int(input("ID?")), input("nom?"), input("indication?"), input("partie utilisée?"), float(input("prix?")))
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except mysql.connector.errors.IntegrityError:
        print("ID ERROR!")


def delete(mydb, mycursor):
    id_choice = input("ID?")
    sql = "DELETE FROM plante WHERE ID = %s"
    val = (id_choice,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record deleted.")


def listing(mycursor):
    mycursor.execute("SELECT * FROM plante")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def search(mycursor):
    choice = input("nom de la plante")
    sql = "SELECT * FROM plante WHERE nom LIKE %s ORDER BY nom LIMIT 3"
    val = ("%" + choice + "%",)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
