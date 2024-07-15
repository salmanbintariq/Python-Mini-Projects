def task():
    print("---Welcome to the ToDo Application---")
    tasks = [] #list

    total_tasks = int(input("Enter how many tasks you want to do:  "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter the Task{i} = ")
        tasks.append(task_name)
    print(f"Today's tasks are:\n{tasks}")

    while True:
        print("Do you want to perform more operations?")
        operations = int(input("1.Add Tasks \n2.View Tasks \n3.Update Tasks \n4.Delete Tasks \n5.Exit \n"))

        if operations == 1: #Add task in list
            add_task = input("Enter the task you want to add: ")
            tasks.append(add_task)
            print(f"Task '{add_task}' has been successfully added.")

        elif operations == 2: #View task in list
            print(f"Total tasks : {tasks}")

        elif operations == 3: #Update task in list
            update_task = input("Enter the task name you want to update: ")
            if update_task in tasks:
                up = input("Enter new Task: ")  
                ind = tasks.index(update_task)
                tasks[ind] = up  
                print(f"Updated task {up}.")
            else:
                print("Please enter a valid task.")    

        elif operations == 4: #Delete task in list
            delete_task = input("Enter the task name you want to delete: ")
            if delete_task in tasks:
                ind = tasks.index(delete_task)
                del tasks[ind]
                print(f"Your task {delete_task} is successfully deleted.")
            else:
                print("Please a enter a valid task.")            
        
        elif operations == 5: #Exit the program
            print("---Application Closed---")
            break
        
        else:
            print("Please enter a valid operation.")

task()
