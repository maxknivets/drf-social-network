module.exports = {
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
        }
      ]
    },
    mode: 'development',
    output: {
        publicPath: 'http://localhost:9000/static/',
    },
    devServer: {
        contentBase: './static',
        port: 9000,
        headers: {
          'Access-Control-Allow-Origin': '*'
        },
        compress: true,
        hot: true
    },
  };