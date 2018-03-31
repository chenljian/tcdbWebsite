const mongoose = require('mongoose');
const PostSchema = require('../schemas/post');
const Post = mongoose.model('Post', PostSchema, 'tcdb');

module.exports = Post;