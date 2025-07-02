# Task 1. Read and Display File Contents
#Task: Read a .txt file and display each line with line numbers.
# Handle file not found error.


def read_and_display():

   try:
        file=open("meena.txt",'r')
        lines=file.readlines()

        for i in range(len(lines)):
           print(f"{i + 1}: {lines[i].strip()}")

        file.close()

   except FileNotFoundError:
        print("file not exist")

read_and_display()

# Task 2 Search in File
# Search for a specific keyword in a file and print how many times it appears.
# Bonus: Show the lines where it occurs.

def search_in_file(file_path, keyword):
    try:
        with open(file_path, 'r') :
            content = file.read().lower()
            keyword_lower = keyword.lower()
            count = content.count(keyword_lower)
            return count
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage:
file_name = "example.txt"
search_keyword = "file"

with open(file_name, 'w') as f:
    f.write("This is the test file .\n")

occurrences = search_in_file(file_name, search_keyword)

if occurrences > 0:
    print(f"The keyword '{search_keyword}' appears {occurrences} times in '{file_name}'.")
else:
    print(f"The keyword '{search_keyword}' was not found in '{file_name}' or an error occurred.")

search_in_file(file_name, search_keyword)

# Task 3. Log Writer App
#Task: Create a program that logs user activities (like login, logout) to a file.
#Use append mode to add logs with timestamps.
#Ex: [2025–06–30 10:00:00] User logged in

def log_activity(action):
    from datetime import datetime
    timestamp = datetime.now()
    with open('user_log.txt','a') as f:
        f.write(f"[{timestamp}] User {action}\n")

log_activity('logged in')
log_activity('logged out')


#Task 4. User Feedback Collector
#Task: Accept user input and store it in a file.
#Every time a new feedback is entered, it should be appended.

feedback = input('Enter feedback: ')

file = open('feedback.txt','a')
file.write(feedback+'\n')
file.close()

print('feedback saved')

# Task 3. To-Do List Manager
# Create a to-do list app that:
#Adds tasks to a file (write or append)
#Reads all tasks from the file
#Deletes all tasks (clear file content using 'w' mode)

def add_task(task, filename="to-do.txt"):
    try:
        with open(filename, "a") as file:
            file.write(task + "\n")
        print(f"Task '{task}' added.")
    except Exception as e:
        print(f"Error adding task: {e}")

def view_tasks(filename="to-do.txt"):
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()
        if tasks:
            print("Your To-Do List:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")
        else:
            print("Your to-do list is empty.")
    except FileNotFoundError:
        print("No tasks found yet.  Try adding some!")
    except Exception as e:
        print(f"Error viewing tasks: {e}")

def delete_all_tasks(filename="to-do.txt"):

    try:
        with open(filename, "w") as file:
            pass

        print("All tasks deleted.")
    except Exception as e:
        print(f"Error deleting tasks: {e}")

# Example Usage:
if __name__ == "__main__":
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete All Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_all_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
