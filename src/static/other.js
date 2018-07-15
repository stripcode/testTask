var AppRootView = Marionette.View.extend({

  template: false,

  el: "body",

  regions: {
    "workspace": ".workspaceAppRootView",
  }
});



export var appRootView = new AppRootView();



export function XHRError(mode, xhr){
  alert(xhr.responseText);
}