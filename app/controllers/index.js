const assert = require('assert');
const Post = require("../models/post");

var compareArticleDate = function (p1, p2) {
    return parseInt(p2.date) - parseInt(p1.date);
};

exports.commintro = function (req, res) {
    res.render('commintro/index', {
        title: "专委会介绍"
    });
};

exports.honormember = function (req, res) {
    res.render('commintro/honormember', {
        title: "荣誉委员"
    });
};

exports.contact = function (req, res) {
    res.render('contact/contact', {
        title: "联系方式"
    });
};

exports.resources = function (req, res) {
    res.render('resources/opensource', {
        title: "相关资源"
    });
};

exports.opensource = function (req, res) {
    res.render('resources/opensource', {
        title: "开源软件"
    });
};

exports.documents = function (req, res) {
    res.render('resources/documents', {
        title: "相关文档材料"
    });
};

exports.special = function (req, res) {
    res.render('special/dseintro', {
        title: "特别栏目"
    });
};

exports.dseintro = function (req, res) {
    res.render('special/dseintro', {
        title: "DSE期刊"
    });
};
exports.dseeditors = function (req, res) {
    res.render('special/dseeditors', {
        title: "DSE期刊"
    });
};
exports.dsecallforpaper = function (req, res) {
    res.render('special/dsecallforpaper', {
        title: ""
    });
};
exports.dsepaperlist = function (req, res) {
    res.render('special/dsepaperlist', {
        title: "DSE期刊"
    });
};

exports.vldbsummerschool = function (req, res) {
    res.render('special/vldbsummerschool2016', {
        title: "暑期学校"
    })
};
exports.vldbsummerschool2016 = function (req, res) {
    res.render('special/vldbsummerschool2016', {
        title: "暑期学校"
    })
};
exports.vldbsummerschool2015 = function (req, res) {
    res.render('special/vldbsummerschool2015', {
        title: "暑期学校"
    })
};
exports.vldbsummerschool2014 = function (req, res) {
    res.render('special/vldbsummerschool2014', {
        title: "暑期学校"
    })
};
exports.vldbsummerschool2013 = function (req, res) {
    res.render('special/vldbsummerschool2013', {
        title: "暑期学校"
    })
};

exports.conferences = function (req, res) {
    res.render('conferences', {
        title: '会议归档'
    })
};

exports.dev = function (req, res) {
    res.render('dev', {
        title: 'WAIM-APWeb2017-dev'
    })
};

exports.index = function (req, res) {
    Post.find().select("category date title_en title_cn special_recomm").exec(function (err, docs) {
        assert.equal(err, null);
        res.render('index', {
            title: "中国计算机学会数据库专业委员会",
			//提供四种文章
            special_posts: docs.filter(function (doc) {
                return doc.special_recomm == true;
            }).sort(compareArticleDate).slice(0, 8),
            newsdynamics_posts: docs.filter(function (doc) {
                return doc.category == 'newsdynamics';
            }).sort(compareArticleDate).slice(0, 4),
            commdynamics_posts: docs.filter(function (doc) {
                return doc.category == 'commdynamics';
            }).sort(compareArticleDate).slice(0, 5),
            confinfo_posts: docs.filter(function (doc) {
                return doc.category == 'confinfo';
            }).sort(compareArticleDate).slice(0, 4)
        });
    });
};

exports.newsdynamics = function (req, res) {
    Post.find({'category': 'newsdynamics'}).select("date title_en title_cn special_recomm").exec(function (err, docs) {
        assert.equal(err, null);
        res.render('newsdynamics/newsdynamics', {
            title: "新闻动态",
            posts: docs.sort(function (p1, p2) {
                return parseInt(p2.date) - parseInt(p1.date);
            })
        });
    });
};

exports.commdynamics = function (req, res) {
    Post.find({'category': 'commdynamics'}).select("date title_en title_cn special_recomm").exec(function (err, docs) {
        assert.equal(err, null);
        res.render('commdynamics/commdynamics', {
            title: "委员动态",
            posts: docs.sort(compareArticleDate)
        });
    });
};

exports.confinfo = function (req, res) {
    Post.find({'category': 'confinfo'}).select("date title_en title_cn special_recomm").exec(function (err, docs) {
        assert.equal(err, null);
        res.render('confinfo/confinfo', {
            title: "会议信息",
            posts: docs.sort(compareArticleDate)
        });
    });
};