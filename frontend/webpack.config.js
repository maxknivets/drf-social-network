module.exports = {
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
        },
        {
          test: /\.css$/,
          loader: 'style-loader'
        },
        {
          test: /\.css$/,
          loader: 'css-loader',
          options: {
            modules: true,
            //localIdentName: '[name]__[local]___[hash:base64:5]'
          }
        }
      ],
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