import csv

def export_to_csv(filename="tasks.csv"):
    if not tasks:
        print("Aucune tâche à exporter.")
        return
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Numéro", "Tâche"])
            for i, task in enumerate(tasks, 1):
                writer.writerow([i, task])
        print(f"Tâches exportées avec succès dans {filename}")
    except Exception as e:
        print(f"Erreur lors de l'export : {e}")
        
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
        try:
          task = input("Tâche : ")
          add_task(task)
        except ValueError:
          print("Entrée invalide, veuillez entrer un nombre.")
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        index = int(input("Index à supprimer (int) : "))
        remove_task(index)
    elif choice == '4':
        break
