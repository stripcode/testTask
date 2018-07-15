import 'bootstrap/dist/css/bootstrap.css'
import 'font-awesome/css/font-awesome.css'
import "eonasdan-bootstrap-datetimepicker"
import "eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.css"
import "select2/dist/css/select2.css"
import "select2/dist/js/select2.js"



import {authRouter} from "./auth"
import {XHRError} from "./other"
import {User} from "./user"



var router = Marionette.AppRouter.extend({
});



var app = new Marionette.Application({

  onStart: function(){

    var r = new router();
    r.processAppRoutes(authRouter.controller, authRouter.routes);

    var currentUser = new User();
    currentUser.fetch({
      url: "/data/user/session/",
      success: function(){
      },
      error: function(){
        location.hash = "enter/"
      }
    })
  }
});



$(document).ready(function(){
  app.start();
  Backbone.history.start();
});