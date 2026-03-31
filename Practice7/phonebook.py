import csv
from connect import get_connection

def create_table():
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    user_name VARCHAR(100),
                    phone_number VARCHAR(20)
                );
            """)
            conn.commit()
        conn.close()
        print("--- Таблица создана или уже существует ---")

def import_from_csv(file_name):
    conn = get_connection()
    if not conn: return
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute(
                        "INSERT INTO phonebook (user_name, phone_number) VALUES (%s, %s)",
                        (row[0], row[1])
                    )
                conn.commit()
        print(f"--- Данные из {file_name} успешно импортированы! ---")
    except Exception as e:
        print(f"Ошибка при импорте: {e}")
    finally:
        conn.close()

def query_contacts():
    search = input("Введите имя или часть номера для поиска: ")
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM phonebook 
                WHERE user_name ILIKE %s OR phone_number LIKE %s
            """, (f'%{search}%', f'%{search}%'))
            
            results = cur.fetchall()
            if not results:
                print("Никого не нашли :(")
            for row in results:
                print(f"ID: {row[0]} | Имя: {row[1]} | Тел: {row[2]}")
        conn.close()

if __name__ == "__main__":
    create_table()         
    import_from_csv('contacts.csv')  
    
    print("\n--- Проверка поиска ---")
    query_contacts()       

def update_phone():
    name = input("Кому меняем номер? (Введите имя): ")
    new_phone = input("Введите новый номер: ")
    
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            # SQL запрос на обновление
            cur.execute(
                "UPDATE phonebook SET phone_number = %s WHERE user_name = %s",
                (new_phone, name)
            )
            conn.commit()
            if cur.rowcount > 0:
                print(f"--- Номер для {name} успешно обновлен! ---")
            else:
                print("--- Контакт не найден ---")
        conn.close()



def delete_contact():
    name = input("Кого удалить? (Введите имя): ")
    
    conn = get_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE user_name = %s", (name,))
            conn.commit()
            print(f"--- Контакт {name} удален (если он был) ---")
        conn.close()



if __name__ == "__main__":
    create_table()
    
    while True:
        print("\nМеню:")
        print("1. Импорт из CSV")
        print("2. Поиск")
        print("3. Обновить номер")
        print("4. Удалить контакт")
        print("5. Выход")
        
        choice = input("Выбери действие: ")
        
        if choice == '1':
            import_from_csv('contacts.csv')
        elif choice == '2':
            query_contacts()
        elif choice == '3':
            update_phone()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            break
        else:
            print("Нет такого пункта!")
            