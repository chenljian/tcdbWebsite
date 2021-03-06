const mongoose = require('mongoose');

//define person schema
var PersonSchema = new mongoose.Schema({
	photo: String,
	name: String,
	department: String,
	jobTitle: String,
	email: String,
	homePage: String,
	position: String,
	introduction: String
});

module.exports = PersonSchema;
