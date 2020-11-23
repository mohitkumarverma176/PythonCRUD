import db_connection as dbConn;


class Update:
    def func_UpdateData(self):
        # Get the SQL connection
        connection = dbConn.getConnection()
        choice = int(input("What do you want to update 1: for name, 2: for Age"))
        cursor = connection.cursor()

        try:
            if choice == 1:
                name = input("Input the old name of the employee")
                sql = "Select * From Employee Where name = %s"

                cursor.execute(sql, [name])
                item = cursor.fetchone()
                print("Old record is ", item)
                name1 = str(input("Enter the new name of the employee"))
                sql1 = "Update Employee set name = %s where name = %s"
                cursor.execute(sql1, [name1,name])
                connection.commit()
                print("Data Updated Successfully")
            elif choice == 2:
                name = input("Enter the name  of the employee to update the age")
                sql = "Select * From Employee Where name = %s"
                cursor.execute(sql, [name])
                item = cursor.fetchone()
                print("Old record is ", item)
                age = int(input("Enter the new age of the Employee"))
                sql1 = "Update Employee set age = %s where name = %s"
                cursor.execute(sql1, [age, name])
                connection.commit()
                print("Data Updated Successfully")
            else:
                print("You have enterd the wrong choice please check")

        except:
            print('Something wrong, please check')

        finally:
            # Close the connection
            connection.close()