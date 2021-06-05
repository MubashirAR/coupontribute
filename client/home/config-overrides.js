/* eslint import/no-webpack-loader-syntax: off */
import * as ModuleFederationPlugin from 'webpack/lib/container/ModuleFederationPlugin'

module.exports = function override(config, env) {
    if (!config.plugins) {
        config.plugins = [];
    }
    console.log({ config })
    throw 'adasds'
    config.output.publicPath = 'http://localhost:3000'
    config.plugins.push(
        new ModuleFederationPlugin({
            name: 'home',
            library: { type: 'var', name: 'home'},
            filename: 'remoteEntry.js',
            remotes: {
                auth: 'auth'
            },
            shared: ['react', 'react-dom']
        })
    );

    return config;
}