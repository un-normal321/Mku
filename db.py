import aiosqlite

DB_PATH = "conversations.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            role TEXT,
            content TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        await db.commit()

async def save_message(session_id: str, role: str, content: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
            (session_id, role, content)
        )
        await db.commit()

async def load_history(session_id: str, limit: int = 40):
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute(
            "SELECT role, content FROM messages WHERE session_id = ? ORDER BY id DESC LIMIT ?",
            (session_id, limit)
        )
        rows = await cur.fetchall()
    return [{"role": r[0], "content": r[1]} for r in reversed(rows)]
