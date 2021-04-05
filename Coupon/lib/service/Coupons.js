const models = require('../../models')
// const Model from "mongoose";
class Coupon {
    createCoupon = async data => {
        let coupon = new models.Coupon(data);
        let result = await coupon.save()
    }
    getCoupons = async query => {
        let coupons = await models.Coupon.find();
        return coupons
    }
}
module.exports = Coupon