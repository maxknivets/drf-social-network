import React from 'react';
import ReactDOM from 'react-dom';

export function Sidebar() {
    return (
        <div className="sidebars">
            <div className="left-sidebar">
                <div className="content">
                    <div>
                        <div>
                            <br />
                            <a className="btn btn-primary btn-block" href="/" role="button">Home</a>
                            <br />
                            <a className="btn btn-primary btn-block" href={`/user/`} role="button">Your profile</a>
                            <br />
                            <a className="btn btn-primary btn-block" href="/settings" role="button">Settings</a>
                            <br />
                            <a className="btn btn-primary btn-block" href="/logout" role="button">Log out</a>
                        </div>
                    </div>
                </div>
            </div>
            <div className="right-sidebar">
                <div className="content">
                    <br />
                    <button className="btn btn-primary btn-sm">#POLITICS</button>
                    <button className="btn btn-primary btn-sm">#GAMES</button>
                    <button className="btn btn-primary btn-sm">#BOREDOM</button>
                    <button className="btn btn-primary btn-sm">#WORK</button>
                    <button className="btn btn-primary btn-sm">#HEALTHCARE</button>
                    <button className="btn btn-primary btn-sm">#ART</button>
                    <button className="btn btn-primary btn-sm">#MOTIVATION</button>
                    <button className="btn btn-primary btn-sm">#CATS</button>
                    <button className="btn btn-primary btn-sm">#MUSIC</button>
                    <button className="btn btn-primary btn-sm">#HOME</button>
                </div>
            </div>
        </div>
    )
}