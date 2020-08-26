const path = require("path");

const CopyWebpackPlugin  = require("copy-webpack-plugin");
const BundleTracker = require("webpack-bundle-tracker");
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
  publicPath: "http://127.0.0.1:8080/", 
  outputDir: './dist/',

  pages: {
    index: {
      entry: "src/main.js",
      template: "public/index.html",
      filename: "index.html"
    }
  },

  devServer: {
    // // the first 3 lines of the following code have been added to the configuration
    public: 'http://127.0.0.1:8080',
    host: '127.0.0.1',
    port: 8080,
    clientLogLevel: "warning",
    disableHostCheck: true,
    hot: true,
    https: false,
    headers: {"Access-Control-Allow-Origin": ["\*"]},
    // contentBase: "dist",
    compress: true,
    open: true,
    overlay: {warnings: false, errors: true},
    // publicPath: "/",
    quiet: true,
    watchOptions: {
      poll: 1000,
      ignored: /node_modules/
    }
  },
  chainWebpack: config => {

    config.module
      .rule("vue")
      .use("vue-loader")
      .loader("vue-loader")
      .tap(options => {
        options.compilerOptions.preserveWhitespace = true;
        return options;
      });
  },
  productionSourceMap: false,

  assetsDir: "./assets/",
  configureWebpack: {
    plugins: [
      new BundleTracker({ filename: './webpack-stats.json' }),
      // new CopyWebpackPlugin([
      //   {from: "src/assets/images", to: "assets/img"},
      // ])
    ]
  },

  lintOnSave: false,
  pluginOptions: {},

  transpileDependencies: ["vue-echarts", "resize-detector"]
};
