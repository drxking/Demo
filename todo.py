import os
import ast
import time
import random as r
tt = r.randint(1,3)
for i in range(0,101):
			print(f"----- Loading {i}% -----" , end="\r")
			time.sleep(0.005 * tt)
print("Welcome to TO-DO list Manager!")
if not os.path.exists("oho.txt"):
	with open("oho.txt","x")as f:
		f.write("[]")
		for i in range(0,101):
			print(f"- Creating Storage file {i}%" , end="\r")
			time.sleep(0.005 * tt)
		print('''- Storage file created successfully ("oho.txt") ''')
print('''
Commands:
- Type 'add' to add a new task.Type '***' in Task Description to exit from add command.
- Type 'view' to view your to-do list.
- Type 'complete' to mark a task as completed.
- Type 'quit' to exit''')


store = []
with open("oho.txt", "r") as f:
	imp = f.read()
store =  ast.literal_eval(imp)
while True:             
    command = input("\nEnter the command: ")
    command = command.lower()
    if command == "add":
        desc = input("\nTask Description : ")
        if desc != "***":
            date = input("Due Date (optional): ")
            if date == "" or date == " ":
                date = "*"
            print(f"- Task '{desc} on {date}' added to To-Do list")
            store.append({desc : date})
            with open("oho.txt" , "w") as f:
            	f.write(f"{store}")
        else:
            print("-Exited from Add")
    elif command == "view":
        if len(store) != 0:
            number = 0
            print("\n--- To-Do List ---")
            for i in store:
                for j in i:
                    print(f"{number + 1}. '{j}' ( On : {i[j]})")
                    number += 1
        else:
            print('''-To_do List is empty, type "add" to Add the Task!!!''')
        
    elif command == "complete":
        while True:
            if len(store) == 0:
                print('''-To_do List is empty, type "add" to Add the Task!!!''')
                break
            remo = input('''\nEnter the task number to mark as completed(must use a number): ''')
            if remo.isdigit() :
                remo = int(remo)
                if remo <= len(store):
                    getelem = store[remo-1]
                    for i in getelem:
                        print(f"-Task '{i}' marked as completed and removed from your to-do list.")
                    store.remove(getelem)
                    with open("oho.txt","w") as f:
                    	f.write(f"{store}")
                    break
                else:
                    print('''-Invalid Number , type "exit" to exit and view the list...''')
            elif(remo == "*"):
            	store.clear()
            	with open("oho.txt","w") as f:
                    	f.write(f"{store}")
            	print("-Everything is cleared.")
            	break
            	
            elif(remo == 'exit'):
                break

            else:
                print('''-Must be Number or type "exit" to exit ''')

    elif command == "quit":
        print("Thank you for your consideration!!!")
        break

    else:
        print("-Invalid Command")