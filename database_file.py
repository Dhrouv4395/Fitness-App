#database file
import harperdb

url = "https://cloud1-dhrouv.harperdbcloud.com"
username = "USERNAME"
password = "PASSWORD"

db = harperdb.HarperDB(url=url,username=username,password=password)

# print(db.describe_all())

SCHEMA = "workout_repo"
TABLE = "workout"
TABLE_TODAY = "today_workout"

# data = {"video_id":"123",
#         "title":"Test1",
#         "channel": "Test channel"}

# res = db.insert(SCHEMA, TABLE, [data])
# print(res)

def insert_workout(workout_data):
    return db.insert(SCHEMA, TABLE, [workout_data])

def delete_workout(workout_id):
    return db.delete(SCHEMA, TABLE, [workout_id])

def get_all_workouts():
    return db.sql(f"select * from {SCHEMA}.{TABLE}")

def get_workout_today():
    return db.sql(f"select * from {SCHEMA}.{TABLE_TODAY} where id = 0")

def update_workout_today(workout_data, insert=False):
    if insert:
        return db.insert(SCHEMA, TABLE, [workout_data])
    return db.update(SCHEMA, TABLE_TODAY, [workout_data])

#------------------------------------------------------------------
from yt_extractor import get_info

infos = get_info("")
print(infos)
insert_workout(infos)
workouts = get_all_workouts()
print(workouts)