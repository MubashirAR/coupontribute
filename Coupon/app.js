var express = require('express');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const mongoose = require('mongoose');
require('express-async-errors');

var indexRouter = require('./routes/index');
require('./dbConnect')

var app = express();

const handleErrors = (err, req, res, next) => {
    if(err instanceof mongoose.Error.ValidationError) {
        return res.status(400).send({
            msg: 'Invalid Input',
            errors: err.errors.map(e => ({ message: e.message }))
        })
    }
    console.error(err)
    res.status(500).send({
        msg: `Something went wrong. ${err.message}`,
        errors: [{ message: err.message }]
    })
    
}

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use('/', indexRouter);
app.use('/', handleErrors);

module.exports = app;
