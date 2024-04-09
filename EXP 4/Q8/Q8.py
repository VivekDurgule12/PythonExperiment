def search():
    file = open("student.dat","rb")
    try:
        while True:
            record = pickle.load(file)
            if record[0] == 1005:
                print(record)
    except EOFError:
        pass
    file.close()

# import pickle

# def create_student_data():
#     # Sample student records
#     students = [
#         (1001, "Alice", 20, "A"),
#         (1002, "Bob", 21, "B"),
#         (1003, "Charlie", 19, "C"),
#         (1004, "David", 22, "A"),
#         (1005, "Eve", 20, "B"),
#         # Add more records as needed
#     ]
    
#     # Open the file in binary write mode
#     with open("student.dat", "wb") as file:
#         # Serialize and write each student record
#         for student in students:
#             pickle.dump(student, file)

# # Call the function to create the file
# create_student_data()
