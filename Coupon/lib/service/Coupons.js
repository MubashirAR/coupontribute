const models = require('../../models')
// const Model from "mongoose";
class Coupon {
    createCoupon = async data => {
        let coupon = new models.Coupon(data);
        let result = await coupon.save()
        return result
    }
    createCouponBulk = async list => {
        let coupons = list.map(data => new models.Coupon(data));
        let result = models.Coupon.insertMany(coupons);
        return result
    }
    getCoupons = async query => {
        let coupons = await models.Coupon.find();
        return coupons
    }
}
module.exports = Coupon