import React from 'react'
import './login.scss'
export default () => {
    return <>
        <div className="container login-container">
            <div className="card login-card" >
                <div className="card-body login-card-body">
                    <h5 className="card-title">Card title</h5>
                    <form>
                        <div className="form-group">
                            <label for="exampleInputEmail1">Username</label>
                            <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" />
                            {/* <small id="emailHelp" className="form-text text-muted">We'll never share your email with anyone else.</small> */}
                        </div>
                        <div className="form-group">
                            <label for="exampleInputPassword1">Password</label>
                            <input type="password" className="form-control" id="exampleInputPassword1" placeholder="Password" />
                        </div>
                        {/* <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="exampleCheck1" />
                            <label class="form-check-label" for="exampleCheck1">Check me out</label>
                        </div> */}
                        <button type="submit" class="btn btn-primary login-btn">Login</button>
                    </form>
                </div>
            </div>
        </div>

    </>
}