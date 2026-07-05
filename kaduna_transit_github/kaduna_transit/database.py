import os
import json
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.environ.get("DATABASE_URL")


def get_conn():
    return psycopg2.connect(DATABASE_URL)


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routes (id SERIAL PRIMARY KEY, origin TEXT NOT NULL, destination TEXT NOT NULL, vehicle TEXT NOT NULL, fare TEXT NOT NULL, duration TEXT NOT NULL, notes TEXT NOT NULL)")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM routes")
    count = cur.fetchone()[0]
    if count == 0:
        json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "routes.json")
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for key, options in data.items():
                parts = key.split("|")
                if len(parts) == 2:
                    origin, destination = parts[0].strip(), parts[1].strip()
                    for opt in options:
                        cur.execute("INSERT INTO routes (origin, destination, vehicle, fare, duration, notes) VALUES (%s, %s, %s, %s, %s, %s)", (origin, destination, opt.get("vehicle", ""), opt.get("fare", ""), opt.get("duration", ""), opt.get("notes", "")))
            conn.commit()
    cur.close()
    conn.close()


def load_routes():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM routes ORDER BY origin, destination")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    routes = {}
    for row in rows:
        key = f"{row['origin']}|{row['destination']}"
        if key not in routes:
            routes[key] = []
        routes[key].append({"id": row["id"], "vehicle": row["vehicle"], "fare": row["fare"], "duration": row["duration"], "notes": row["notes"]})
    return routes


def load_routes_for_chatbot():
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM routes ORDER BY origin, destination")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    routes = {}
    for row in rows:
        key = f"{row['origin']}|{row['destination']}"
        if key not in routes:
            routes[key] = []
        routes[key].append({"vehicle": row["vehicle"], "fare": row["fare"], "duration": row["duration"], "notes": row["notes"]})
    return routes


def save_route(origin, destination, vehicle, fare, duration, notes):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO routes (origin, destination, vehicle, fare, duration, notes) VALUES (%s, %s, %s, %s, %s, %s)", (origin, destination, vehicle, fare, duration, notes))
    conn.commit()
    cur.close()
    conn.close()


def update_route(route_id, vehicle, fare, duration, notes):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE routes SET vehicle=%s, fare=%s, duration=%s, notes=%s WHERE id=%s", (vehicle, fare, duration, notes, route_id))
    conn.commit()
    cur.close()
    conn.close()


def delete_route(route_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM routes WHERE id=%s", (route_id,))
    conn.commit()
    cur.close()
    conn.close()
