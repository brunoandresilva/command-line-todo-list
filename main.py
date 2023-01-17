import sqlite3


def main():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()


    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='todos'")
    result = c.fetchone()

    if not result:
        c.execute('''CREATE TABLE todos (task text, status text)''')
        
    flag = True
    while flag:
        print("1-> List all my tasks")
        print("2-> Add new task")
        print("3-> Mark a task as Done")
        print("4-> Exit")
        option = int(input("Option: "))
        while option < 1 or option > 4:
            print("1-> List all my tasks")
            print("2-> Add new task")
            print("3-> Mark a task as Done")
            print("4-> Exit")
            option = input("Option: ")
        if option == 1:
            c.execute("SELECT * FROM todos")
            rows = c.fetchall()
            for row in rows:
                print(row)
        if option == 2:
            task = input("New task to Add: ")
            status = "Not Completed"
            c.execute("INSERT INTO todos (task, status) VALUES (?,?)", (task, status))
        if option == 3:
            task = input("Task to delete: ")
            c.execute("DELETE FROM todos WHERE task = ?", (task,))
        if option == 4:
            flag = False

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()