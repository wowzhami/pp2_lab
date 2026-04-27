import psycopg2
from connect import get_connection

def search():
    pattern = input("Введите имя или номер для поиска: ")
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
        for row in cur.fetchall():
            print(f"Контакт: {row[0]} | Тел: {row[1]}")
    conn.close()

def upsert():
    name = input("Имя: ")
    phone = input("Телефон: ")
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        conn.commit()
        print("Готово!")
    conn.close()

def show_with_pagination():
    limit = 3
    offset = 0
    conn = get_connection()
    while True:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            rows = cur.fetchall()
            print(f"\n--- Страница {(offset//limit)+1} ---")
            for r in rows:
                print(f"{r[0]}: {r[1]}")
        
        cmd = input("\nn - дальше, q - выход: ")
        if cmd == 'n': offset += limit
        else: break
    conn.close()

def delete():
    target = input("Введите имя или номер для удаления: ")
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("CALL delete_contact_adv(%s)", (target,))
        conn.commit()
        print("Запись удалена.")
    conn.close()

if __name__ == "__main__":
    while True:
        print("\n--- Practice 8 ---")
        print("1. Поиск (Function)\n2. Добавить/Обновить (Procedure)\n3. Пагинация\n4. Удалить\n0. Выход")
        ch = input("> ")
        if ch == '1': search()
        elif ch == '2': upsert()
        elif ch == '3': show_with_pagination()
        elif ch == '4': delete()
        elif ch == '0': break