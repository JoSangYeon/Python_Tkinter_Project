import sqlite3

"""sqlite 버젼 확인"""
print(sqlite3.version)
print(sqlite3.sqlite_version)

"""db파일 생성"""
conn = sqlite3.connect("test.db", isolation_level=None)

"""커서 선언"""
c = conn.cursor()

"""테이블 생성"""
cmd = """CREATE TABLE IF NOT EXISTS table1
(id integer PRIMARY KEY, name text, birthday text)"""
c.execute(cmd)

"""실습전 이전 데이터 삭제"""
conn.execute("DELETE FROM table1")

"""데이터 삽입"""
# 데이터 삽입 방법 1
c.execute("INSERT INTO table1 VALUES(1, 'CHO', '1998-12-19')")

# 데이터 삽입 방법 2
c.execute("INSERT INTO table1(id, name, birthday) VALUES(?,?,?)", (2, "KIM", "1999-00-00"))

# 데이터 삽입 방법 3
test_tuple = (
    (3, 'PARK', '1991-99-12'),
    (4, 'CHOI', '1992-12-12'),
    (5, 'JUNG', '1993-13-13'),
    )
c.executemany("INSERT INTO table1(id, name, birthday) VALUES(?,?,?)", test_tuple)

"""데이터 불러오기"""
# 커서.fetchone(): 하나씩 출력(커서가 첫번째 데이터부터 한줄씩 읽어옴)
c.execute("SELECT * FROM table1")
print(c.fetchone())
print(c.fetchone())
print(c.fetchone())
print(type(c.fetchone())) #tuple타입으로 반환함

# 커서.fetchall(): 전체 데이터를 반환(리스트 형태)
c.execute("SELECT * FROM table1")
data = c.fetchall()
print(type(data)) # list 타입으로 반환됨
# 방법 1
for row in data:
    print(row)

# 방법 2
for row in c.execute("SELECT * FROM table1 ORDER BY id ASC"):
    print(row)

"""데이터 조회하기기"""
# 방법 1
param1 = (1,)
c.execute("SELECT * FROM table1 WHERE id=?", param1)
print('param1:', c.fetchone())
print('param1:', c.fetchall())

# 방법 2
param2 = 1
c.execute("SELECT * FROM table1 WHERE id='%s'" % param2)  # %s %d %f
print('param2', c.fetchone())
print('param2', c.fetchall())

# 방법 3
c.execute("SELECT * FROM table1 WHERE id=:Id", {"Id": 1})
print('param3', c.fetchone())
print('param3', c.fetchall())

# 방법 4
param4 = (1, 4)
c.execute('SELECT * FROM table1 WHERE id IN(?,?)', param4)
print('param4', c.fetchall())

# 방법 5
c.execute("SELECT * FROM table1 WHERE id In('%d','%d')" % (1, 4))
print('param5', c.fetchall())

# 방법 6
c.execute("SELECT * FROM table1 WHERE id=:id1 OR id=:id2", {"id1": 1, "id2": 4})
print('param6', c.fetchall())

"""데이터 수정하기"""
# 방법 1
c.execute("UPDATE table1 SET name=? WHERE id=?", ('NEW1', 1))
# 방법 2
c.execute("UPDATE table1 SET name=:name WHERE id=:id", {"name": 'NEW2', 'id': 3})
# 방법 3
c.execute("UPDATE table1 SET name='%s' WHERE id='%s'" % ('NEW3', 5))
# 확인
for row in c.execute('SELECT * FROM table1'):
    print(row)


"""데이터 삭제하기"""
# 방법 1
c.execute("DELETE FROM table1 WHERE id=?", (1,))
# 방법 2
c.execute("DELETE FROM table1 WHERE id=:id", {'id': 3})
# 방법 3
c.execute("DELETE FROM table1 WHERE id='%s'" % 5)
# 확인
for row in c.execute('SELECT * FROM table1'):
    print(row)