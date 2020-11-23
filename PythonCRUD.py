import db_connection
from read import Read
from create import Create
from update import Update
from delete import Delete
def main():
    while True:
        print('Available Options: C=Create, R=Read, U=Update, D=Delete , E = Exit')
        choice = input('Choose your option = ')

        if choice == 'C':
            createObj=Create()
            createObj.func_CreateData()
        elif choice == 'R':
            readObj =  Read()
            readObj.func_ReadData()
        elif choice == 'U':
            updateObj = Update()
            updateObj.func_UpdateData()
        elif choice == 'D':
            deleteObj = Delete()
            deleteObj.func_DeleteData()
        elif choice == 'E':
            print("Thanku")
            break
        elif choice != 'C' and choice != 'R' and choice != 'U' and choice != 'D':
            print('Wrong choice, You are going to exit')
            break



# Call the main function
main()