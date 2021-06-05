import React from 'react'

const getFormattedDate = date => {
    return `${date.getDate()}/${date.getMonth()}/${date.getFullYear()} ${date.getHours()}:${date.getSeconds()}`
}
export default () => {
    let payments = [{
        currency: {
            name: 'Indian Rupee',
            abbreviation: 'INR',
            symbol: '₹'
        },
        amount: '100',
        paymentDate: new Date()
    }];
    return <div className="container">

        <table className="table table-bordered">
            <thead>
                <tr>
                    <th scope="col">Amount</th>
                    <th scope="col">Payment date</th>
                </tr>
            </thead>
            <tbody>
                {payments.map(payment => (
                    <tr>
                        <th scope="row">{payment.currency.symbol}{payment.amount}</th>
                        <td>{getFormattedDate(payment.paymentDate)}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}