const mongoose = require('mongoose');

//define database schema
var PostSchema = new mongoose.Schema({
    category: String,
    source: String,
    title_en: String,
    date: String,
    special_recomm: Boolean,
    news_cover: String,
    title_cn: String,
    content: String,
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

PostSchema.pre('save', function (next) {
    if (this.isNew) {
        this.meta.createAt = this.meta.updateAt = Date.now()
    }
    else {
        this.meta.updateAt = Date.now()
    }
    next()
});

PostSchema.statics = {
    findLast: function (filter, cb) {
        return this
            .find(filter)
            .sort({'title_en': '-1'})
            .limit(1)
            .exec(cb)
    }
};

module.exports = PostSchema;