/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.{html,js}"],
    theme: {
        fontFamily: {
            'title': ['Rubik', 'Inter', 'sans-serif']
        },
        extend: {
            colors: {
                card: '#26292f',
                background: '#434956',
                separator: '#474b54',
                backgrounddark: '#36393f',
                version: '#b0bac5',
            }
        }
    },
    plugins: [],
}