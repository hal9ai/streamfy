// npx vue-cli-service inspect > webpack.js

module.exports = {
  publicPath: './',
  chainWebpack: config => {
    config.optimization.minimizer('terser').tap(args => {
      // args[0].terserOptions.compress.dead_code = false;
      return args;
    });
  }
}