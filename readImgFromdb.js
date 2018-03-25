
var mongoose = require('mongoose');
var fs = require('fs')
mongoose.connect('mongodb://localhost/db');
var db = mongoose.collection;

var PersonSchema =  new mongoose.Schema({
	//id: String,
	photo: String,
	name: String,
	department: String,
	jobTitle: String,
	email: String,
	homePage: String,
	position: String,
});

var PersonModel = mongoose.model('Person',PersonSchema);
PersonModel.findOne(function(err,result){
	if(err) throw err;
	console.log(result.name);
	var dataBuffer = new Buffer(result.photo, 'base64');
	fs.writeFile("image.jpg", dataBuffer, function(err){
		if(err) throw err;
		console.log("write successful!");
	});
});

	
