# python
## 小白自封装的mysql操作类

引入：from db import db
查询：db.select(table, where(可为空), [](查询字段列表), 10(查询条数))
插入：db.insert('user', data(dict))
更新：db.update('user', 'id=1', data(dict))
删除：db.delete('user', 'id=2')
