def create_task(task_id, task_name, task_matrix):
    task_row = {
        "id": task_id,
        "task": task_name
    }
    # Append the new task to the task matrix
    task_matrix.append(task_row)
    return task_matrix
# This function displays the current tasks in a formatted manner
def display_tasks(task_matrix):
    if not task_matrix:
        print("\n--- Your To-Do List is currently empty! ---")
        return
# Display the tasks in a tabular format
    print("\n================ SYSTEM DATABASE ================")
    print(f"{'INDEX':<10}{'USER TASK ID':<15}{'TASK NAME'}")
    print("-------------------------------------------------")
  # Loop through the task matrix and display each task with its index  
    for index, task_row in enumerate(task_matrix, start=1):
        print(f"{index:<10}{task_row['id']:<15}{task_row['task']}")
    print("=================================================")
# The main function that runs the task management system
def main():
    my_tasks = []
    
    print("=== DECODELABS JUNIOR BACKEND ENGINE ON ===")
    while True:
        print("\n--- MENU ---")
        print("1. Add Task (Data Entry)")
        print("2. View Tasks (Display)")
        print("3. Exit (Process Terminate)")
        
        choice = input("Select an option (1-3): ").strip()
        # Handle the user's choice and perform the corresponding action
        if choice == "1":
            try:
                num_tasks = int(input("Enter how many tasks you want to enter: "))
                
                for i in range(num_tasks):
                    print(f"\n--- Entering Task {i + 1} of {num_tasks} ---")
                    
                    # Keep looping until valid unique entries are provided
                    while True:
                        t_id = input("Enter custom Task ID: ").strip()
                        t_name = input("Enter task description: ").strip()
                        
                        # Check 1: Empty Fields
                        if not t_id or not t_name:
                            print("❌ Error: Both ID and Task description are required. Try again.")
                            continue
                        
                        # Check 2: Duplicates
                        id_exists = any(task['id'] == t_id for task in my_tasks)
                        name_exists = any(task['task'].lower() == t_name.lower() for task in my_tasks)
                        
                        if id_exists:
                            print(f"❌ Error: Task ID '{t_id}' already exists! Try a different ID.")
                        elif name_exists:
                            print(f"❌ Error: Task description '{t_name}' already exists! Try a different description.")
                        else:
                            # Inputs are perfectly unique, break inner loop to move to next task
                            my_tasks = create_task(t_id, t_name, my_tasks)
                            print("✨ Success: Task successfully saved to memory!")
                            break  
                            
            except ValueError:
                print("❌ Error: Please enter a valid whole number.")
                
        elif choice == "2":
            display_tasks(my_tasks)
            
        elif choice == "3":
            print("\nWarning: RAM is volatile. Terminating the process will clear all data.")
            print("Shutting down... Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
# Run the main function when the script is executed
if __name__ == "__main__":
    main()
