def todo_list():
    tasks = []
    while True:
        task = input("Enter a task (type 'done' to exit)")
        if task == 'done':
            break
        tasks.append(task)

    
    print("\n Your Todo list :")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


todo_list()