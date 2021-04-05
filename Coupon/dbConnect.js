const mongoose = require('mongoose');

mongoose.connect('mongodb://coupon-db/db', {useNewUrlParser: true, useUnifiedTopology: true}, () => console.log('Mongo connected'));
