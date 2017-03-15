var events = require('events');
var util = require('util');

var person = function(name){
  this.name = name;
};

util.inherits(person, events.EventEmitter);

var james = new person('james');
var john = new person('john');
var boi = new Person('boi');
var people = [james, john, boi]

people.forEach(function(person){
  person.on('speak', function(msg){
    console.log(person.name + ' said: ' + msg)
  });
});

james.emit('speak', 'oof')