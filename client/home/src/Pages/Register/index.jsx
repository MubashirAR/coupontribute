import React from 'react'

export default () => {
    return <>
        <div className="container login-container">
            <div className="card login-card" >
                <div className="card-body login-card-body">
                    <h5 className="card-title">Card title</h5>
                    <form>
                        <div className="form-group">
                            <label for="exampleInputEmail1">Email</label>
                            <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" />
                            {/* <small id="emailHelp" className="form-text text-muted">We'll never share your email with anyone else.</small> */}
                        </div>
                        <div className="form-group">
                            <label for="exampleInputPassword1">Name</label>
                            <input type="text" className="form-control" id="exampleInputPassword1" placeholder="Your Name" />
                        </div>
                        <div className="form-group">
                            <label for="exampleInputPassword1">Password</label>
                            <input type="password" className="form-control" id="exampleInputPassword1" placeholder="Password" />
                        </div>
                        <button type="submit" class="btn btn-primary login-btn">Login</button>
                    </form>
                </div>
            </div>
        </div>

    </>
}