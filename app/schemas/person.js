const mongose = require('mongoose');

//define person schema
var PersonSchema = new mongoose.schema({
	photo: String,
	name: String,
	department: String,
	jobTitle: String,
	email: String,
	homePage: String,
	position: String,
});

module.exports = PersonSchema;