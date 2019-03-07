def delete(mydb, mycursor):
    id_choice = input("ID?")
    sql = "DELETE FROM plante WHERE ID = %s"
    val = (id_choice,)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record deleted.")
