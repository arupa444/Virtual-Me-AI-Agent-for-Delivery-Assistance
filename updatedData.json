{
  "students": [
    {
      "Name": "Arupa Nanda Swain",
      "roll_number": "UCSE21072",
      "room_number": "B-233",
      "degree": "Btech In Computer Science And Technology",
      "phoneNo": "+91XXXXXXXXXX",
      "whatsappNo": "+91XXXXXXXXXX",
      "emergency_contact": "+91XXXXXXXXXX"
    },
    {
      "Name": "Rahul Sharma",
      "roll_number": "UCSE21055",
      "room_number": "G-121",
      "degree": "Btech In Computer Science And Technology",
      "phoneNo": "+91XXXXXXXXXX",
      "whatsappNo": "+91XXXXXXXXXX",
      "emergency_contact": "+91XXXXXXXXXX"
    },
    {
      "Name": "Priya Das",
      "roll_number": "UCSE21081",
      "room_number": "B-310",
      "degree": "Btech In Computer Science And Technology",
      "phoneNo": "+91XXXXXXXXXX",
      "whatsappNo": "+91XXXXXXXXXX",
      "emergency_contact": "+91XXXXXXXXXX"
    }
  ],

  "location": {
    "address": "Nijigada, Kurki, Plot No:12(A, Harirajpur, Kakudia, Odisha 752050",
    "pin code": 752050,
    "landmarks": [
      "XIM University",
      "SBI ATM",
      "Union Bank ATM",
      "South Indian Bank",
      "Green Salad Hotel and Fast Foods",
      "Pani Puri Stall left to the road from the XIM Projection"
    ]
  },

  "availability": {
    "monday_to_saturday": {
      "class_hours": "9:00 AM - 5:00 PM",
      "break": "12:30 PM - 2:00 PM",
      "available_slots": [
        "6:00 AM - 8:30 AM",
        "12:30 PM - 2:00 PM",
        "5:00 PM - 9:40 PM"
      ]
    },
    "sunday": {
      "available_slots": [
        "6:00 AM - 9:00 PM"
      ]
    },
    "gate_closing_time": "10:00 PM"
  },

  "navigation_steps": {
    "step1": "Enter the campus through the main gate (left side from XIM projection).",
    "step2": "Walk straight for 70 meters until you reach a two-way split.",
    "step3": "Do NOT take the right (XIM chapel), instead take the LEFT towards UG Boys Hostel.",
    "step4": "On this path, you’ll notice the Main Campus Building on your right and the Amphitheater on your left.",
    "step5": "Continue straight for 50 meters until you reach a three-way road.",
    "step6": "You will see IC (International Center) on the left and Library on the right, but keep going STRAIGHT.",
    "step7": "After 50 meters, another three-way road will appear. Main Auditorium & Faculty Lounge will be on the left, PG Hostel on the right. Keep going STRAIGHT.",
    "step8": "At the end of this straight path, you’ll find another three-way split.",
    "step9": "On the left is the Doctor Dispensary, at 60° is the Vending Zone, but you must take the RIGHT (90°).",
    "step10": "Walk 40 meters. UG Boys Hostel will be on your LEFT.",
    "step11": "At the UG Boys Hostel reception, mention delivery for {Name} (Room {room_number}).",
    "step12": "Inside hostel, you will find 3 pathways: → RIGHT = Ground floor (rooms G-1 to G-44), → LEFT = G-100+ rooms, → STRAIGHT = B-block rooms (B-1 to B-544).",
    "step13": "For B-rooms, ground floor rooms are B-1 to B-44. If the room has 3 digits (e.g., B-233), the first digit indicates the floor (1xx = 1st floor, 2xx = 2nd floor, 3xx = 3rd floor).",
    "step14": "Use stairs or lift (10 meters inside B-block entrance).",
    "step15": "Find Room {room_number} in serial order and deliver the parcel."
  },

  "decision_tree": {
    "step1": "step2",
    "step2": "step3",
    "step3": "step4",
    "step4": "step5",
    "step5": "step6",
    "step6": "step7",
    "step7": "step8",
    "step8": "step9",
    "step9": "step10",
    "step10": "step11",
    "step11": "step12",
    "step12": "step13",
    "step13": "step14",
    "step14": "step15",
    "step15": "completed"
  },

  "fallbacks": {
    "cant_find": "Please search the location in Google Maps: {address}",
    "uncertain_location": "Can you find any landmark from {landmarks}?",
    "wrong_area": "Okay, you are somewhere else. Try searching Google Maps for: {address}",
    "landmarks_confirmed": "Okay, go to the main gate (left one from your projection), mention that you are here to deliver a package to one of the XIM students.",
    "security_details": "You can say his name is {Name}, he is pursuing his {degree} and the roll no is {roll_number}.",
    "security_destination": "Tell him I will visit UG Boys Hostel.",
    "room_locked_outside": "If the parcel is large, leave it in the corridor safely. If small, find nearby locker and search for {room_number} safe. If locked, try knocking nearest rooms. If nothing works, submit at reception and inform via WhatsApp {whatsappNo}.",
    "room_locked_inside": "Try knocking. If no response, knock nearest rooms and hand the parcel.",
    "rain_weather": "Take shelter under the UG parking or wait at the reception until rain stops. Delivery process remains the same afterwards."
  },

  "navigation_context": {
    "landmark_chapel": {
      "trigger_phrases": ["I can see a chapel", "There is a chapel", "I reached chapel"],
      "response": "You are on the wrong path. Please go back to the last two-way split and take the LEFT path towards UG Boys Hostel instead of the chapel.",
      "correction_step": "step3"
    },
    "landmark_main_building": {
      "trigger_phrases": ["I see the main building", "Main campus building is here"],
      "response": "Good, you are on the correct path. Keep moving straight.",
      "confirm_step": "step4"
    },
    "landmark_amphitheater": {
      "trigger_phrases": ["I see the amphitheater", "Amphitheater is here"],
      "response": "Perfect, you are on the right track. Keep walking straight.",
      "confirm_step": "step4"
    },
    "landmark_library": {
      "trigger_phrases": ["I see the library", "Library is here"],
      "response": "Good, you are on the correct path. Keep going straight.",
      "confirm_step": "step6"
    },
    "landmark_international_center": {
      "trigger_phrases": ["I see the IC", "International center is here"],
      "response": "Correct, you are close. Continue straight ahead.",
      "confirm_step": "step6"
    },
    "landmark_auditorium": {
      "trigger_phrases": ["I see the auditorium", "Main auditorium is here"],
      "response": "Perfect, you are very close. Keep going straight without turning.",
      "confirm_step": "step7"
    },
    "landmark_pg_hostel": {
      "trigger_phrases": ["I see PG hostel", "PG hostel is here"],
      "response": "You are near the right spot. Keep going straight until the next three-way split, then take the RIGHT (90°) to reach UG Boys Hostel.",
      "confirm_step": "step7"
    },
    "landmark_doctor_dispensary": {
      "trigger_phrases": ["I see the dispensary", "Doctor building is here"],
      "response": "You are at the last junction. Do NOT take left or 60°, instead take the RIGHT (90°) to reach UG Boys Hostel.",
      "confirm_step": "step9"
    },
    "landmark_vending_zone": {
      "trigger_phrases": ["I see vending zone", "Snacks corner is here"],
      "response": "You are very close. Ignore vending zone, take the RIGHT (90°). UG Boys Hostel is 40 meters ahead on your LEFT.",
      "confirm_step": "step9"
    },
    "landmark_ug_hostel": {
      "trigger_phrases": ["I reached UG hostel", "UG hostel is here"],
      "response": "Great, please go to reception and mention delivery for {Name} (Room {room_number}).",
      "confirm_step": "step10"
    },
    "lost": {
      "trigger_phrases": ["I am lost", "I can’t figure it out", "Nothing matches"],
      "response": "No worries. Please share your nearest landmark and I’ll guide you back on track."
    }
  },

  "query_system": {
    "search_by_name": "Match {Name} in students array and load their details.",
    "search_by_roll_number": "Match {roll_number} in students array and load their details.",
    "on_match": "Replace placeholders {Name}, {room_number}, {degree}, {roll_number}, {phoneNo}, {whatsappNo} in responses with matched student details.",
    "on_no_match": "Sorry, I can’t find this student in the database. Please re-check name/roll number."
  }
}
