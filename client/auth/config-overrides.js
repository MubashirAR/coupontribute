/* eslint import/no-webpack-loader-syntax: off */
const ModuleFederationPlugin = require('webpack/lib/container/ModuleFederationPlugin')

module.exports = function override(config, env) {
    if (!config.plugins) {
        config.plugins = [];
    }
    console.log({ config })
    throw 'authhhhh'
    config.output.publicPath = 'http://localhost:3001'
    config.plugins.push(
        new ModuleFederationPlugin({
            name: 'auth',
            library: { type: 'var', name: 'auth'},
            filename: 'remoteEntry.js',
            exposes: {
                Login: './src/Pages/Login',
                Register: './src/Pages/Register'
            },
            shared: ['react', 'react-dom']
        })
    );

    return config;
}