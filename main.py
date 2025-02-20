# Marisol Morales & Andreas Moreno, 5/1/24, Lab 12 Iterator

import check_input
import tasklist


def main_menu():
  
    """Displays the main menu and returns the user's input."""
  
  
    print("1. Display current task")
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")
    choice = check_input.get_int_range("Enter choice: ", 1, 6)
    return choice

def get_date():
  
    """Prompts the user to enter the month, day, and year and returns the date in the format MM/DD/YYYY"""
  
    print('Enter due date:')
    month = check_input.get_int_range('Enter month: ', 1, 12)
    day = check_input.get_int_range('Enter day: ', 1, 31)
    year = check_input.get_int_range('Enter year: ', 2000, 2100)
    return f'{month:02d}/{day:02d}/{year}'

def get_time():
  
    """Prompts the user to enter the hour and minute and returns the time in the format HH:MM"""
  
    print('Enter time:')
    hour = check_input.get_int_range('Enter hour: ', 0, 23)
    minute = check_input.get_int_range('Enter minute: ', 0, 59)
    return f'{hour:02d}:{minute:02d}'

if __name__ == "__main__":
    task_list = tasklist.TaskList()

    while True:
        print("-Tasklist-")
        print(f"Tasks to complete: {len(task_list)}")
        choice = main_menu()

        if choice == 1:
            current_task = task_list.get_current_task()
            if current_task:
                print("Current task is:")
                print(current_task)
            else:
                print("All tasks are complete!")

        elif choice == 2:
            print("Tasks:")
            for i, task in enumerate(task_list, start=1):
                print(f"{i}. {task}")

        elif choice == 3:
          completed_task = task_list.mark_complete()
          if completed_task is not None:
            print("Marking current task as complete:  " + str(completed_task))
            current_task = task_list.get_current_task()
            if current_task is not None:
              print("New current task is:  " + str(current_task))
            else:
              print("All tasks are complete!")  
          else:
            print("All tasks are complete!")
              

        elif choice == 4:
            new_desc = input("Enter a task: ")
            new_date = get_date()
            new_time = get_time()
            task_list.add_task(new_desc, new_date, new_time)

        elif choice == 5:
            search_date = get_date()
            print(f"Tasks due on {search_date}:")
            found = False
            for task in task_list:
                if task.date == search_date:
                    print(task)
                    found = True
            if not found:
                print("No tasks found.")

        elif choice == 6:
            print("Saving list...")
            task_list.save_file()
            break
