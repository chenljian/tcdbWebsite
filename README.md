##中国计算机学会数据库专家委员会官网项目


### How to deploy
```
$ pip install pymongo
$ npm install
$ python makedocs.py
```

## Deploy Update!!!
下面把admin drop掉，然后重新插入带有管理员权限等级的数据
```
mongo
> use db
> db.admin.drop()
> db.admin.insert({name: "tcdbroot", password: "$2a$10$bHd5QiQ0OVIw2jdrLO5rHegn6VkO07p10GFBlFxBCQDPIzuZ.q5K.", role: 42});
```

```
$ node app
```

### Authentication
username: tcdbroot
password: d0ntte11y0u

### Pages
login: /admin/login/admin/posts
