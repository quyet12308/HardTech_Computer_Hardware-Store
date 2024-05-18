import sqlite3

# Kết nối với CSDL SQLite
conn = sqlite3.connect(
    "databases/ecommerce_database.db"
)  # Thay thế bằng đường dẫn thực tế đến tệp CSDL SQLite của bạn

cursor = conn.cursor()

try:
    cursor.execute("PRAGMA main.timezone")
    result = cursor.fetchone()

    if result is not None:
        print("Múi giờ hiện tại:", result[0])
    else:
        print("Không tìm thấy kết quả.")
except Exception as e:
    print("Lỗi:", str(e))

conn.close()
