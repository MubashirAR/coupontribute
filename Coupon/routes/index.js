var express = require('express');
var router = express.Router();
var amqp = require('amqplib/callback_api');



const CouponService = require('../lib/service/Coupons')
/* GET home page. */
router.get('/', async function(req, res, next) {
  try {
    amqp.connect('amqp://event-bus', function(error0, connection) {
  if (error0) {
    throw error0;
  }
  connection.createChannel(function(error1, channel) {
    if (error1) {
      throw error1;
    }
    var queue = 'hello';
    var msg = JSON.stringify({
      'task': 'hello',
      'id': Math.round(Math.random()*100000) + '',
      'args': ['id', 'asdasd'],
      "kwargs": {},
      "retries": 0,
      "eta": new Date()
    });
  
    channel.assertQueue(queue, {
      durable: true
    });
  
    channel.sendToQueue(queue, Buffer.from(msg));
    console.log(" [x] Sent %s", msg);
  });

});
    let couponService = new CouponService();
    const data = await couponService.getCoupons()
    res.send({
      status: 'success',
      msg: 'Fetched data!',
      data
    })
  } catch (error) {
    console.error(error)
    res.send({
      status: 'error',
      msg: 'Something went wrong!'
    })
  }
});
router.post('/', async function(req, res, next) {
  try {
    let couponService = new CouponService();
    const data = await couponService.createCoupon(req.body)
    res.send({
      status: 'success',
      msg: 'Fetched data!',
      data
    })
  } catch (error) {
    console.error(error)
    res.send({
      status: 'error',
      msg: 'Something went wrong!'
    })
  }
});

module.exports = router;
