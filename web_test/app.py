from flask import Flask, Response

app = Flask(__name__)

# Dùng để kiểm tra HTTP headers
@app.route("/")
def home():
    return "Vulnerable Test Website"

# Giả lập WordPress 
@app.route("/wp-login.php")
def wp_login():
    return "WordPress Login Page"

# Cố tình lộ Server header 
@app.after_request
def add_server_header(response):
    response.headers["Server"] = "Apache/2.4.1" #Thêm thông tin Server giả lập Apache
    return response

# Mô phỏng đường dẫn nhạy cảm
@app.route("/admin")
def admin():
    return "Admin Panel"

@app.route("/login")
def login():
    return "Login Page"

# lỗi lộ thông tin qua robots.txt
@app.route("/robots.txt")
def robots():
    return (
        "User-agent: *\n"
        "Disallow: /admin\n"
        "Disallow: /login\n",
        200,
        {"Content-Type": "text/plain"}
    )

#File nhạy cảm có thể truy cập
@app.route("/phpinfo.php")
def phpinfo():
    return "phpinfo() page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)    #port 80 dùng để test port 
