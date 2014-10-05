'use strict';

/* Controllers */

/* Sample Controller */
/*
.controller('sample',['$scope','$http','$cookieStore', function($scope,$http,$cookieStore){
	console.log("sample")
}])
*/

angular.module('angularProject.controllers', [])

.controller('home',['$scope','$http','$cookieStore', function($scope,$http,$cookieStore){
    //console.log("home");
	$scope.logout = function logout(){
        $cookieStore.remove('token');
        location.assign('#/');
    };
}])




.controller('account',['$scope','$http', function($scope,$http){
	//console.log("account");
}])




.controller('leaderboard',['$scope','$http','baseURL', function($scope,$http,baseURL){
	//console.log("leaderboard");
    $http({method:"GET",url: baseURL + "players/"}).success(function(data){
        $scope.players = data;
        console.log($scope.players)
    })
    
}])




.controller('match',['$scope','$http','passPubNub','passGameInfo','$cookieStore','baseURL', function($scope,$http,passPubNub,passGameInfo,$cookieStore,baseURL){
	//console.log("match");
    //console.log(passGameInfo.getGameInfo())
    $scope.game = passGameInfo.getGameInfo()
    var channel_name = $scope.game.channelName;
    var pubnub = passPubNub.getPubNub()
    $scope.defeated = false;
    pubnub.subscribe({
        channel : channel_name,
        message : function(m){ handle(m) },
    });

    $scope.broadcastVictory = function(){
        console.log("BROADCAST!!!")
        var gameData = {"channelName": channel_name,"status":"completed"}
        $http({method:"POST",url: baseURL + "game/status/",data: gameData }).success(function(data){
            console.log(data)
        })
        pubnub.publish({
            channel : channel_name,
            message : {"player":$cookieStore.get('userdata').username,"text":"won"}
        })
    }

    $scope.redirectToHome = function(){
        location.assign('#/');
        location.reload();
    }

    $scope.concedeDefeat = function(){

    }

    $scope.aceChanged = function(e) {
            pubnub.publish({
                channel : channel_name,
                message : {"player":$cookieStore.get('userdata').username,"text":e[0]['data']['text']}
            })
        };

    $http({method:"GET",url: baseURL + "game/search/"}).success(function(data){
        $scope.game = data;        
        $scope.playerNames = [];
        $scope.output = "";
        $scope.player = []
        for(var i =0;i< $scope.game.gameMembers.length;i++){
            if($cookieStore.get('userdata').username != $scope.game.gameMembers[i].username){
                $scope.playerNames.push($scope.game.gameMembers[i].username)
            }
        }

        if($scope.playerNames[0]){
            $scope.player[0] = {}
            $scope.player[0].username = $scope.playerNames[0];
            $scope.player[0].typedCode = "";
        }

        if($scope.playerNames[1]){
            $scope.player[1] = {}
            $scope.player[1].username = $scope.playerNames[1]
            $scope.player[1].typedCode = "";
        }

        if($scope.playerNames[2]){
            $scope.player[2] = {}
            $scope.player[2].username = $scope.playerNames[2]
            $scope.player[2].typedCode = "";
        }

        /*
        {"player":"__username__","text":"__text__"}
        */
        $scope.build = function(code){
            var funcResponse = code;
            var unitTests = $scope.game.unitTests;
            console.log(funcResponse)
            var check = false;
            var output = new Function("x","y",funcResponse)
            for(var i = 0;i < unitTests.length;i++){
                var answer = output(unitTests[i].firstInput,unitTests[i].secondInput)
                if(answer == unitTests[i].result){
                    check = true;
                }
                else{
                    check = false;
                }
            }
            
            if(check){
                $scope.winner = true;
            }
        }
    })

    function handle(m){
        $scope.$apply(function(){
            if(m.text == "won" && m.player != $cookieStore.get('userdata').username){
                $scope.defeated = true;
                console.log("DEFEATED!!!");
                $('#defeat').css('display','block');
                $('#defeat').attr('class','modal fade in');
            }
            else{
                for(var i = 0; i < $scope.playerNames.length;i++){
                    if($scope.playerNames[i] == m.player){
                        $scope.player[i].typedCode += m.text;
                    }
                }
            }
        })
    }
    
}])




.controller('finding_match',['$scope','$http','baseURL','passPubNub','passGameInfo', function($scope,$http,baseURL,passPubNub,passGameInfo){
	//console.log("finding match");

    $http({method:"GET",url: baseURL + "game/search/"}).success(function(data){
        $scope.game = data;
        passGameInfo.setGameInfo(data)


        console.log(data)
        var channel_name = data.channelName;
        
        var pubnub = PUBNUB.init({
            publish_key   : 'pub-c-93c79041-9bb5-4adb-9afe-939047661a21',
            subscribe_key : 'sub-c-7431702c-0889-11e4-ae9d-02ee2ddab7fe'
        });

        pubnub.subscribe({
            channel : channel_name,
            message : function(m){ console.log(m) },
            connect : publish
        });

        function publish() {
            pubnub.publish({
                channel : channel_name,
                message : "Hi."
            })
        };

        pubnub.here_now({
            channel : channel_name,
            callback : function(m){
                $scope.$apply(function(){
                    if(m.uuids.length == 4){
                        passPubNub.setPubNub(pubnub)
                        location.assign('#/match');
                    }
                    $scope.playerCount=m.uuids.length;
                })
            }
        });
        window.setInterval(function(){
        pubnub.here_now({
            channel : channel_name,
            callback : function(m){
                $scope.$apply(function(){
                    if(m.uuids.length == 4){
                        passPubNub.setPubNub(pubnub)
                        location.assign('#/match');
                    }
                    $scope.playerCount=m.uuids.length;
                })
            }
        });
        }, 2500);
        
    })
}])





.controller('sidebar',['$scope','$http','$cookieStore', function($scope,$http,$cookieStore){
    $scope.logout = function logout(){
        $cookieStore.remove('token');
        location.assign('#/');
    };
}])




.controller('header',['$scope','$http','$cookieStore', function($scope,$http,$cookieStore){
    var userdata = $cookieStore.get('userdata')
    $scope.username = userdata.username
    $scope.logout = function logout(){
        $cookieStore.remove('token');
        location.assign('#/');
    };
}])




.controller('auth',['$scope','$cookieStore',function($scope,$cookieStore){
    //console.log("auth");
    $scope.is_logged = function is_logged(){
        if($cookieStore.get('token')){
            return true;
        }
        else{
            return false;
        }
    };
}])





.controller('signin',['$scope','$cookieStore','$http','$location','baseURL', function($scope,$cookieStore,$http,$location,baseURL){

    $scope.submit = function(username,password){
        var user_data = {
            "username": username,
            "password": password
        };
        $http({method:"POST",url: baseURL + "api-token-auth/", data: user_data})
        .success(function(response) {
            $cookieStore.put('token', response.token);
            $http.defaults.headers.common['Authorization'] = 'Token ' + response.token;

            $http({method:"GET",url: baseURL + "user/profile/"}).success(function(data){
                $cookieStore.put('userdata',data)
            })

            if($cookieStore.get('token')){
                location.assign("#/home");
            };
        });
    };
}])