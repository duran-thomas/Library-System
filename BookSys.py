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
		print("Student")
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
		time.sleep(2)
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
		bk = open("Book.bat", "a")
		bk.write(title + " ")
		bk.write(author + " ")
		bk.write(str(accession) + " ")
		bk.write(isbn + " ")
		bk.write(available )
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
		time.sleep(2)
		Initialize()

def AddStudent():
	os.system('clear')
	print("  ===============================================")
	print("||             Create Student Record             ||")
	print("  ===============================================\n")
	name = input("Name: ")
	id = input("ID#: ")
	faculty = input("Faculty: ")
	contact = input("Contact#: ")
	loan = 0.00

	try:
		stud = open("Student.bat", "a")
		stud.write(name + " ")
		stud.write(id + " ")
		stud.write(faculty + " ")
		stud.write(contact + " ")
		stud.write(str(loan))
		stud.write("\n")
		stud.close()

	except Exception as e:
		raise e

	print("Student Record Added")
	choice = input("Add Another? (Y/N)")
	if choice == "Y" or choice == "y":
		AddStudent()
	elif choice == "N" or choice == "n":
		print("Returning To Previous Menu....")
		time.sleep(2)
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
		teach = open("Teacher.bat", "a")
		teach.write(name + " ")
		teach.write(id + " ")
		teach.write(faculty + " ")
		teach.write(contact + " ")
		teach.write("\n")
		teach.close()

	except Exception as e:
		raise e

	print("Teacher Record Added")
	choice = input("Add Another? (Y/N)")
	if choice == "Y" or choice == "y":
		AddStudent()
	elif choice == "N" or choice == "n":
		print("Returning To Previous Menu....")
		time.sleep(2)
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
		print("Borrow Book")
	elif choice == 2:
		print("Search")
	elif choice == 3:
		ViewAvailable()
	elif choice == 4:
		print("Return")
	elif choice == 5:
		print("Returning To Main Menu......")
		time.sleep(2)
		Menu()
	else:
		print("Invalid Choice")
		Initialize()

def ViewAvailable():
	os.system('clear')
	try:
		bk = open("Book.bat", "r")
		while True:
			book = bk.read()
			titl = book.strip('').split(" ")

			title, author, accession, isbn, available = titl
			print("Title: " + title)
			print("Author: " + author)
			print("Accession#: " + accession)
			print("ISBN#: " + isbn)
			print("Available: " + available)

			if ("" == book):	
			 	break

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
		print("Books On Loan")
	elif choice == 2:
		ViewAvailable()
	elif choice == 3:
		print("Check Outstanding Balance")
	elif choice == 4:
		print("Books Status")
	elif choice == 5:
		print("Returning To Main Menu......")
		time.sleep(2)
		Menu()
	else:
		print("Invalid Choice")
		Initialize()



Menu()