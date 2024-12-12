# To-Do List 

import os

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def __str__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.name}"


class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, name):
        task = Task(name)
        self.tasks.append(task)
        print(f"Görev eklendi: {name}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print(f"Görev tamamlandı: {self.tasks[index].name}")
        else:
            print("Geçersiz görev numarası!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Görev silindi: {removed_task.name}")
        else:
            print("Geçersiz görev numarası!")

    def list_tasks(self):
        print("\nYapılacak Görevler:")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.name}|{task.completed}\n")
        print("Görevler kaydedildi.")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    name, completed = line.strip().split("|")
                    self.tasks.append(Task(name, completed == "True"))
            print("Görevler yüklendi.")
        else:
            print("Kayıtlı görev bulunamadı.")


def main():
    manager = TaskManager()

    while True:
        print("\n1. Görev Ekle")
        print("2. Görevi Tamamla")
        print("3. Görev Sil")
        print("4. Görevleri Listele")
        print("5. Çıkış")
        
        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            name = input("Görev adını girin: ")
            manager.add_task(name)
        elif choice == "2":
            manager.list_tasks()
            try:
                index = int(input("Tamamlamak istediğiniz görev numarasını girin: "))
                manager.complete_task(index)
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")
        elif choice == "3":
            manager.list_tasks()
            try:
                index = int(input("Silmek istediğiniz görev numarasını girin: "))
                manager.delete_task(index)
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")
        elif choice == "4":
            manager.list_tasks()
        elif choice == "5":
            manager.save_tasks()
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()