import {appRootView, XHRError} from "./other"



var AuthRequest = Backbone.Model.extend({
  url: "/data/authRequest/"
});



export var authRouter = {

  routes: {
    "enter/": "showAuthPage",
  },

  controller: {
    showAuthPage: function(){
      appRootView.showChildView("workspace", new AuthPage());
    }
  }
}



var AuthPage = Marionette.View.extend({

  template: require("templates/auth/authPage.tpl"),

  events: {
    "click .submitAuthPage": "submit"
  },

  submit: function(){
    var request = new AuthRequest();
    request.save({
      login: this.$el.find("input[name=login]").val(),
      password: this.$el.find("input[name=password]").val()
    },{
      success: function(model){
        console.log(model)
      },
      error: XHRError
    })
  }
});