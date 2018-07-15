import {appRootView, XHRError} from "./other"



var Doc = Backbone.Model.extend({
  url: "/data/doc/"
});



var DocCollection = Backbone.Collection.extend({
  model: Doc,
  url: "/data/doc/"
});



export var docRouter = {

  routes: {
    "doc/": "showAllDocsPage",
  },

  controller: {
    showAllDocsPage: function(){
      appRootView.showPrivateView(new AllDocsPage());
    }
  }
}



var AllDocsPage = Marionette.View.extend({

  template: require("templates/doc/allDocsPage.tpl"),

  regions: {
    workspace: ".workspaceAllDocsPage"
  },

  onRender: function(){
    var docCollection = new DocCollection();
    docCollection.fetch({
      success: _.bind(function(collection){
        this.showChildView("workspace", new DocCollectionView({collection: collection}));
      }, this),
      error: XHRError
    })
  }
});



var DocCollectionView = Marionette.View.extend({

  template: require("templates/doc/docCollectionView.tpl")
});