

# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-76b00-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Priyanshu ",
            "major": "CS",
            "starting_year": 2020,
            "total_attendance": 5,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "3073":
        {
            "name": "Mohit Singh",
            "major": "CS",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Nitish Kalyan",
            "major": "CS",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "3096":
        {
            "name": "Virat Kohli",
            "major": "Cricket",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 10,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "3100":
        {
            "name": "Nitish ",
            "major": "IT",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)