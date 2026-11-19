"""SQLite 저장소: 계획, 세션별 실행 이벤트, 대화 맥락."""
import json, os, sqlite3
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path(os.getenv("DATABASE_PATH", Path(__file__).resolve().parent / "data" / "fire_agent.db"))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with connect() as c:
        c.executescript('''
        CREATE TABLE IF NOT EXISTS plans (
          id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, region TEXT,
          plan_date TEXT NOT NULL, start_time TEXT, end_time TEXT,
          payload TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS execution_logs (
          id INTEGER PRIMARY KEY AUTOINCREMENT, session_id TEXT NOT NULL,
          event_type TEXT NOT NULL, timestamp TEXT NOT NULL, payload TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_logs_session ON execution_logs(session_id, id);
        CREATE TABLE IF NOT EXISTS conversations (
          session_id TEXT PRIMARY KEY, memory TEXT NOT NULL, updated_at TEXT NOT NULL
        );
        ''')


def save_event(event):
    with connect() as c:
        c.execute('INSERT INTO execution_logs(session_id,event_type,timestamp,payload) VALUES(?,?,?,?)',
                  (event['session_id'], event['event_type'], event['timestamp'], json.dumps(event['payload'], ensure_ascii=False)))


def list_logs(limit=100):
    with connect() as c:
        rows=c.execute('SELECT session_id, MIN(timestamp) started_at, MAX(timestamp) ended_at, COUNT(*) event_count FROM execution_logs GROUP BY session_id ORDER BY MAX(id) DESC LIMIT ?', (limit,)).fetchall()
        return [dict(r) for r in rows]


def get_logs(session_id):
    with connect() as c:
        rows=c.execute('SELECT id,session_id,event_type,timestamp,payload FROM execution_logs WHERE session_id=? ORDER BY id', (session_id,)).fetchall()
        return [{**dict(r), 'payload':json.loads(r['payload'])} for r in rows]


def delete_logs(session_id):
    with connect() as c:
        cur=c.execute('DELETE FROM execution_logs WHERE session_id=?',(session_id,))
        return cur.rowcount


def get_memory(session_id):
    with connect() as c:
        row=c.execute('SELECT memory FROM conversations WHERE session_id=?',(session_id,)).fetchone()
        return json.loads(row['memory']) if row else []


def save_memory(session_id, memory):
    with connect() as c:
        c.execute('INSERT INTO conversations(session_id,memory,updated_at) VALUES(?,?,?) ON CONFLICT(session_id) DO UPDATE SET memory=excluded.memory, updated_at=excluded.updated_at',
                  (session_id,json.dumps(memory,ensure_ascii=False),datetime.now(timezone.utc).isoformat()))


def _overlap(a_start,a_end,b_start,b_end):
    if not all([a_start,a_end,b_start,b_end]): return False
    return a_start < b_end and b_start < a_end


def create_plan(data):
    now=datetime.now(timezone.utc).isoformat()
    payload=dict(data)
    with connect() as c:
        rows=c.execute('SELECT id,start_time,end_time FROM plans WHERE plan_date=?',(data['plan_date'],)).fetchall()
        overlaps=[r['id'] for r in rows if _overlap(data.get('start_time'),data.get('end_time'),r['start_time'],r['end_time'])]
        cur=c.execute('INSERT INTO plans(title,region,plan_date,start_time,end_time,payload,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?)',
          (data['title'],data.get('region'),data['plan_date'],data.get('start_time'),data.get('end_time'),json.dumps(payload,ensure_ascii=False),now,now))
        return {'id':cur.lastrowid,'overlap':bool(overlaps),'overlapping_plan_ids':overlaps,'created_at':now,**payload}


def list_plans():
    with connect() as c:
        rows=c.execute('SELECT * FROM plans ORDER BY plan_date,start_time,id').fetchall()
        return [_plan_row(r) for r in rows]


def get_plan(plan_id):
    with connect() as c:
        r=c.execute('SELECT * FROM plans WHERE id=?',(plan_id,)).fetchone()
        return _plan_row(r) if r else None


def _plan_row(r):
    if not r: return None
    return {'id':r['id'],**json.loads(r['payload']),'created_at':r['created_at'],'updated_at':r['updated_at']}


def update_plan(plan_id,data):
    old=get_plan(plan_id)
    if not old:return None
    merged={**{k:v for k,v in old.items() if k not in ('id','created_at','updated_at','overlap','overlapping_plan_ids')},**data}
    now=datetime.now(timezone.utc).isoformat()
    with connect() as c:
        rows=c.execute('SELECT id,start_time,end_time FROM plans WHERE plan_date=? AND id<>?',(merged['plan_date'],plan_id)).fetchall()
        overlaps=[r['id'] for r in rows if _overlap(merged.get('start_time'),merged.get('end_time'),r['start_time'],r['end_time'])]
        c.execute('UPDATE plans SET title=?,region=?,plan_date=?,start_time=?,end_time=?,payload=?,updated_at=? WHERE id=?',
          (merged['title'],merged.get('region'),merged['plan_date'],merged.get('start_time'),merged.get('end_time'),json.dumps(merged,ensure_ascii=False),now,plan_id))
    return {'id':plan_id,**merged,'overlap':bool(overlaps),'overlapping_plan_ids':overlaps,'created_at':old['created_at'],'updated_at':now}


def delete_plan(plan_id):
    with connect() as c:
        cur=c.execute('DELETE FROM plans WHERE id=?',(plan_id,))
        return cur.rowcount>0

init_db()
