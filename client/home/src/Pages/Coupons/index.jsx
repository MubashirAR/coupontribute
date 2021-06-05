import React from 'react'

export default () => {
    let coupons = [{
        amount: 10,
        count: 10
    }, {
        amount: 20,
        count: 10
    }];
    let currencies = [{
        name: 'Indian Rupee',
        abbreviation: 'INR',
        symbol: '₹',
        coupons
    }, {
        name: 'United States Dollar',
        abbreviation: 'USD',
        symbol: '$',
        coupons
    }]
    return <div className="container">
        {
            currencies.map(currency => (
                <>
                    <h4>{currency.name} ({currency.abbreviation})</h4>
                    <table className="table table-bordered">
                        <thead>
                            <tr>
                                <th scope="col">Amount</th>
                                <th scope="col">No. of coupons</th>
                            </tr>
                        </thead>
                        <tbody>
                            {currency.coupons.map(coupon => (
                                <tr>
                                    <th scope="row">{currency.symbol}{coupon.amount}</th>
                                    <td>{coupon.count}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </>
            ))
        }
    </div>
}