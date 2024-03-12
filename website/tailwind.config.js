/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './templates/*.html',
    './static/src/**/*.js',
    './static/src/*.js'
  ],
  theme: {
    extend: {}
  },
  plugins: [require('daisyui')]
}
