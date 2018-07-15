import {User} from "./user"



var AppRootView = Marionette.View.extend({

  template: false,

  el: "body",

  regions: {
    "workspace": ".workspaceAppRootView"
  },

  initialize: function(){
    this.currentUser = new User();
  },

  showDefaultPage: function(view){
    if(this.currentUser.has("id")){
      this.showChildView("workspace", new PrivatePage({model: this.currentUser}))
    }else{
      this.currentUser.fetch({
        url: "/data/user/session/",
        success: _.bind(function(model){
          this.showChildView("workspace", new PrivatePage({model: model}))
        }, this),
        error: function(){
          location.hash = "enter/"
        }
      });
    }
  },

  showPrivateView: function(view){
    if(this.currentUser.has("id")){
      this.getChildView("workspace").showChildView("workspace", view)
    }else{
      this.currentUser.fetch({
        url: "/data/user/session/",
        success: _.bind(function(model){
          this.showChildView("workspace", new PrivatePage({model: model}))
          this.getChildView("workspace").showChildView("workspace", view)
        }, this),
        error: function(){
          location.hash = "enter/"
        }
      });
    }
  }
});



export var appRootView = new AppRootView();



export function XHRError(mode, xhr){
  alert(xhr.responseText);
}



var PrivatePage = Marionette.View.extend({

  template: require("templates/other/privatePage.tpl"),

  regions: {
    menu: ".menuPrivatePage",
    workspace: ".workspacePrivatePage"
  },

  onRender: function(){
    this.showChildView("menu", new UserMenu({model: this.model}))
    this.showChildView("workspace", new WelcomeView())
  }
});



var UserMenu = Marionette.View.extend({

  template: require("templates/other/userMenu.tpl")
});



var WelcomeView = Marionette.View.extend({

  template: require("templates/other/welcomeView.tpl")
});