module.exports = {
  outputDir: '../docs',
  transpileDependencies: ['vuetify'],
  assetsDir: './',
  // publicPath: '/ex_design/'
  publicPath: process.env.NODE_ENV === 'production' ? '/ex_design/' : '/',
  pages: {
    index: {
      entry: 'src/main.js',
      title: '文献管理システム実験アプリ'
    }
  }
}
