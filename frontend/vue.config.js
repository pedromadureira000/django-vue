module.exports = {
  outputDir: '../django_vue/base/templates',
  assetsDir: '../static'
}

// module.exports = {
//   devServer: {
//     proxy: {
//       "^/api/": {
//         target: "http://localhost:8000",
//         changeOrigin: true,
//         logLevel: "debug",
//         pathRewrite: { "^/api": "/api" }
//       }
//     }
//   }
// };