var mongoose = require('mongoose');
var bcryptjs = require('bcryptjs');

var SALT_FACTOR = 10;

var AdminSchema = new mongoose.Schema({
    name: {
        unique: true,
        type: String
    },
    password: String,

    // role
    // 7: editor
    // 12: uploader
    // 15: editor and uploader
    // 42: super admin
    role: {
        type: Number,
        default: 7
    },
    meta: {
        createAt: {
            type: Date,
            default: Date.now()
        },
        updateAt: {
            type: Date,
            default: Date.now()
        }
    }
});

AdminSchema.pre('save', function (next) {
    var admin = this;

    if (this.isNew) {
        this.meta.createAt = this.meta.updateAt = Date.now()
    }
    else {
        this.meta.updateAt = Date.now()
    }

    bcryptjs.genSalt(SALT_FACTOR, function (err, salt) {
        if (err) return next(err);

        bcryptjs.hash(admin.password, salt, function (err, hash) {

            if (err) return next(err);
            admin.password = hash;
            next()
        })
    })
});

AdminSchema.methods = {
    comparePassword: function (_password, cb) {
        bcryptjs.compare(_password, this.password, function (err, isMatch) {
            if (err) {
                cb(err)
            }

            cb(null, isMatch)
        })
    }
};

AdminSchema.statics = {
    fetchReverse: function (cb) {
        return this
            .find({})
            .sort('-meta.createAt')
            .limit(10)
            .exec(cb)
    },
    findById: function (id, cb) {
        return this
            .findOne({_id: id})
            .exec(cb)
    }
};

module.exports = AdminSchema;