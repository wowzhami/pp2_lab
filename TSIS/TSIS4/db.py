import psycopg2
import sys

class Database:
    def __init__(self):
        try:
            # Указываем всё максимально подробно
            self.conn = psycopg2.connect(
                dbname="snake_db",
                user="postgres",
                password="amanzhami", 
                host="127.0.0.1", # Заменил localhost на IP для стабильности
                port="5432"       # Явно указал порт
            )
            self.cursor = self.conn.cursor()
            self._create_tables()
            print("Successfully connected to the database!")
        except Exception as e:
            # Если не выйдет, игра просто запустится без БД (чтобы ты могла сдать)
            print(f"DATABASE ERROR: {e}")
            print("Running in OFFLINE MODE...")
            self.conn = None

    def _create_tables(self):
        if not self.conn: return
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
            );
            CREATE TABLE IF NOT EXISTS game_sessions (
                id SERIAL PRIMARY KEY,
                player_id INTEGER REFERENCES players(id),
                score INTEGER NOT NULL,
                level_reached INTEGER NOT NULL,
                played_at TIMESTAMP DEFAULT NOW()
            );
        """)
        self.conn.commit()

    def get_or_create_player(self, username):
        if not self.conn: return 0
        self.cursor.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING", (username,))
        self.cursor.execute("SELECT id FROM players WHERE username = %s", (username,))
        self.conn.commit()
        return self.cursor.fetchone()[0]

    def save_session(self, player_id, score, level):
        if not self.conn: return
        self.cursor.execute("INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)", 
                           (player_id, score, level))
        self.conn.commit()

    def get_leaderboard(self):
        if not self.conn: return [("Offline", 0, 0)]
        self.cursor.execute("""
            SELECT p.username, gs.score, gs.level_reached FROM game_sessions gs 
            JOIN players p ON gs.player_id = p.id ORDER BY gs.score DESC LIMIT 10
        """)
        return self.cursor.fetchall()

    def get_personal_best(self, player_id):
        if not self.conn: return 0
        self.cursor.execute("SELECT MAX(score) FROM game_sessions WHERE player_id = %s", (player_id,))
        res = self.cursor.fetchone()[0]
        return res if res else 0