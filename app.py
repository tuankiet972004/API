from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = [{"id": 1, "name": "John Doe", "email": "john@example.com"}]

@app.route('/')
def index():
    return render_template('index.html')


# Dữ liệu câu hỏi mẫu
qa_data = [
    {
        "question": "What is Flask?",
    },
    {
        "question": "How to add a new user?",
    },
    {
        "question": "Who is HauLee?",
    }
]

# Lấy danh sách câu hỏi và câu trả lời
@app.route('/api/questions', methods=['GET'])
def get_questions():
    return jsonify(qa_data)
#hiển thị câu hỏi
def get_questions():
    return jsonify(qa_data)


# Thêm câu hỏi mới
@app.route('/api/questions', methods=['POST'])
def add_question():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"message": "Please provide a question."}), 400

    new_question = {
        "question": question,
        "answer": ""  # Không cần câu trả lời khi thêm câu hỏi
    }
    qa_data.append(new_question)
    return jsonify(new_question), 201


# Trang thêm câu hỏi
@app.route('/add-question')
def add_question_page():
    return render_template('add_question.html')

#Trang trả lời câu hỏi
@app.route('/add-answer')
def ask_question_page():
    return render_template('add_answer.html')

#hiển thị câu hỏi
def get_questions():
    return jsonify(qa_data)


# Trả lời câu hỏi
@app.route('/api/answer', methods=['POST'])
def answer_question():
    data = request.get_json()
    question = data.get('question')
    answer = data.get('answer')

    if not question or not answer:
        return jsonify({"message": "Please provide both question and answer."}), 400

    # Tìm câu hỏi và lưu câu trả lời vào dữ liệu
    for qa in qa_data:
        if qa['question'].lower() == question.lower():
            qa['answer'] = answer
            # Tìm câu hỏi tiếp theo
            next_question_index = qa_data.index(qa) + 1
            if next_question_index < len(qa_data):
                next_question = qa_data[next_question_index]['question']
                return jsonify({"message": "Answer has been saved!", "next_question": next_question}), 200
            else:
                return jsonify({"message": "You've answered all the questions!"}), 200

    return jsonify({"message": "Question not found."}), 404


if __name__ == '__main__':
    app.run(debug=True)
