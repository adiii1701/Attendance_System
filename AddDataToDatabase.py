import firebase_admin
from firebase_admin import credentials
from  firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "  " #create a live database link from firebase and paste it here
})

ref = db.reference('Students')

data = {
    "171621":
        {
            "name": "Tom Holland",
            "major": "Movies",
            "starting_year": 2020,
            "total_attendance" : 6,
            "standing": "G",
            "year": "5",
            "last_attendance_time" : "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emily Blunt",
            "major": "TV",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "B",
            "year": "2",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Robotics",
            "starting_year": 2020,
            "total_attendance": 2,
            "standing": "G",
            "year": "4",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "0104053":
        {
            "name": "Sreenidhi KLS",
            "major": "CSE AIML",
            "starting_year": 2022,
            "total_attendance": 2,
            "standing": "G",
            "year": "3",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "0104139":
        {
            "name": "Aditya Gadagandla",
            "major": "CSE AIML:",
            "starting_year": 2022,
            "total_attendance": 2,
            "standing": "G",
            "year": "3",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "0104096":
        {
            "name": "R Vishwanath",
            "major": "CSE AIML",
            "starting_year": 2022,
            "total_attendance": 2,
            "standing": "G",
            "year": "3",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
