const assert = require('assert');
const Post = require("../models/post");
const url = require('url');
const querystring = require('querystring');
const _ = require('underscore');

exports.GETpost = function (req, res) {
    var params = req.url.split('-');
    var filter = {'date': params[1], 'title_en': params[2]};
    Post.findOne(filter, function (err, post) {
        assert.equal(err, null);
        res.render('post', {
            post: post
        });
    });
};

exports.search = function (req, res) {
    var _query = url.parse(req.url).query;
    var _content = querystring.parse(_query).content;
    var filter = {content: {"$regex": _content, "$options": "i"}};
    Post.find(filter, function (err, posts) {
        assert.equal(err, null);
        // res.setHeader('Content-Type', 'application/json');
        // res.send(JSON.stringify(post));
        // console.log(posts);
        res.render('search', {
            results: posts
        });
    });
};

exports.list = function (req, res) {
    Post.find({}, function (err, docs) {
        res.render('admin/postlist', {
            currentAdmin: req.session.admin.name,
            userRole: req.session.admin.role,
            newsdynamics_posts: docs.filter(function (doc) {
                return doc.category == 'newsdynamics';
            }).sort(function (p1, p2) {
                return parseInt(p2.date) - parseInt(p1.date);
            }),
            commdynamics_posts: docs.filter(function (doc) {
                return doc.category == 'commdynamics';
            }).sort(function (p1, p2) {
                return parseInt(p2.date) - parseInt(p1.date);
            }),
            confinfo_posts: docs.filter(function (doc) {
                return doc.category == 'confinfo';
            }).sort(function (p1, p2) {
                return parseInt(p2.date) - parseInt(p1.date);
            })
        });
    })
};

exports.GETadd = function (req, res) {
    res.render('admin/addpost', {
        currentAdmin: req.session.admin.name,
        post: ""
    });
};

exports.update = function (req, res) {
    var _query = url.parse(req.url).query;
    var _title_en = querystring.parse(_query).title_en;
    var _date = querystring.parse(_query).date;
    var filter = {'date': _date, 'title_en': _title_en};
    Post.findOne(filter, function (err, post) {
        res.render('admin/addpost', {
            post: post
        });
    });
};

exports.POSTadd = function (req, res) {
    var title_en = req.body.title_en;
    var date = req.body.date;
    if (title_en == "" || !title_en) {
        // 如果没有title_en,则为新的文章。
        Post.findLast({date: date}, function (err, post) {
            var num;
            if (post[0]) {
                num = post[0].title_en.slice(1);
            }
            else {
                num = 1;
            }
            _title = "p" + num;
            _source = req.body.source;
            if (_source == "") {
                _source = '计算机学会数据库专委会'
            }
            _post = new Post({
                title_cn: req.body.title_cn,
                category: req.body.category,
                content: req.body.content,
                date: req.body.date,
                title_en: _title,
                source: _source
            });
            _post.save(function (err, post) {
                assert.equal(err, null);
                res.json({success: 1});
            });
        });
    } else {
        // 此处为修改文章的post代码
        var olddate = req.body.olddate; // 存储旧时间用于修改。
        var filter = {title_en: title_en, date: olddate};
        Post.findOne(filter, function (err, postOld) {
            assert.equal(err, null);
            Post.findLast({date: date}, function (err, post) {
                var PostObj = req.body;
                var _post = _.extend(postOld, PostObj);
                _post.save(function (err, post) {
                    assert.equal(err, null);
                    res.json({success: 1});
                })
            });
        });
    }
};

exports.delete = function (req, res) {
    var _query = url.parse(req.url).query;
    var _title_en = querystring.parse(_query).title_en;
    var _date = querystring.parse(_query).date;
    Post.remove({title_en: _title_en, date: _date}, function (err, post) {
        assert.equal(err, null);
        res.json({success: 1});
    });
};