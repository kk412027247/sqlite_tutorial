import sqlite3

conn = sqlite3.connect('./test.db')

# 或者直接在内存里建立
# conn = sqlite3.connect(":memory:")

cu = conn.cursor()

# 创建一张user表，标准哦功能有id（主键），名字（唯一），年龄，备注（预设为空）
# cu.execute("create table user (id integer primary key, name varchar(20) UNIQUE, age integer, comment text NULL)")


# 插入语句，用元祖插入
# for user in[(2, 'ccc', 111, 'cccc'),(3, 'ddd',222,'dddd')]:
#     conn.execute("insert into user values (?,?,?,?)", user)
# conn.commit()

# 查询资料
cu.execute('select * from user')
print(cu.fetchone())

# 修改
cu.execute('update user set name="fff1" where id = 0')
conn.commit()

cu.execute('select * from user')
print(cu.fetchall())

# 删除
cu.execute('delete from user where id = 1')
conn.commit()

cu.execute('select * from user')
print(cu.fetchall())


# https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/365040/
