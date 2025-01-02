from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = [{"id": 1, "name": "John Doe", "email": "john@example.com"}]

@app.route('/')
def index():
    return render_template('index.html')

# Dữ liệu mẫu
customers = []

# Lấy danh sách khách hàng
@app.route('/api/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

# Thêm khách hàng mới
@app.route('/api/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = {
        "id": len(customers) + 1,
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
    }
    customers.append(new_customer)
    return jsonify(new_customer), 201

if __name__ == '__main__':
    app.run(debug=True)
