const mongoose = require('mongoose');

mongoose.connect('mongodb://coupon-db-srv/db', {useNewUrlParser: true, useUnifiedTopology: true}, (err) => console.log('Mongo connected', err));
