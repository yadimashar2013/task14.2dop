import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')
cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
for i in range(1, 11):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
               (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))

# cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
#                (500, 'User1'))
# cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
#                (500, 'User3'))
# cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
#                (500, 'User5'))
# cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
#                (500, 'User7'))
# cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
#                (500, 'User9'))
# cursor.execute('DELETE FROM Users WHERE username = ?', ('User1',))
# cursor.execute('DELETE FROM Users WHERE username = ?', ('User4',))
# cursor.execute('DELETE FROM Users WHERE username = ?', ('User7',))
# cursor.execute('DELETE FROM Users WHERE username = ?', ('User10',))
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
# users = cursor.fetchall()
# for user in users:
#     print(user)
cursor.execute('SELECT SUM(balance) FROM Users')
users = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM Users')
users1 = cursor.fetchone()[0]
print(users / users1)


connection.commit()
connection.close()