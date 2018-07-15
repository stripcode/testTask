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
    "shop/search/": "showShopSearchPage",
  },

  controller: {
    showAllShopsPage: function(){
      appRootView.showPrivateView(new AllShopsPage());
    },

    showShopSearchPage: function(){
      appRootView.showPrivateView(new ShopSearchPage());
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



var ShopSearchPage = Marionette.View.extend({

  template: require("templates/shop/shopSearchPage.tpl"),

  regions: {
    workspace: ".workspaceAllShopsPage"
  },

  events: {
    "click .submitShopSearchPage": "submit"
  },

  submit: function(){
    var shopCollection = new ShopCollection();
    shopCollection.fetch({
      url: "/data/shop/search/",
      data: {
        phrase: this.$el.find("input[name=search]").val()
      },
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