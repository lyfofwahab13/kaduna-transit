"""
Run this ONCE to convert your existing transport_data.py into routes.json
Command: python3 export_routes.py
"""
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from transport_data import TRANSPORT_ROUTES

routes_json = {}
for (origin, destination), options in TRANSPORT_ROUTES.items():
    key = f"{origin}|{destination}"
    routes_json[key] = options

with open("routes.json", "w", encoding="utf-8") as f:
    json.dump(routes_json, f, ensure_ascii=False, indent=2)

print(f"✅ Done! Exported {len(routes_json)} routes to routes.json")
