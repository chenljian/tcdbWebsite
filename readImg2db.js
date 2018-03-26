//read img to mongodb
var mongoose = require('mongoose');
var fs = require('fs');
mongoose.connect('mongodb://localhost/db');
var db = mongoose.connection;

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

var fileUrl = "./public/assets/images";
var imageData = fs.readFileSync(fileUrl+'/slide/example-slide-1.jpg');
var imageBase64 = imageData.toString("base64");
//var imagePrefix = "data:image/jpeg;base64,";
//document.getElementById('img').src = imagePrefix + imageBase64;

var PersonEntity = new PersonModel({
	photo:imageBase64,
	name: "Mack"
});

PersonEntity.save(function(err){
	if(err){
		console.log(err);
	}
	else{
		console.log("save success!");
	}
});



