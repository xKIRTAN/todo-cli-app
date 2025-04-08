class Todo:
    def __init__(self):
        self.tasks = {}
        self.menu_card()

    def add_task(self, task):
        if task in self.tasks:
            print(f"Task '{task}' already exists.")
        else:
            self.tasks[task] = False
            print(f"Task '{task}' added.")

    def view_tasks(self):
        print('------------------------ TO-DO LIST ------------------------')
        if not self.tasks:
            print("No tasks found.")
        else:
            for task, done in self.tasks.items():
                status = "✅ Done" if done else "❌ Not Done"
                print(f"- {task}: {status}")
        print('-----------------------------------------------------------')

    def delete_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Task '{task}' deleted.")
        else:
            print(f"Task '{task}' not found.")

    
    def update_task(self, task):
        if task in self.tasks:
            self.tasks[task] = True
            print(f"Task '{task}' updated to ✅ Done.")
        else:
            print(f"Task '{task}' not found.")

    def menu_card(self):
        while 1:
            print('------------------------ Welcome to the To-Do List ------------------------')
            print('1. Add task')
            print('2. View task')
            print('3. Delete task')
            print('4. Update task')
            print('0. Exit Application')

            try:
                choice = int(input('Enter your choice:'))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue    
            if choice == 1:
                user_task = input('Enter task to add:')
                self.add_task(user_task)
            
            elif choice == 2:
                self.view_tasks()
    
            elif choice == 3:
                user_task = input('Enter task to delete:')
                self.delete_task(user_task)
    
            elif choice == 4:
                user_task = input('Enter task to update:')
                self.update_task(user_task)
        
            elif choice == 0:
                print()
                print('Arigato!')
                break
            print()