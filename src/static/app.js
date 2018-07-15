import 'bootstrap/dist/css/bootstrap.css'
import 'font-awesome/css/font-awesome.css'
import "eonasdan-bootstrap-datetimepicker"
import "eonasdan-bootstrap-datetimepicker/build/css/bootstrap-datetimepicker.css"
import "select2/dist/css/select2.css"
import "select2/dist/js/select2.js"



export var app = new Marionette.Application({

  onStart: function(){
  }
});



$(document).ready(function(){
  app.start();
  Backbone.history.start();
});