import csv
import json
from connect import get_connection

def create_table():
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    user_name VARCHAR(100),
                    email VARCHAR(100),
                    birthday DATE,
                    group_id INTEGER
                );
            """)
            conn.commit()
        conn.close()

def import_from_csv(file_name):
    conn = get_connection()
    if not conn: return
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute(
                        "INSERT INTO phonebook (user_name, email) VALUES (%s, %s)",
                        (row[0], row[1])
                    )
                conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def query_contacts():
    search = input("Search (name/email/phone): ")
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s)", (search,))
            res = cur.fetchall()
            for row in res:
                print(f"Name: {row[0]} | Email: {row[1]} | Phone: {row[2]}")
        conn.close()

def paginate_contacts():
    limit = 5
    offset = 0
    while True:
        conn = get_connection()
        if conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_name, email FROM phonebook LIMIT %s OFFSET %s", (limit, offset))
                rows = cur.fetchall()
                print(f"\n--- Page {(offset // limit) + 1} ---")
                for r in rows:
                    print(f"{r[0]} | {r[1]}")
            conn.close()
        move = input("\n[n] Next, [p] Prev, [q] Quit: ").lower()
        if move == 'n': offset += limit
        elif move == 'p' and offset >= limit: offset -= limit
        elif move == 'q': break

def export_to_json(file_name="contacts.json"):
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT pb.user_name, pb.email, g.name, ARRAY_AGG(ph.phone) 
                FROM phonebook pb
                LEFT JOIN groups g ON pb.group_id = g.id
                LEFT JOIN phones ph ON pb.id = ph.contact_id
                GROUP BY pb.id, g.name
            """)
            data = [{"name": r[0], "email": r[1], "group": r[2], "phones": r[3]} for r in cur.fetchall()]
            with open(file_name, "w") as f:
                json.dump(data, f, indent=4)
            print("Done!")
        conn.close()

def update_phone():
    name = input("Name: ")
    new_email = input("New Email: ")
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET email = %s WHERE user_name = %s", (new_email, name))
            conn.commit()
        conn.close()

def delete_contact():
    name = input("Name to delete: ")
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE user_name = %s", (name,))
            conn.commit()
        conn.close()

def move_contact_to_group():
    name = input("Contact Name: ")
    group = input("Group Name: ")
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("CALL move_to_group(%s, %s)", (name, group))
            conn.commit()
        conn.close()

if __name__ == "__main__":
    create_table()
    while True:
        print("\n1. Import CSV | 2. Search | 3. Update | 4. Delete | 5. Pages | 6. Export JSON | 7. Change Group | 0. Exit")
        choice = input("> ")
        if choice == '1': import_from_csv('contacts.csv')
        elif choice == '2': query_contacts()
        elif choice == '3': update_phone()
        elif choice == '4': delete_contact()
        elif choice == '5': paginate_contacts()
        elif choice == '6': export_to_json()
        elif choice == '7': move_contact_to_group()
        elif choice == '0': break