import mysql.connector

# 数据库连接参数
config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'test'
}

num_records = 1000000  # 要插入的数据记录数
batch_size = 10000  # 每次插入的批量大小

# 建立数据库连接
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # 设置自动提交为false，以便进行批量插入
    conn.autocommit = False

    # SQL语句
    sql = "INSERT INTO user (id, name) VALUES (%s, %s)"

    # 批量插入数据
    for i in range(1, num_records+1):
        data = (i, 'name_' + str(i))
        cursor.execute(sql, data)

        # 每达到批量大小时执行批量插入
        if i % batch_size == 0:
            conn.commit()
            print("Inserted", i, "records")

    # 执行最后一批剩余的数据
    conn.commit()
    print("Inserted", num_records, "records")

except mysql.connector.Error as e:
    print("Error: ", e)

finally:
    # 关闭数据库连接
    cursor.close()
    conn.close()