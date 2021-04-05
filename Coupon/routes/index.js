var express = require('express');
var router = express.Router();
const CouponService = require('../lib/service/Coupons')
/* GET home page. */
router.get('/', async function(req, res, next) {
  try {
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
