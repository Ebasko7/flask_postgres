from flask import Flask, jsonify 
from model import students, db

app = Flask('server')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://ericbaskovich:@localhost:5432/school'

db.init_app(app)

@app.route('/students/')
def get_students():
    student_data = [stud.to_dict() for stud in students.query.all()]
    return jsonify(student_data)

app.run(debug= True, port=8000)