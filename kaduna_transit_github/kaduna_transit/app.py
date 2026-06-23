from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from chatbot_engine import process_message
import json
import os

app = Flask(__name__)
app.secret_key = "kaduna_transit_secret_2025"

ADMIN_PASSWORD = "admin1234"
ROUTES_FILE = os.path.join(os.path.dirname(__file__), "routes.json")


def load_routes():
    if not os.path.exists(ROUTES_FILE):
        return {}
    with open(ROUTES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_routes(routes):
    with open(ROUTES_FILE, "w", encoding="utf-8") as f:
        json.dump(routes, f, ensure_ascii=False, indent=2)


# ── Main chatbot ─────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify({"reply": "Please type a message."})
    response = process_message(user_message)
    return jsonify({"reply": response})


# ── Admin login ──────────────────────────────────────────────
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(url_for("admin"))
        else:
            return render_template("admin.html", error="Wrong password", logged_in=False, routes={})

    if not session.get("admin"):
        return render_template("admin.html", logged_in=False, routes={}, error=None)

    routes = load_routes()
    return render_template("admin.html", logged_in=True, routes=routes, error=None)


@app.route("/admin/logout")
def admin_logout():
    session.pop("admin", None)
    return redirect(url_for("admin"))


# ── Admin: Add route ─────────────────────────────────────────
@app.route("/admin/add", methods=["POST"])
def admin_add():
    if not session.get("admin"):
        return redirect(url_for("admin"))

    origin      = request.form.get("origin", "").strip().lower()
    destination = request.form.get("destination", "").strip().lower()
    vehicle     = request.form.get("vehicle", "").strip()
    fare        = request.form.get("fare", "").strip()
    duration    = request.form.get("duration", "").strip()
    notes       = request.form.get("notes", "").strip()

    if not all([origin, destination, vehicle, fare, duration, notes]):
        routes = load_routes()
        return render_template("admin.html", logged_in=True, routes=routes,
                               error="All fields are required.")

    routes = load_routes()
    key = f"{origin}|{destination}"

    new_option = {
        "vehicle": vehicle,
        "fare": fare,
        "duration": duration,
        "notes": notes
    }

    if key in routes:
        routes[key].append(new_option)
    else:
        routes[key] = [new_option]

    save_routes(routes)
    return redirect(url_for("admin"))


# ── Admin: Delete route ──────────────────────────────────────
@app.route("/admin/delete", methods=["POST"])
def admin_delete():
    if not session.get("admin"):
        return redirect(url_for("admin"))

    key = request.form.get("key", "")
    routes = load_routes()

    if key in routes:
        del routes[key]
        save_routes(routes)

    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True)
