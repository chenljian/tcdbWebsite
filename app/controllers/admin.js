const Admin = require('../models/admin');
const assert = require('assert');
const fs = require('fs-extra');
var bcryptjs = require('bcryptjs');
const unzip = require('unzip');
const logger = require('../../log');
var SALT_FACTOR = 10;

exports.index = function (req, res) {
    var admin = req.session.admin;

    // 除非只有网页上传权限，默认显示后台文章列表
    if (admin.role == 12) {
        res.redirect('/admin/upload');
    } else {
        res.redirect('/admin/posts');
    }
};

exports.login = function (req, res) {
    delete req.session.hint;
    res.render('admin/login');
};

exports.signup = function (req, res) {
    delete req.session.hint;
    res.render('admin/signup', {
        currentAdmin: req.session.admin.name
    });
};

exports.POSTlogin = function (req, res) {
    var _admin = req.body;
    var name = _admin.username;
    var password = _admin.password;

    Admin.findOne({name: name}, function (err, admin) {
        assert.equal(err, null);
        if (admin == null) {
            req.session.hint = "登录失败";
            return res.redirect('/admin/login');
        }

        var role = admin.role;

        admin.comparePassword(password, function (err, isMatch) {
            assert.equal(err, null);
            if (isMatch) {//用户登录成功
                logger.info("login success" + name);
                req.session.admin = {};
                req.session.admin.name = name;
                req.session.admin.password = password;
                req.session.admin.role = role;
                res.redirect('/admin');
            } else {
                logger.info("login failed" + name);
                req.session.hint = "登录失败";
                return res.redirect('/admin/login');
            }
        });
    });
};

exports.POSTsignup = function (req, res) {
    var _admin = req.body;
    var name = _admin.username;
    var password1 = _admin.password1;
    var password2 = _admin.password2;
    var isEditor = _admin.isEditor;
    var isUploader = _admin.isUploader;

    var userRole;

    if (isEditor) {
        if (isUploader) {
            userRole = 13;  // 同时是Editor和Uploader
        } else {
            userRole = 7;   // 只是Edtior
        }
    } else {
        if (isUploader) {
            userRole = 12;  // 只是Uploader
        } else {
            req.session.hint = '请选择至少一个用户权限';
            return res.redirect('/admin/signup');
        }
    }

    if (name == '') {
        req.session.hint = '用户名不能为空';
        return res.redirect('/admin/signup');   // 这里的return很重要
    }

    if (password1 == '') {
        req.session.hint = '密码不能为空';
        return res.redirect('/admin/signup');
    }

    if (password1 != password2) {
        req.session.hint = '密码不一致';
        return res.redirect('/admin/signup');   // 这里的return很重要
    }

    var password = password1;

    Admin.findOne({name: name}, function (err, admin) {
        assert.equal(err, null);
        if (admin != null) {
            req.session.hint = '用户名已被注册';
            return res.redirect('/admin/signup');   // 这里的return很重要
        } else {
            var _admin = new Admin({
                name: name,
                password: password,
                role: userRole
            });
            _admin.save(function (err, admin) {
                logger.info("signup success" + name + "by " + _admin.name);
                assert.equal(err, null);
                req.session.hint = '注册成功，请登录';
                res.redirect('/admin/login');
            });
        }
    });
};

exports.logout = function (req, res) {
    logger.info("logout" + req.session.admin.name);
    delete req.session.admin;
    delete req.session.hint;
    // res.json({msg: "登出"});
    res.redirect('/admin/login');
};

exports.modifyPassword = function (req, res) {
    delete req.session.hint;
    res.render('admin/modifypassword', {
        currentAdmin: req.session.admin.name
    });
};

exports.POSTmodifyPassword = function (req, res, next) {
    var modifyInfo = req.body;
    var password1 = modifyInfo.password1;
    var password2 = modifyInfo.password2;

    var admin = req.session.admin;
    var name = admin.name;

    if (password1 == '') {
        req.session.hint = '密码不能为空';
        return res.redirect('/admin/modifypassword');
    }

    if (password1 != password2) {
        req.session.hint = '两次输入的新密码不一致';
        return res.redirect('/admin/modifypassword');
    }

    var newPassword = password1;
    // 将新密码更新到Mongo数据库中去
    // 删除当前session信息
    // 重定向到登录页面

    bcryptjs.genSalt(SALT_FACTOR, function (err, salt) {
        if (err) return next(err);

        bcryptjs.hash(newPassword, salt, function (err, hashPassword) {

            if (err) return next(err);
            Admin.update({name: name}, {password: hashPassword}, function (err, raw) {
                assert.equal(err, null);
                // console.log('The raw response from Mongo was ', raw);
                delete req.session.admin;
                res.redirect('/admin/login');
            });
        });
    });
};

//midware for user signin and admin
exports.loginRequired = function (req, res, next) {
    var admin = req.session.admin;
    if (!admin) {
        req.session.hint = "请登录";
        return res.redirect('/admin/login');
    }
    next();
};

exports.editorLoginRequired = function (req, res, next) {
    var admin = req.session.admin;

    if (!admin) {
        req.session.hint = "请登录";
        return res.redirect('/admin/login');
    }

    if (!(admin.role == 7 || admin.role == 13 || admin.role == 42)) {
        req.session.hint = "对不起，当前账户没有此权限";
        return res.redirect('/admin');
    }
    next();
};

exports.uploaderLoginRequired = function (req, res, next) {
    var admin = req.session.admin;

    if (!admin) {
        req.session.hint = "请登录";
        return res.redirect('/admin/login');
    }

    if (!(admin.role == 12 || admin.role == 13 || admin.role == 42)) {
        req.session.hint = "对不起，当前账户没有此权限";
        return res.redirect('/admin');
    }
    next();
};

exports.superAdminRequired = function (req, res, next) {
    var admin = req.session.admin;

    if (!admin) {
        req.session.hint = "请登录";
        return res.redirect('/admin/login');
    }

    if (admin.role != 42) {
        return res.redirect('/admin/posts');
    }

    next();

};

exports.GETupload = function (req, res) {
    delete req.session.hint;
    res.render('admin/upload', {
        currentAdmin: req.session.admin.name
    });
};

exports.POSTupload = function (req, res) {
    var username = req.session.admin.name;

    if (req.busboy) {
        var isValidZip = false;
        req.busboy.on("file", function (fieldName, fileStream, fileName, encoding, mimeType) {
            //Handle file stream here
            isValidZip = (fileName == username + '.zip');
            if (isValidZip) {
                var localFStream = fs.createWriteStream('./upload-zips/' + fileName);
                fileStream.pipe(localFStream);
                localFStream.on('close', function () {
                    console.log(fileName + ' uploaded!');
                    console.log('Extracting files to /root/dev/' + username);
                    var directory = "/root/dev/" + username;
                    fs.emptyDir(directory, function (err) {
                        if (err) {
                            console.err(err);
                        } else {
                            fs.createReadStream('./upload-zips/' + fileName)
                                .pipe(unzip.Extract({path: directory}))
                                .on('close', function () {
                                    console.log('Unzipping finished.');
                                    res.redirect('/' + username);
                                });
                        }
                    });
                });

            } else {
                fileStream.resume();
                req.session.hint = '文件名格式不对';
                res.redirect('/admin/upload');
            }
        });
        req.pipe(req.busboy);
    }
};
