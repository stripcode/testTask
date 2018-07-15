import {appRootView, XHRError} from "./other"



var LogoutRequest = Backbone.Model.extend({
  url: "/data/authRequest/logout/"
});



export var pageRouter = {

  routes: {
    "logout/": "showLogoutPage",
    "": "showDefaultPage",
  },

  controller: {
    showLogoutPage: function(){
      appRootView.showPrivateView(new LogoutPage());
    },

    showDefaultPage: function(){
      appRootView.showDefaultPage();
    }
  }
}



var LogoutPage = Marionette.View.extend({

  template: require("templates/page/logoutPage.tpl"),

  events: {
    "click .submitLogoutPage": "submit"
  },

  submit: function(){
    var model = new LogoutRequest();
    model.save({},{
      success: function(){
        location.reload();
      },
      error: XHRError
    });
  }
});