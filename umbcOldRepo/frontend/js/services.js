'use strict';

var service = angular.module('angularProject.services', ['ngResource'])

service.service('passPubNub', function() {
	var pubNub = null;
    return {
    	getPubNub:  function(){
    		return pubNub;
    	},
    	setPubNub:  function(value){
    		pubNub = value;
    	},
    }
});

service.service('passGameInfo', function() {
	var game = null;
    return {
    	getGameInfo:  function(){
    		return game;
    	},
    	setGameInfo:  function(value){
    		game = value;
    	},
    }
});