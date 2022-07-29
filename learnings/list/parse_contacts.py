# Print only the email of the students
contacts = {
    "number":4,
    "students":
    [
        {"name":"Virat Kholi", "email":"virat@bcci.com"},
        {"name":"Sachin Tendulkar", "email":"sachin@bcci.com"},
        {"name":"Rahul Dravid", "email":"rahul@bcci.com"}
    ]
}

for i in contacts["students"]:
    print(i.get("email"))

for j in contacts["students"]:
    print(j['email'])