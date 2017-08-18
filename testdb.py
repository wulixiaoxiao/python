import db
data = {
    'name' : 'aaa',
    'sex' : 'nan',
    'age' : 20
}

# results = db.db().select('user', "", [], 10)
# print(results)
# is_success = db.db().insert('user', data)
# is_success = db.db().update('user', 'id=1', data)
is_success = db.db().delete('user', 'id=2')


