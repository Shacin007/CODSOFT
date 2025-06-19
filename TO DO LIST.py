List=[]
def add_task():
    ent_task=input("Enter a task:")
    if ent_task not in List:
                List.append(ent_task)
                print("Task Added")
    else:
        print("Task already exsisted : ")
def remove_task():
    rem_task=input("Enter a task to be removed:")
    if rem_task in List:
                 List.remove(rem_task)
                 print("Task Removed")
    else:
        print("Task not found")
def view_task():
    print(List)
while True:
    print("Main Menu :")
    print ("1.Add Task")
    print ("2.Remove Task")
    print ("3.View Task")
    print ("4.End Task")
    ch=int(input("Enter your choice:"))
    if ch==1:
     add_task()
    elif ch==2:
        remove_task()
    elif ch==3:
        view_task()
    elif ch == 4:
        print("Exiting task manager.")
        break
    else:
         print("Enter a valid choice")
        
        
    
       

        
