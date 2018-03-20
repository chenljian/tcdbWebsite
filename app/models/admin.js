const mongoose = require('mongoose');
const AdminSchema = require('../schemas/admin');
const Admin = mongoose.model('Admin', AdminSchema, 'admin');

module.exports = Admin;