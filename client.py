from socket import *
import time

def mainMenu():
    delay_t = 0.5
    serverIP = input("Enter the IP address: ")
    username = input("Enter the user name: ")
    clientSocket = socket(AF_INET, SOCK_STREAM)
    #clientSocket.settimeout(120)
    clientSocket.connect((serverIP, 95))
    clientSocket.send(username.encode('utf-8'))
    main_file = ""
    
    while (True):
        print("**File Management System**")

        print("""
            1.Create file
            2.Delete file
            3.Open file
            4.Close file
            5.Read file
            6.Write in the file
            7.Append in the end of text file
            8.Read from a specific point
            9.Write at the specific point
            10.Truncate
            11.Move within a file
            12.Show memory map
            13.Exit System 
            """)

        choice = input("What would you like to do: ")

        if choice == "1":
            fname = input(
                "Enter the name for the text file: ")
            send_data = "Create#"+fname
            main_file = fname
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "2":
            fname = input(
                "Enter the name for the text file you want to delete: ")
            send_data = "Delete#"+fname
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "3":
            fname = input(
                "Enter the name of the file you want to open: ")
            mode = input("Enter the file mode (r,w,a)")
            main_file = fname
            send_data = "Open#"+fname+"#"+mode
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "4":
            fname = input(
                "Enter the name of the file you want to close: ")
            send_data = "Close#"+fname
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "5":
            send_data = "Read_From_File#"+main_file
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "6":
            text = input("Enter data: ")
            send_data = "write_to_file#"+main_file+"#"+text
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "7":
            text = input("Enter data: ")
            send_data = "appendFile#"+main_file+"#"+text
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "8":
            start = input("Enter the starting point: ")
            size = input("Enter the string you want to read till: ")
            send_data = "read_from_file_at#"+main_file+"#"+start+"#"+size
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "9":
            write_at = input("Enter the point where you want to write: ")
            text = input("Enter Data: ")
            cond = input("Do you want to overwrite: IF YES THEN WRITE 1 else 0")
            send_data = "Write_to_File_over#"+main_file+"#"+write_at+"#"+text+"#"+cond
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "10":
            maxsize = input("Enter the size of the file, you want: ")
            send_data = "truncate#"+main_file+"#"+maxsize
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "11":
            start = input("Enter starting index: ")
            size = input("Enter the size of string: ")
            target = input("Enter where you want to put the string: ")
            send_data = "Move_within_file#"+main_file+"#"+start+"#"+size+"#"+target
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(204800).decode('utf-8')
            print(output)
        elif choice == "12":
            send_data = "show_memory_map"
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t)
            output = clientSocket.recv(2048000).decode('utf-8')
            print(output)
        elif choice == "13":
            send_data = "MHA_ARA"
            clientSocket.send(send_data.encode('utf-8'))
            time.sleep(delay_t+1)
            clientSocket.send(send_data.encode('utf-8'))
            break
        elif choice != "":
            print("\n Not Valid Choice Try again")
    clientSocket.close()

mainMenu()
