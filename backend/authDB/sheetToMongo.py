import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pymongo import MongoClient
from pprint import pprint

# 1. 구글 시트 연결
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\User\\OneDrive\\Desktop\\GP\\backend\\google_creds.json", scope)
client = gspread.authorize(creds)

# 2. 시트 열기
spreadsheet = client.open("PRFS reservation")  # 구글 시트 이름
sheet = spreadsheet.worksheet("2025년 6월 3째주")  # 워크시트 이름

# 3. 시트에서 데이터 읽기 
values = sheet.get_all_values()
pprint(values)
records = []
# 예시: values[2]는 19:00~22:00 라인의 데이터
for row in values[2:]:
    time_slot = row[0]  # A열의 시간대
    for i, student in enumerate(row[1:], start=1):  # B~H열: 요일
        day = values[1][i]  # 두 번째 줄이 요일 헤더
        if student.strip():  # 예약자 정보가 있다면
            record = {f"{day}_{time_slot}": f"{student.strip()}"}
            records.append(record)

#스튜던트를 키로하고,
# 날짜를 어레이로 벨류로 받아. 
# 그 딕셔너리를 레코드로.하면 
# 그럼, 딕셔너리를 어디서 생성해야하는가...]
# 그롬 포문을 한 번 더 돌려야됨, 만약에 잇으면 거기에 추가하고

# 4. MongoDB 연결
mongo_client = MongoClient("mongodb://localhost:27017")
db = mongo_client["student_db"]
collection = db["reservation"]

# 5. MongoDB에 업데이트 or 삽입
for record in records: # 레코드리스트의 레코드들 포문돌림
    for day, student_id in record.items(): # 딕셔너리고 ,키는 날짜, 벨류는학번
        filter = {"student_id": student_id} #얘는 필터 UPDATE_ONE 할 때 필터임
        if collection.find_one({"student_id": student_id}): #레절베이션 컬렉션에서 학번이 있으면 
            record = {"day": day } # 레코드는 데이가 됨 
            update = {"$push": record} # {"$push": {"reservations": "2025-06-22 19:00"}
           
            print("if문")
        else:
            record = {"student_id": student_id,
                    "day": day }
            update = {"$set": record}
            print("else문")
        collection.update_one(filter, update, upsert=True)

print("✅ MongoDB 업데이트 완료")
"""
[
  {
    _id: ObjectId('6855420dd58799f603a68142'),
    student_id: 'C123000',
    day: '일_19:00-22:00'
  }
]

"""
"""
student_db> db.reservation.find().pretty()
[
  {
    _id: ObjectId('6855420dd58799f603a68142'),
    student_id: 'C123000',
    day: '일_19:00-22:00'
  }
]
student_db> db.reservation.find().pretty()
[
  {
    _id: ObjectId('6855420dd58799f603a68142'),
    student_id: 'C123000',
    day: '일_19:00-22:00'
  }
]
"""