from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from chatbot_engine import process_message
from database import init_db, load_routes, save_route, delete_route, update_route
import os

app = Flask(__name__)
app.secret_key = "kaduna_transit_secret_2025"
ADMIN_PASSWORD = "admin1234"


# ── Init database on startup ─────────────────────────────────
with app.app_context():
    init_db()


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
    save_route(origin, destination, vehicle, fare, duration, notes)
    return redirect(url_for("admin"))


# ── Admin: Edit route ─────────────────────────────────────────
@app.route("/admin/edit", methods=["POST"])
def admin_edit():
    if not session.get("admin"):
        return redirect(url_for("admin"))
    route_id = request.form.get("route_id", "")
    vehicle  = request.form.get("vehicle", "").strip()
    fare     = request.form.get("fare", "").strip()
    duration = request.form.get("duration", "").strip()
    notes    = request.form.get("notes", "").strip()
    if not all([route_id, vehicle, fare, duration, notes]):
        return redirect(url_for("admin"))
    update_route(route_id, vehicle, fare, duration, notes)
    return redirect(url_for("admin"))


# ── Admin: Delete route ──────────────────────────────────────
@app.route("/admin/delete", methods=["POST"])
def admin_delete():
    if not session.get("admin"):
        return redirect(url_for("admin"))
    route_id = request.form.get("route_id", "")
    if route_id:
        delete_route(route_id)
    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True)
