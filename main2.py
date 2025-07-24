1
@app.get("/hello", response_class=PlainTextResponse)
def hello():
return "Hello world"

2
@app.get("/Welcome",  response_class=PlainTextResponse)
def welcome(name: str):
  return "Welcome {name}"

3
@app.post("/students", status_code=201)
def add_students(new_students: List[Student]):
    students_db.extend(new_students)
    return students_db

4
@app.get("/students")
def get_students():
    return students_db

5
@app.put("/students")
def upsert_student(student: Students):
    for i,s in enumerate(students_db):
        if s.refere