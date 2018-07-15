const path = require("path");
const webpack = require("webpack");



ExtractTextPlugin = require("extract-text-webpack-plugin");



module.exports = {

  entry: {
    app: "./app.js",
  },

  output: {
    path: path.resolve(__dirname, "../flask/app/static"),
    filename: "[name].js"
  },
  mode: "development",
  devtool: "source-map",

  resolve: {
    alias: {
      templates: path.resolve(__dirname, "templates/")
    },
  },

  module: {

    rules:[{
      test: /.js$/,
      exclude: /(node_modules|bower)/,
      use: {
        loader: "babel-loader"
      }
    },{

      test: /.tpl$/,
      exclude: /node_modules/,
      use: {
        loader:"twig-loader"
      }
    },{
      test: /\.css$/,
      use:  ExtractTextPlugin.extract({
        fallback: "style-loader",
        use: "css-loader"
      })
    },{
     test: /\.(woff|woff2|eot|ttf|otf|svg)$/,
     use: [
       'file-loader?name=[name].[ext]'
     ]
    },{
     test: /\.(png|svg|jpg|gif)$/,
     use: [
       'file-loader?name=[name].[ext]'
     ]
    }]
  },

  plugins: [
    new ExtractTextPlugin("app.css"),
    new webpack.ProvidePlugin({
          $: "jquery",
          jQuery: "jquery",
          _: "underscore",
          Marionette: "backbone.marionette",
          Backbone: "backbone",
          moment: "moment",
          Tinycon: "tinycon",
          Inputmask: "inputmask"
       })
  ]
};