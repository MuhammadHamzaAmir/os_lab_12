# README file

## User Guide

- First, server.py file will be run.
- User will run client.py file and perform functions from there.
- We can initiate the program by requesting access to the file system.
- The file system will grant access by asking for the username.
- After the user has entered the name, a thread will be assigned to the user.
- User can now access the functions from the file system as the connection with the server is established.
- Multiple clients can use the system in read mode concurrently.
- Only one user is allowed to write in the file at the same time.
- Writing in the file is mutually exclusive.
- If 2 clients are reading a file and third client wants to write in the file then he/she will have to wait for both of the clients to close the file.