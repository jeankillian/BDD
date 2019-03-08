import mysql.connector
import function


def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="phpmyadmin",
        passwd="grimmjow26",
        database="Herboristerie"
    )
    mycursor = mydb.cursor()
    while True:
        choice = input("choisissez 'i' pour insert, 'd' pour delete, 'l' pour list, 'q' pour quit ou 's' pour "
                       "search").lower()
        if choice == "i":
            function.insert(mydb, mycursor)

        if choice == "d":
            function.delete(mydb, mycursor)

        if choice == "l":
            function.listing(mycursor)

        if choice == "s":
            function.search(mycursor)

        if choice == "q":
            print("Bye Bye!")
            break


main()
