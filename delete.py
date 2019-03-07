def delete(mydb):
    mycursor = mydb.cursor()
    id_choice = input("ID?")
    sql = "DELETE FROM plante WHERE ID = '" + id_choice + "'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record deleted.")
