const mongoose = require('mongoose');

const Coupon = mongoose.model('Coupons', 
    {
        isUsed: Boolean,
        payment_status: {
            type: String,
            enum: ['paid', 'failed', 'ongoing'],
            default: 'ongoing'
        }
    }
);

module.exports = {
    Coupon
}