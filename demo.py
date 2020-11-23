import db_connection as dbConn;




# Get the SQL connection
connection = dbConn.getConnection()
choice = int(input("What do you want to update 1: for name, 2: for Age"))
cursor = connection.cursor()
if choice == 1:
    name = input("Input the old name of the employee")
    sql = "Select * From Employee Where name = %s"

    cursor.execute(sql,[name])
    item = cursor.fetchone()
    print("Old record is ",item)
    name1 = str(input("Enter the new name of the employee"))
    sql1 = "Update Employee set name = %s where name = %s"
    cursor.execute(sql1,[name1,name])
    connection.commit()
    print("Data Updated Successfully")
elif choice == 2:
    name = input("Enter the name  of the employee to update the age")
    sql = "Select * From Employee Where name = %s"
    cursor.execute(sql,[name])
    item = cursor.fetchone()
    print("Old record is ", item)
    age = int(input("Enter the new age of the Employee"))
    sql1 = "Update Employee set age = %s where name = %s"
    cursor.execute(sql1,[age,name])
    connection.commit()
    print("Data Updated Successfully")
else:
    print("You have enterd the wrong choice please check")

'''id = input('Enter Employee Id = ')


# Fetch the data which needs to be updated
sql = "Select * From Employee Where name = %s"
cursor = connection.cursor()
cursor.execute(sql, [id])
item = cursor.fetchone()

print('Enter New Data To Update Employee Record ')

name = input('Enter New Name = ')
age = input('Enter New Age = ')
query = "Update Employee Set Name = %s, Age =%s where name = id"

# Execute the update query
cursor.execute(query, [name, age, id])
connection.commit()
print('Data Updated Successfully')

print('Something wrong, please check')


# Close the connection'''
connection.close()