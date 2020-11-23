import db_connection as dbConn;


class Delete:
    def func_DeleteData(self):
        # Get the SQL connection
        connection = dbConn.getConnection()

        id = input('Enter Employee name = ')

        try:
            # Get record which needs to be deleted
            sql = "Select * From Employee Where name = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', item)

            confirm = input('Are you sure to delete this record (Y/N)?')

            # Delete after confirmation
            if confirm == 'Y':
                deleteQuery = "Delete From Employee Where name = %s"
                cursor.execute(deleteQuery, [id])
                connection.commit()
                print('Data deleted successfully!')
            else:
                print('Wrong Entry')
        except:
            print('Something wrong, please check')
        finally:
            connection.close()