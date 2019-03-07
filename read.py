import mysql.connector
import insert
import delete


def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="phpmyadmin",
        passwd="grimmjow26",
        database="Herboristerie"
    )
    while True:
        choice = input("choisissez 'i' pour insert, 'd' pour delete, 'l' pour list ou 'q' pour quit").lower()
        if choice == "i":
            insert.insert(mydb)

        if choice == "d":
            delete.delete(mydb)

        if choice == "l":
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM plante")
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)

        if choice == "q":
            print("Bye Bye!")
            break


main()
