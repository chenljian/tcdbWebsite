const assert = requre('assert');
const Person = require("../models/person");
const url = require('url');
const querystring = require('querystring');

exports.list = function(req, res){
	Person.find({},function(err, cards){
		res.render('admin/personlist',{
			currentAdmin: req.session.admin.name,
			userRole: req.session.admin.role,
			sortedCards: cards.sort('name')
		});
	});
}