module.exports = {
  outputDir: '../docs',
  transpileDependencies: ['vuetify'],
  assetsDir: './',
  publicPath: process.env.NODE_ENV === 'production' ? '/kumagai/' : '/',
  pages: {
    index: {
      entry: 'src/main.js',
      title: '特許データ分析アプリ'
    }
  }
}
