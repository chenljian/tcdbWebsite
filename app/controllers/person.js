const assert = require('assert');
const Person = require("../models/person");
const url = require('url');
const querystring = require('querystring');
const mongoose = require("mongoose");

exports.list = function(req, res){
	Person.find({},function(err, cards){
		res.render('admin/personlist',{
			currentAdmin: req.session.admin.name,
			userRole: req.session.admin.role,
			sortedCards: cards.sort('name')
		});
	});
};

exports.GETadd = function(req, res){
	res.render('admin/addperson',{
		currentAdmin: req.session.admin.name,
		person: ""
	});
};

exports.update = function(req, res){
	var _query = url.parse(req.url).query;
	var _person_id = querystring.parse(_query)._id;
	var filter = {'_id': _person_id};
	Person.findOne(filter, function(err, person){
		res.render('admin/addperson',{
			person: person
		});
	});
};

exports.PERSONadd = function(req, res){
	var person_id = req.body._id;
	if(peron_id == "" || !peron_id){
		//new person
		_person = new Person({
			photo: req.body.photo,
			name: req.body.name,
			department: req.body.department,
			jobTitle: req.body.jobTitle,
			email: req.body.email,
			homePage: req.body.homePage,
			position: req.body.position,
			introduction: req.body.position
		});
		_person.save(function(err, person){
			assert.equal(err, null);
			res.json({success: 1});
		});
	}
	else{
		//modify person
		var filter = {_id: req.body.id};
		var _person = req.body;
		Person.update(filter, _person);
	}
};

exports.delete = function(req, res){
	var _query = url.parse(req.url).query;
	var _person_id = querystring.parse(_query)._id;
	Person.remove({_id: _person_id}, function(err, person){
		assert.equal(err, null);
		res.json({success: 1});
	});
};
