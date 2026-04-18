from manager import StudentManager

def print_menu():
    print("\n╔══════════════════════════════╗")
    print("║   Student Management System  ║")
    print("╠══════════════════════════════╣")
    print("║  1. Add Student              ║")
    print("║  2. Update Student           ║")
    print("║  3. Delete Student           ║")
    print("║  4. List All Students        ║")
    print("║  5. Find Student by ID       ║")
    print("║  6. Exit                     ║")
    print("╚══════════════════════════════╝")

def main():
    manager = StudentManager()
    print("🎓 Welcome to the Student Management System!")

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\n-- Add New Student --")
            sid = input("Enter Student ID: ").strip()
            name = input("Enter Name: ").strip()
            grade = input("Enter Grade (e.g. A, B+, 85): ").strip()
            if sid and name and grade:
                manager.add_student(sid, name, grade)
            else:
                print("❌ All fields are required.")

        elif choice == "2":
            print("\n-- Update Student --")
            sid = input("Enter Student ID to update: ").strip()
            name = input("New Name (press Enter to skip): ").strip()
            grade = input("New Grade (press Enter to skip): ").strip()
            manager.update_student(sid, name or None, grade or None)

        elif choice == "3":
            print("\n-- Delete Student --")
            sid = input("Enter Student ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete '{sid}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                manager.delete_student(sid)
            else:
                print("❎ Deletion cancelled.")

        elif choice == "4":
            print("\n-- All Students --")
            manager.list_students()

        elif choice == "5":
            print("\n-- Find Student --")
            sid = input("Enter Student ID: ").strip()
            manager.find_student(sid)

        elif choice == "6":
            print("\n👋 Goodbye! Exiting system.")
            break

        else:
            print("⚠️  Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()