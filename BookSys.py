import os
import time

def Menu():
	os.system('clear')
	print("  ===============================================")
	print("||                    Main Menu                  ||")
	print("  ===============================================")
	print("||  Please Select An Option From The Menu Below  ||")
	print("||                                               ||")
	print("|| 1. Initialize System                          ||")
	print("|| 2. Teacher Account                            ||")
	print("|| 3. Student Account                            ||")
	print("|| 4. Librarian Account                          ||")
	print("|| 5. Exit                                       ||")
	print("||                                               ||")
	print(" ================================================")
	choice = int(input("Select Option: "))
	if choice == 1:
		Initialize()
	elif choice == 2:
		TeacherAccount()
	elif choice == 3:
		StudentAccount()
	elif choice == 4:
		LibrarianAccount()
	elif choice == 5:
		print("Closing System.....")
		os.system('exit')
	else:
		print("Invalid Choice")

def Initialize():
	os.system('clear')
	print("  ===============================================")
	print("||               Initialize System               ||")
	print("  ===============================================")
	print("||  Please Select An Option From The Menu Below  ||")
	print("||                                               ||")
	print("|| 1. Add New Book                               ||")
	print("|| 2. Create Teacher Account                     ||")
	print("|| 3. Create Student Account                     ||")
	print("|| 4. Back To Main Menu                          ||")
	print("||                                               ||")
	print(" ================================================")
	choice = int(input("Select Option: "))
	if choice == 1:
		AddBook()
	elif choice == 2:
		AddTeacher()
	elif choice == 3:
		AddStudent()
	elif choice == 4:
		print("Returning To Main Menu......")
		time.sleep(1)
		Menu()
	else:
		print("Invalid Choice")
		Initialize()

def AddBook():
	os.system('clear')
	print("  ===============================================")
	print("||                 Add New Book                  ||")
	print("  ===============================================\n")
	title = input("Title: ")
	author = input("Author: ")
	accession = int(input("Accession#: "))
	isbn = input("ISBN#: ")
	available = "Yes"
	try:

		bk = open("Book.bat", "a+")
		bk.write("%s %s %d %s %s\n" % (title, author, accession, isbn, available))
	except Exception as e:
		raise e
	finally:
		bk.close()

	print("Book Successfully Added")
	choice = input("Add Another? (Y/N)")
	if choice == "Y" or choice == "y":
		AddBook()
	elif choice == "N" or choice == "n":
		print("Returning To Previous Menu....")
		time.sleep(1)
		Initialize()

def AddStudent():
	os.system('clear')
	print("  ===============================================")
	print("||             Create Student Record             ||")
	print("  ===============================================\n")
	name = input("Name: ")
	id = int(input("ID#: "))
	faculty = input("Faculty: ")
	contact = input("Contact#: ")
	loan = 0.00

	try:
		stud = open("Student.bat", "a+")
		stud.write("%s %d %s %s %.2f\n" % (name, id, faculty, contact, loan))
	except Exception as e:
		raise e
	finally:
		stud.close()

	print("Student Record Added")
	choice = input("Add Another? (Y/N)")
	if choice == "Y" or choice == "y":
		AddStudent()
	elif choice == "N" or choice == "n":
		print("Returning To Previous Menu....")
		time.sleep(1)
		Initialize()

def AddTeacher():
	os.system('clear')
	print("  ===============================================")
	print("||             Create Teacher Record             ||")
	print("  ===============================================\n")
	name = input("Name: ")
	id = input("ID#: ")
	faculty = input("Faculty: ")
	contact = input("Contact#: ")

	try:
		teach = open("Teacher.bat", "a+")
		teach.write("%s %d %s %s\n" % (name, id, faculty, contact))
	except Exception as e:
		raise e
	finally:
		teach.close()

	print("Teacher Record Added")
	choice = input("Add Another? (Y/N)")
	if choice == "Y" or choice == "y":
		AddTeacher()
	elif choice == "N" or choice == "n":
		print("Returning To Previous Menu....")
		time.sleep(1)
		Initialize()

def TeacherAccount():
	os.system('clear')
	print("  ===============================================")
	print("||                Teacher Account                ||")
	print("  ===============================================")
	print("||  Please Select An Option From The Menu Below  ||")
	print("||                                               ||")
	print("|| 1. Borrow Book                                ||")
	print("|| 2. Search For Book                            ||")
	print("|| 3. View Books Available                       ||")
	print("|| 4. Return Book                                ||")
	print("|| 5. Exit To Main Menu                          ||")
	print("||                                               ||")
	print(" ================================================")
	choice = int(input("Select Option: "))
	if choice == 1:
		BorrowBook()
	elif choice == 2:
		print("Search")
	elif choice == 3:
		ViewAvailable()
	elif choice == 4:
		print("Return")
	elif choice == 5:
		print("Returning To Main Menu......")
		time.sleep(1)
		Menu()
	else:
		print("Invalid Choice")
		Initialize()

def ViewAvailable():
	os.system('clear')
	try:
		line_number = 0
		with open('Book.bat') as file:
			for line in file:
				line_number += 1
				print(line_number, line.rstrip())

	except Exception as e:
		raise e
	
def LibrarianAccount():
	os.system('clear')
	print("  ===============================================")
	print("||               Librarian Account               ||")
	print("  ===============================================")
	print("||  Please Select An Option From The Menu Below  ||")
	print("||                                               ||")
	print("|| 1. View Books On Loan                         ||")
	print("|| 2. View Books Available                       ||")
	print("|| 3. Check Outstanding Balance                  ||")
	print("|| 4. View All Books Status                      ||")
	print("|| 5. Exit To Main Menu                          ||")
	print("||                                               ||")
	print(" ================================================")
	choice = int(input("Select Option: "))
	if choice == 1:
		BooksOnLoan()
	elif choice == 2:
		ViewAvailable()
	elif choice == 3:
		CheckBalance()
		print("Books On Loan")
	elif choice == 2:
		ViewAvailable()
	elif choice == 3:
		print("Check Outstanding Balance")
	elif choice == 4:
		print("Books Status")
	elif choice == 5:
		print("Returning To Main Menu......")
		time.sleep(1)
		Menu()
	else:
		print("Invalid Choice")
		Initialize()

def BooksOnLoan():
	os.system('clear')
	try:
		bk = open("Book.bat", "r+")
		book = bk.readline()
		titl = book.strip('').split(" ")

		title, fauthor, lauthor, accession, isbn, available = titl
		if (available == "Yes"):
			print("Title: " + title)
			print("Author: " + fauthor, lauthor)
			print("Accession#: " + accession)
			print("ISBN#: " + isbn)
		else:
			print("No Books On Loan")
		
	except Exception as e:
		raise e
	finally:
		bk.close()

def CheckBalance():
	os.system('clear')
	print("  ===============================================")
	print("||           Check Outstanding Balance           ||")
	print("  ===============================================")
	print("\n")
	id=input("Enter Student ID: ")

	with open('Student.bat', 'r') as searchfile:
	    for line in searchfile:
	        if id in line:
	            info = line.strip(' ').split()
	            fname, lname, idnum, faculty, contactnum, bal = info
	            continue
	        else:
	        	print("Student Record Not Found")
	os.system('clear')
	print("  ===============================================")
	print("||           Check Outstanding Balance           ||")
	print("  ===============================================")
	print("\n")
	print("ID#: " + idnum)
	print("Name: " + fname, lname)
	print("Loan Balance: " + bal)
	print("\n")

	choice = input("Check Another? (Y/N)")
	if choice == "Y" or choice == "y":
		CheckBalance()
	elif choice == "N" or choice == "n":
		print("Returning To Previous Menu....")
		time.sleep(1)
		LibrarianAccount()

def BorrowBook():
	os.system('clear')
	print("  ===============================================")
	print("||                  Borrow Book                  ||")
	print("  ===============================================")
	print("\n")
	isbn=input("Enter ISBN#: ")

	with open('Book.bat', 'r') as searchfile:
	    for line in searchfile:
	        if isbn in line:
	            info = line.strip(' ').split()
	            title, fauthor, lauthor, isbn, accession, available = info
	            continue
	        else:
	        	print("Book Not Found")
	os.system('clear')
	print("  ===============================================")
	print("||                  Borrow Book                  ||")
	print("  ===============================================")
	print("\n")
	print("ISBN#: " + isbn)
	print("Title: " + title)
	print("Author: " + fauthor, lauthor)
	print("Available: " + available)
	print("\n")

	choice = input("Would You Like To Borrow This Book? (Y/N)")
	if choice == "Y" or choice == "y":
		available = "No"
	elif choice == "N" or choice == "n":
		print("Returning To Previous Menu....")
		time.sleep(1)
		LibrarianAccount()

def StudentAccount():
	os.system('clear')
	print("  ===============================================")
	print("||                Student Account                ||")
	print("  ===============================================")
	print("||  Please Select An Option From The Menu Below  ||")
	print("||                                               ||")
	print("|| 1. Borrow Book                                ||")
	print("|| 2. Check Outstanding Balance                  ||")
	print("|| 3. Make Payments                              ||")
	print("|| 4. Search For A Book                          ||")
	print("|| 5. View Books Available                       ||")
	print("|| 6. Return Books                               ||")
	print("|| 7. Exit To Main Menu                          ||")
	print("||                                               ||")
	print(" ================================================")
	choice = int(input("Select Option: "))
	if choice == 1:
		BorrowBook()
	elif choice == 2:
		CheckBalance()
	elif choice == 3:
		print("Make Payments")
	elif choice == 4:
		SearchBook()
	elif choice == 5:
		ViewAvailable()
	elif choice == 6:
		print("Return Book")
	elif choice == 7:
		print("Returning To Main Menu......")
		time.sleep(1)
		Menu()
	else:
		print("Invalid Choice")
		Initialize()

def SearchBook():
	os.system('clear')
	print("  ===============================================")
	print("||                  Search Book                  ||")
	print("  ===============================================")
	print("\n")
	isbn=input("Enter ISBN#: ")

	with open('Book.bat', 'r') as searchfile:
	    for line in searchfile:
	        if isbn in line:
	            info = line.strip(' ').split()
	            title, fauthor, lauthor, isbn, accession, available = info
	            continue
	        else:
	        	print("Book Not Found")

	os.system('clear')
	print("  ===============================================")
	print("||                  Search Book                  ||")
	print("  ===============================================")
	print("\n")
	print("ISBN#: " + isbn)
	print("Title: " + title)
	print("Author: " + fauthor, lauthor)
	print("Available: " + available)
	print("\n")

	choice = input("Would You Like To Search For Another? (Y/N)")
	if choice == "Y" or choice == "y":
		SearchBook()
	elif choice == "N" or choice == "n":
		print("Returning To Previous Menu....")
		time.sleep(1)
		StudentAccount()


Menu()