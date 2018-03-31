const mongoose = require('mongoose');
const PersonSchema = require('../schemas/person');
const Person = mongoose.model('Person', PersonSchema,'tcdbPerson');

module.exports = Person;