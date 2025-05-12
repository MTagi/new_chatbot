from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/get_response', methods=['POST', 'GET']) # Chấp nhận cả POST và GET
def get_response():
    # Bạn có thể lấy dữ liệu từ request nếu cần, ví dụ:
    # user_query = ""
    # if request.method == 'POST':
    #     data = request.get_json()
    #     user_query = data.get('query', '')
    # elif request.method == 'GET':
    #     user_query = request.args.get('query', '')
    # print(f"Received query: {user_query}") # In ra console để xem

    response_data = {
        "response_text": "hello" # Luôn trả về "hello"
    }
    return jsonify(response_data)

if __name__ == '__main__':
    # Chạy server trên localhost, cổng 5000
    # Bạn có thể thay đổi host thành '0.0.0.0' để có thể truy cập từ thiết bị Android trong cùng mạng
    app.run(host='0.0.0.0', port=5000, debug=True)