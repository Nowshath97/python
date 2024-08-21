from flask import Flask, jsonify,request
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


students = {
    1: {"name": "Alice Johnson", "age": 20, "major": "Computer Science"},
    2: {"name": "Bob Smith", "age": 22, "major": "Mathematics"},
    3: {"name": "Charlie Brown", "age": 19, "major": "Physics"}
}

@app.route('/api/student',methods=['GET'])
def get_student():
    student_id=request.args.get('id',type=int)
    if student_id in students:
        return jsonify({
            'student_id':student_id,
            'details':students[student_id],
            'status':'success'
        })
    else:
        return jsonify({
            'message':'Student not found',
            'status':'error'
        }),
if __name__ == '__main__':
    app.run(debug=True)
