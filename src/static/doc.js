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
    "doc/:id": "showDocPage"
  },

  controller: {
    showAllDocsPage: function(){
      appRootView.showPrivateView(new AllDocsPage());
    },
    showDocPage: function(id){
      var doc = new Doc();
      doc.fetch({
        url: "/data/doc/" + id,
        success: function(model){
          appRootView.showPrivateView(new DocPage({model: model}));
        },
        error: XHRError
      })
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



var DocPage = Marionette.View.extend({

  template: require("templates/doc/docPage.tpl"),

  events: {
    "click .cancelDocPage": "cancel"
  },

  cancel: function(){
    history.back();
  }
});



var DocCollectionView = Marionette.View.extend({

  template: require("templates/doc/docCollectionView.tpl")
});