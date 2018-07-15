import {appRootView, XHRError} from "./other"



var Shop = Backbone.Model.extend({
  url: "/data/shop/"
});



var ShopCollection = Backbone.Collection.extend({
  model: Shop,
  url: "/data/shop/"
});



export var shopRouter = {

  routes: {
    "shop/": "showAllShopsPage",
  },

  controller: {
    showAllShopsPage: function(){
      appRootView.showPrivateView(new AllShopsPage());
    }
  }
}



var AllShopsPage = Marionette.View.extend({

  template: require("templates/shop/allShopsPage.tpl"),

  regions: {
    workspace: ".workspaceAllShopsPage"
  },

  onRender: function(){
    var shopCollection = new ShopCollection();
    shopCollection.fetch({
      success: _.bind(function(collection){
        this.showChildView("workspace", new ShopCollectionView({collection: collection}));
      }, this),
      error: XHRError
    })
  }
});



var ShopCollectionView = Marionette.View.extend({

  template: require("templates/shop/shopCollectionView.tpl")
});