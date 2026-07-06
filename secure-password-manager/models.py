from database import get_connection
from encryption import encrypt, decrypt

class PasswordManager:

    def add_password(self, website, username, password, notes):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO passwords(website,username,password,notes) VALUES(?,?,?,?)",
            (website, username, encrypt(password), notes)
        )
        conn.commit()
        conn.close()

    def get_all(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM passwords")
        rows = cur.fetchall()
        conn.close()
        result = []
        for r in rows:
            result.append((r[0], r[1], r[2], decrypt(r[3]), r[4]))
        return result

    def search(self, keyword):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM passwords WHERE website LIKE ?", (f"%{keyword}%",))
        rows = cur.fetchall()
        conn.close()
        return [(r[0], r[1], r[2], decrypt(r[3]), r[4]) for r in rows]

    def delete(self, pid):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM passwords WHERE id=?", (pid,))
        conn.commit()
        conn.close()
