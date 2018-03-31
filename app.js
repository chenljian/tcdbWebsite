const express = require('express');
const app = express();
const mongoose = require('mongoose');
const path = require('path');
const port = 2333;
const bodyParser = require("body-parser");
const session = require('express-session');
const mongoStore = require('connect-mongo')(session);
const busboy = require('connect-busboy');
var logger = require('./log');
// connect to database db
var dbURL = 'mongodb://localhost/db';
mongoose.connect(dbURL);
app.use(session({
    secret: 'tcdb',
    resave: false,
    saveUninitialized: true,

    store: new mongoStore({
        url: dbURL,
        collection: 'sessions'
    })
}));

// setting
//set static dir
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static('/root/conferences'));

app.use(function (req, res, next) {
    logger.info("pageview " + req.connection.remoteAddress + " " + req.originalUrl);
    next();
}, express.static('/root/dev'));

//set tempalte engine
app.set('view engine', 'pug');
app.set('views', './app/views/pages/');

app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));
app.use(bodyParser.json());
app.use(busboy());
// routes分配
require('./config/routes')(app);

const server = app.listen(port, function () {
    var host = server.address().address;
    var port = server.address().port;
    logger.log('App listening at http://%s:%s', host, port);
});
