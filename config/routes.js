const Index = require('../app/controllers/index');
const Post = require("../app/controllers/post");
const Admin = require("../app/controllers/admin");
const logger = require("../log");

module.exports = function (app) {

    // pre handle user
    app.use(function (req, res, next) {
        logger.info("pageview " + req.connection.remoteAddress + " " + req.originalUrl);
        app.locals.user = req.session.user;
        app.locals.hint = req.session.hint;
        next();
    });

    app.get('/', Index.index);
    app.get('/commintro', Index.commintro);
    app.get('/honormember', Index.honormember);
    app.get('/contact', Index.contact);
    app.get('/resources', Index.resources);
    app.get('/opensource', Index.opensource);
    app.get('/documents', Index.documents);
    app.get('/special', Index.special);
    app.get('/vldbsummerschool', Index.vldbsummerschool);
    app.get('/vldbsummerschool2016', Index.vldbsummerschool2016);
    app.get('/vldbsummerschool2015', Index.vldbsummerschool2015);
    app.get('/vldbsummerschool2014', Index.vldbsummerschool2014);
    app.get('/vldbsummerschool2013', Index.vldbsummerschool2013);
    app.get('/newsdynamics', Index.newsdynamics);
    app.get('/commdynamics', Index.commdynamics);
    app.get('/confinfo', Index.confinfo);
    app.get('/dseintro', Index.dseintro);
    app.get('/dseeditors', Index.dseeditors);
    app.get('/dsecallforpaper', Index.dsecallforpaper);
    app.get('/dsepaperlist', Index.dsepaperlist);
    app.get('/conferences', Index.conferences);
    app.get('/dev', Index.dev);

    app.get('/post*', Post.GETpost);
    app.get('/search/q*', Post.search);
    app.get('/admin/login', Admin.login);
    app.post('/admin/login', Admin.POSTlogin);

    // 需要登录
    app.get('/admin/modifypassword', Admin.loginRequired, Admin.modifyPassword);
    app.post('/admin/modifypassword', Admin.loginRequired, Admin.POSTmodifyPassword);
    app.get('/admin/logout', Admin.loginRequired, Admin.logout);

    // editor

    app.get('/admin/posts', Admin.editorLoginRequired, Post.list);
    app.get('/admin/addpost', Admin.editorLoginRequired, Post.GETadd);
    app.get('/admin/updatepost', Admin.editorLoginRequired, Post.update);
    app.post('/admin/addpost', Admin.editorLoginRequired, Post.POSTadd);
    app.delete('/admin/posts/', Admin.editorLoginRequired, Post.delete);
    app.get('/admin/index', Admin.loginRequired, Admin.index);
    app.get('/admin', Admin.loginRequired, Admin.index);


    // superadmin
    app.get('/admin/signup', Admin.editorLoginRequired, Admin.superAdminRequired, Admin.signup);
    app.post('/admin/signup', Admin.editorLoginRequired, Admin.superAdminRequired, Admin.POSTsignup);

    // uploader
    app.get('/admin/upload', Admin.uploaderLoginRequired, Admin.GETupload);
    app.post('/admin/upload', Admin.uploaderLoginRequired, Admin.POSTupload);
};
