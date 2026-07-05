# ============================================================
# Chatbot Engine — reads routes from routes.json (scalable)
# ============================================================
import re
import string
import json
import os

ROUTES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "routes.json")


def load_routes():
    """Load routes from JSON file at runtime so new routes work immediately."""
    if not os.path.exists(ROUTES_FILE):
        # Fallback to transport_data.py if JSON not generated yet
        from transport_data import TRANSPORT_ROUTES
        routes = {}
        for (o, d), opts in TRANSPORT_ROUTES.items():
            routes[f"{o}|{d}"] = opts
        return routes
    with open(ROUTES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_all_locations():
    """Derive all known locations from routes.json dynamically."""
    routes = load_routes()
    locs = set()
    for key in routes:
        parts = key.split("|")
        if len(parts) == 2:
            locs.add(parts[0].strip())
            locs.add(parts[1].strip())
    return sorted(locs, key=len, reverse=True)


def normalize(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.strip()


def extract_locations(user_input):
    normalized_input = normalize(user_input)
    all_locations = get_all_locations()
    found_with_pos = []
    for loc in all_locations:
        pos = normalized_input.find(loc)
        if pos != -1:
            found_with_pos.append((pos, loc))
            normalized_input = normalized_input.replace(loc, "_" * len(loc), 1)
    found_with_pos.sort(key=lambda x: x[0])
    return [loc for pos, loc in found_with_pos]


GREETING_WORDS = {"hello", "hi", "hey", "good morning", "good afternoon", "good evening"}
FAREWELL_WORDS = {"bye", "goodbye", "thanks", "thank you", "exit", "done"}
HELP_WORDS     = {"help", "what can you do", "how does this work"}
LIST_WORDS     = {"list", "show", "all areas", "all locations", "available", "which areas"}


def detect_intent(user_input):
    text   = normalize(user_input)
    tokens = set(text.split())
    if tokens & GREETING_WORDS or any(g in text for g in GREETING_WORDS): return "greeting"
    if tokens & FAREWELL_WORDS or any(f in text for f in FAREWELL_WORDS): return "farewell"
    if tokens & HELP_WORDS     or any(h in text for h in HELP_WORDS):     return "help"
    if tokens & LIST_WORDS     or any(l in text for l in LIST_WORDS):     return "list_areas"
    return "transport_query"


def get_areas_list():
    areas = sorted([l.title() for l in get_all_locations()])
    return "list_areas:" + ",".join(areas)


WELCOME = (
    "👋 Hi! I'm Aisha — your Kaduna public transport assistant.\n\n"
    "Tell me where you're going and I'll show you all available vehicle options with fares.\n\n"
    "Example: \"I want to go from Sabon Tasha to Barnawa\""
)

HELP_MSG = (
    "ℹ️ How to use:\n\n"
    "1️⃣ Type your origin and destination.\n"
    "   e.g. \"From Barnawa to Kawo\"\n\n"
    "2️⃣ I'll show you Keke and Bus options with different fares.\n\n"
    "3️⃣ Type \"list areas\" to see all supported locations."
)

FAREWELL_MSG = "👋 Thank you for using Aisha. Safe travels!"


def process_message(user_input):
    if not user_input or not user_input.strip():
        return "Please type a message so I can help you. 😊"

    intent = detect_intent(user_input)
    if intent == "greeting":   return WELCOME
    if intent == "farewell":   return FAREWELL_MSG
    if intent == "help":       return HELP_MSG
    if intent == "list_areas": return get_areas_list()

    locations = extract_locations(user_input)

    if len(locations) == 0:
        return (
            "🤔 I couldn't identify any Kaduna locations in your message.\n\n"
            "Please mention a valid pickup and destination.\n"
            "Example: \"From Sabon Tasha to Barnawa\"\n\n"
            "Type \"list areas\" to see all supported locations."
        )

    if len(locations) == 1:
        loc = locations[0].title()
        return (
            f"📍 I found one location: {loc}\n"
            f"I need both a pickup location and a destination.\n"
            f"Please also tell me your destination (or origin)."
        )

    origin      = locations[0]
    destination = locations[1]

    routes = load_routes()
    key     = f"{origin}|{destination}"
    key_rev = f"{destination}|{origin}"

    options = routes.get(key)
    if not options:
        options = routes.get(key_rev)
        if options:
            origin, destination = destination, origin

    if options:
        result = f"MULTI_ROUTE:{origin}:{destination}:"
        parts  = []
        for o in options:
            parts.append(
                f"{o['vehicle']}|{o['fare']}|{o['duration']}|{o['notes']}"
            )
        result += "||".join(parts)
        return result

    return (
        f"❌ Sorry, I don't have a route from {origin.title()} to {destination.title()} yet.\n\n"
        f"Please check the location names or try nearby areas.\n"
        f"Type \"list areas\" to see all supported locations."
    )
