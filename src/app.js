const path = require('path')
const express = require('express')
const hbs = require('hbs')

const app = express()
const port = process.env.PORT || 3000

// Define paths for Express config
const publicDirectoryPath = path.join(__dirname, '../public')
const viewsPath = path.join(__dirname, '../templates/views')
const partialsPath = path.join(__dirname, '../templates/partials')

// Setup handlebars engine and views location
app.set('view engine', 'hbs')
app.set('views', viewsPath)
hbs.registerPartials(partialsPath)

// Setup static directory to serve
app.use(express.static(publicDirectoryPath))

//index
app.get('', (req, res) => {
    res.render('index', {
        title: 'Reddit City Locations',
        name: 'Yoon Choi'
    })
})

//about
app.get('/about', (req, res) => {
    res.render('about', {
        title: 'About Me',
        name: 'Yoon Choi'
    })
})

//help
app.get('/help', (req, res) => {
    res.render('help', {
        helpText: 'This is some helpful text.',
        title: 'Help',
        name: 'Yoon Choi'
    })
})

//help 404
app.get('/help/*', (req, res) => {
    res.render('404', {
        title: '404',
        name: 'Yoon Choi',
        errorMessage: 'Help article not found.'
    })
})

//404
app.get('*', (req, res) => {
    res.render('404', {
        title: '404',
        name: 'Yoon Choi',
        errorMessage: 'Page not found.'
    })
})

app.listen(port, () => {
    console.log('Server is up on port ' + port)
})