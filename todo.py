tasks = []

def edit_task(index, new_task):
    if 1 <= index <= len(tasks):
        old = tasks[index - 1]
        tasks[index - 1] = new_task
        print(f"Tâche modifiée : {old} -> {new_task}")
    else:
        print("Index invalide.")

def add_task(task):
    tasks.append(task)
    print(f"Tâche ajoutée : {task}")

def list_tasks():
    if not tasks:
        print("Aucune tâche.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Tâche supprimée : {removed}")
    else:
        print("Index invalide.")

# Menu simple
while True:
    print("\n1. Ajouter tâche\n2. Lister tâches\n3. Supprimer tâche\n4. Quitter")
    choice = input("Choix : ")
    if choice == '1':
        task = input("Tâche : ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        index = int(input("Index à supprimer : "))
        remove_task(index)
    elif choice == '4':
        break
