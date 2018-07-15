import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import 'font-awesome/css/font-awesome.css'
import "eonasdan-bootstrap-datetimepicker"
import "eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.css"
import "select2/dist/css/select2.css"
import "select2/dist/js/select2.js"



import {authRouter} from "./auth"
import {pageRouter} from "./page"
import {XHRError, appRootView} from "./other"



var router = Marionette.AppRouter.extend({
});



var app = new Marionette.Application({

  onStart: function(){
    var r = new router();
    r.processAppRoutes(authRouter.controller, authRouter.routes);
    r.processAppRoutes(pageRouter.controller, pageRouter.routes);
  }
});



$(document).ready(function(){
  app.start();
  Backbone.history.start();
});