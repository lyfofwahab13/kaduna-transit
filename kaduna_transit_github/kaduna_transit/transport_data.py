# ============================================================
# Kaduna Public Transport Route Database — Multi-Vehicle
# Each route can have multiple vehicle options
# ============================================================

TRANSPORT_ROUTES = {
    # Format: (origin, destination): [ {vehicle, fare, duration, notes}, ... ]

    ("sabon tasha", "barnawa"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦200 – ₦300",
            "duration": "10–15 mins",
            "notes": "Board at Sabon Tasha junction. Alight at Barnawa roundabout. Faster but slightly pricier."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "15–25 mins",
            "notes": "Take a bus heading to Barnawa from Sabon Tasha motor park. Cheaper but takes longer."
        }
    ],
    ("sabon tasha", "kawo"): [
        {
            "vehicle": "Bus",
            "fare": "₦150 – ₦200",
            "duration": "20–30 mins",
            "notes": "Take a bus heading to Kawo from Sabon Tasha motor park."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦350 – ₦500",
            "duration": "15–25 mins",
            "notes": "Board keke at Sabon Tasha. Faster but more expensive for this longer route."
        }
    ],
    ("sabon tasha", "tudun wada"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦250",
            "duration": "10–20 mins",
            "notes": "Board at Sabon Tasha main road heading to Tudun Wada."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "15–25 mins",
            "notes": "Take a bus from Sabon Tasha motor park. Cheaper option."
        }
    ],
    ("sabon tasha", "kaduna central"): [
        {
            "vehicle": "Bus",
            "fare": "₦200 – ₦300",
            "duration": "25–35 mins",
            "notes": "Take a bus heading to central Kaduna from Sabon Tasha park."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦400 – ₦600",
            "duration": "20–30 mins",
            "notes": "Board keke at Sabon Tasha. Faster but expensive for long distance."
        }
    ],
    ("sabon tasha", "ungwan rimi"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦200 – ₦300",
            "duration": "15–25 mins",
            "notes": "Board keke at Sabon Tasha heading towards Ungwan Rimi."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "20–30 mins",
            "notes": "Take a bus from Sabon Tasha heading to Ungwan Rimi. Budget option."
        }
    ],

    ("barnawa", "sabon tasha"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦200 – ₦300",
            "duration": "10–15 mins",
            "notes": "Board at Barnawa roundabout heading to Sabon Tasha."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "15–25 mins",
            "notes": "Take a bus from Barnawa to Sabon Tasha. Cheaper option."
        }
    ],
    ("barnawa", "kaduna central"): [
        {
            "vehicle": "Bus",
            "fare": "₦200 – ₦250",
            "duration": "20–30 mins",
            "notes": "Take a bus from Barnawa market heading to central Kaduna."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦350 – ₦500",
            "duration": "15–25 mins",
            "notes": "Board keke at Barnawa for a faster ride to Kaduna Central."
        }
    ],
    ("barnawa", "kawo"): [
        {
            "vehicle": "Bus",
            "fare": "₦200 – ₦300",
            "duration": "30–40 mins",
            "notes": "Take a bus via Kaduna central to Kawo."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦500 – ₦700",
            "duration": "25–35 mins",
            "notes": "Board keke at Barnawa. Faster but more expensive for this long route."
        }
    ],
    ("barnawa", "ungwan rimi"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦200",
            "duration": "10–15 mins",
            "notes": "Board keke at Barnawa roundabout heading to Ungwan Rimi."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦120",
            "duration": "15–20 mins",
            "notes": "Short bus ride from Barnawa to Ungwan Rimi. Budget option."
        }
    ],
    ("barnawa", "television"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦200 – ₦300",
            "duration": "15–20 mins",
            "notes": "Board keke at Barnawa heading towards Television area."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "20–25 mins",
            "notes": "Take a bus from Barnawa to Television area."
        }
    ],

    ("kawo", "sabon tasha"): [
        {
            "vehicle": "Bus",
            "fare": "₦150 – ₦200",
            "duration": "20–30 mins",
            "notes": "Take a bus from Kawo motor park towards Sabon Tasha."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦350 – ₦500",
            "duration": "15–25 mins",
            "notes": "Board keke at Kawo for a faster ride to Sabon Tasha."
        }
    ],
    ("kawo", "barnawa"): [
        {
            "vehicle": "Bus",
            "fare": "₦200 – ₦300",
            "duration": "30–40 mins",
            "notes": "Take a bus from Kawo heading south towards Barnawa."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦500 – ₦700",
            "duration": "25–35 mins",
            "notes": "Board keke at Kawo. Faster but expensive for this long route."
        }
    ],
    ("kawo", "ungwan rimi"): [
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "10–20 mins",
            "notes": "Short bus ride from Kawo to Ungwan Rimi."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦250",
            "duration": "8–15 mins",
            "notes": "Board keke at Kawo for a quicker ride to Ungwan Rimi."
        }
    ],
    ("kawo", "tudun wada"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦200",
            "duration": "15–20 mins",
            "notes": "Board keke from Kawo towards Tudun Wada."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "20–25 mins",
            "notes": "Take a bus from Kawo to Tudun Wada. Cheaper option."
        }
    ],
    ("kawo", "kaduna central"): [
        {
            "vehicle": "Bus",
            "fare": "₦150 – ₦200",
            "duration": "15–25 mins",
            "notes": "Regular buses run from Kawo to central Kaduna."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦250 – ₦400",
            "duration": "12–20 mins",
            "notes": "Board keke at Kawo for a faster ride to Kaduna Central."
        }
    ],
    ("kawo", "kaduna north"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦100 – ₦150",
            "duration": "10–15 mins",
            "notes": "Short keke ride from Kawo to Kaduna North."
        },
        {
            "vehicle": "Bus",
            "fare": "₦80 – ₦100",
            "duration": "12–18 mins",
            "notes": "Take a bus from Kawo to Kaduna North. Budget option."
        }
    ],

    ("kaduna central", "barnawa"): [
        {
            "vehicle": "Bus",
            "fare": "₦200 – ₦250",
            "duration": "20–30 mins",
            "notes": "Board a bus from central Kaduna heading to Barnawa."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦350 – ₦500",
            "duration": "15–25 mins",
            "notes": "Board keke at Kaduna Central for a faster ride to Barnawa."
        }
    ],
    ("kaduna central", "sabon tasha"): [
        {
            "vehicle": "Bus",
            "fare": "₦200 – ₦300",
            "duration": "25–35 mins",
            "notes": "Take a bus heading south to Sabon Tasha."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦400 – ₦600",
            "duration": "20–30 mins",
            "notes": "Board keke at Kaduna Central. Faster but pricier."
        }
    ],
    ("kaduna central", "kawo"): [
        {
            "vehicle": "Bus",
            "fare": "₦150 – ₦200",
            "duration": "15–25 mins",
            "notes": "Regular buses run from central Kaduna to Kawo."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦250 – ₦400",
            "duration": "12–20 mins",
            "notes": "Board keke for a faster ride to Kawo."
        }
    ],
    ("kaduna central", "malali"): [
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦200",
            "duration": "10–20 mins",
            "notes": "Take a bus from the city centre heading to Malali."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦200 – ₦300",
            "duration": "8–15 mins",
            "notes": "Board keke at Kaduna Central for a quicker trip to Malali."
        }
    ],
    ("kaduna central", "ungwan rimi"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦100 – ₦200",
            "duration": "10–15 mins",
            "notes": "Short keke ride within central Kaduna area."
        },
        {
            "vehicle": "Bus",
            "fare": "₦80 – ₦120",
            "duration": "12–18 mins",
            "notes": "Take a bus from Kaduna Central to Ungwan Rimi. Budget option."
        }
    ],
    ("kaduna central", "narayi"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦250",
            "duration": "15–20 mins",
            "notes": "Board keke from central Kaduna towards Narayi."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "18–25 mins",
            "notes": "Take a bus from Kaduna Central to Narayi. Cheaper option."
        }
    ],

    ("ungwan rimi", "barnawa"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦200",
            "duration": "10–15 mins",
            "notes": "Board keke at Ungwan Rimi heading to Barnawa."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦120",
            "duration": "15–20 mins",
            "notes": "Take a bus from Ungwan Rimi to Barnawa. Budget option."
        }
    ],
    ("ungwan rimi", "kawo"): [
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "10–20 mins",
            "notes": "Short bus ride from Ungwan Rimi to Kawo."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦250",
            "duration": "8–15 mins",
            "notes": "Board keke at Ungwan Rimi for a quicker trip to Kawo."
        }
    ],
    ("ungwan rimi", "kaduna central"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦100 – ₦200",
            "duration": "10–15 mins",
            "notes": "Board keke heading to central Kaduna."
        },
        {
            "vehicle": "Bus",
            "fare": "₦80 – ₦120",
            "duration": "12–18 mins",
            "notes": "Take a bus from Ungwan Rimi to Kaduna Central."
        }
    ],
    ("ungwan rimi", "sabon tasha"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦200 – ₦300",
            "duration": "15–25 mins",
            "notes": "Board keke heading south to Sabon Tasha."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "20–30 mins",
            "notes": "Take a bus from Ungwan Rimi to Sabon Tasha. Budget option."
        }
    ],

    ("tudun wada", "sabon tasha"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦250",
            "duration": "10–20 mins",
            "notes": "Board keke from Tudun Wada heading to Sabon Tasha."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "15–25 mins",
            "notes": "Take a bus from Tudun Wada to Sabon Tasha. Cheaper option."
        }
    ],
    ("tudun wada", "kawo"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦200",
            "duration": "15–20 mins",
            "notes": "Board keke from Tudun Wada heading north to Kawo."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "20–25 mins",
            "notes": "Take a bus from Tudun Wada to Kawo. Budget option."
        }
    ],
    ("tudun wada", "kaduna central"): [
        {
            "vehicle": "Bus",
            "fare": "₦150 – ₦200",
            "duration": "15–25 mins",
            "notes": "Take a bus from Tudun Wada to central Kaduna."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦250 – ₦350",
            "duration": "12–20 mins",
            "notes": "Board keke at Tudun Wada for a faster trip to Kaduna Central."
        }
    ],
    ("tudun wada", "barnawa"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦200 – ₦300",
            "duration": "20–30 mins",
            "notes": "Board keke from Tudun Wada heading to Barnawa."
        },
        {
            "vehicle": "Bus",
            "fare": "₦150 – ₦200",
            "duration": "25–35 mins",
            "notes": "Take a bus from Tudun Wada to Barnawa. Cheaper option."
        }
    ],

    ("malali", "kaduna central"): [
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦200",
            "duration": "10–20 mins",
            "notes": "Take a bus from Malali to Kaduna central."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦200 – ₦300",
            "duration": "8–15 mins",
            "notes": "Board keke at Malali for a faster ride to Kaduna Central."
        }
    ],
    ("malali", "kawo"): [
        {
            "vehicle": "Bus",
            "fare": "₦150 – ₦250",
            "duration": "15–25 mins",
            "notes": "Board bus from Malali heading to Kawo."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦250 – ₦350",
            "duration": "12–20 mins",
            "notes": "Board keke at Malali for a quicker trip to Kawo."
        }
    ],
    ("malali", "ungwan rimi"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦200",
            "duration": "10–15 mins",
            "notes": "Short keke ride from Malali to Ungwan Rimi."
        },
        {
            "vehicle": "Bus",
            "fare": "₦80 – ₦120",
            "duration": "12–18 mins",
            "notes": "Take a bus from Malali to Ungwan Rimi. Budget option."
        }
    ],

    ("narayi", "kaduna central"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦250",
            "duration": "15–20 mins",
            "notes": "Board keke from Narayi heading to central Kaduna."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "18–25 mins",
            "notes": "Take a bus from Narayi to Kaduna Central. Cheaper option."
        }
    ],
    ("narayi", "barnawa"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦150 – ₦200",
            "duration": "10–15 mins",
            "notes": "Board keke from Narayi heading to Barnawa."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦120",
            "duration": "12–18 mins",
            "notes": "Take a bus from Narayi to Barnawa. Budget option."
        }
    ],
    ("narayi", "television"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦100 – ₦150",
            "duration": "5–10 mins",
            "notes": "Short keke ride from Narayi to Television area."
        },
        {
            "vehicle": "Bus",
            "fare": "₦80 – ₦100",
            "duration": "8–12 mins",
            "notes": "Take a bus from Narayi to Television. Budget option."
        }
    ],

    ("television", "barnawa"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦200 – ₦300",
            "duration": "15–20 mins",
            "notes": "Board keke at Television area heading to Barnawa."
        },
        {
            "vehicle": "Bus",
            "fare": "₦100 – ₦150",
            "duration": "20–25 mins",
            "notes": "Take a bus from Television to Barnawa. Budget option."
        }
    ],
    ("television", "narayi"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦100 – ₦150",
            "duration": "5–10 mins",
            "notes": "Short keke ride from Television to Narayi."
        },
        {
            "vehicle": "Bus",
            "fare": "₦80 – ₦100",
            "duration": "8–12 mins",
            "notes": "Take a bus from Television to Narayi. Budget option."
        }
    ],
    ("television", "kaduna central"): [
        {
            "vehicle": "Bus",
            "fare": "₦150 – ₦250",
            "duration": "20–30 mins",
            "notes": "Take a bus from Television area to central Kaduna."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦300 – ₦450",
            "duration": "15–25 mins",
            "notes": "Board keke at Television for a faster ride to Kaduna Central."
        }
    ],

    ("kaduna north", "kawo"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦100 – ₦150",
            "duration": "10–15 mins",
            "notes": "Board keke at Kaduna North heading to Kawo."
        },
        {
            "vehicle": "Bus",
            "fare": "₦80 – ₦100",
            "duration": "12–18 mins",
            "notes": "Take a bus from Kaduna North to Kawo. Budget option."
        }
    ],
    ("kaduna north", "kaduna central"): [
        {
            "vehicle": "Bus",
            "fare": "₦150 – ₦200",
            "duration": "15–25 mins",
            "notes": "Take a bus from Kaduna North to central Kaduna."
        },
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦250 – ₦350",
            "duration": "12–20 mins",
            "notes": "Board keke at Kaduna North for a faster ride to Kaduna Central."
        }
    ],
    ("kaduna north", "malali"): [
        {
            "vehicle": "Keke (Tricycle)",
            "fare": "₦100 – ₦200",
            "duration": "10–15 mins",
            "notes": "Short keke ride from Kaduna North to Malali."
        },
        {
            "vehicle": "Bus",
            "fare": "₦80 – ₦120",
            "duration": "12–18 mins",
            "notes": "Take a bus from Kaduna North to Malali. Budget option."
        }
    ],
}

# ── Merge Ahmadu Bello Way routes ──────────────────────────
from ahmadu_bello_data import AHMADU_BELLO_ROUTES, AHMADU_BELLO_LOCATIONS

TRANSPORT_ROUTES.update(AHMADU_BELLO_ROUTES)

ALL_LOCATIONS = list(set(
    [k[0] for k in TRANSPORT_ROUTES] +
    [k[1] for k in TRANSPORT_ROUTES]
))
