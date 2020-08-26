import React from 'react';
import ReactDOM from 'react-dom';

export function Sidebar() {
    return (
        <div>
            <div class="left-sidebar">
                <div class="content">
                    <div>
                        <div>
                            <br />
                            <a class="btn btn-primary btn-block" href="/" role="button">Home</a>
                            <br />
                            <a class="btn btn-primary btn-block" href="/user/{{ user.pk }}" role="button">Your profile</a>
                            <br />
                            <a class="btn btn-primary btn-block" href="/settings" role="button">Settings</a>
                            <br />
                            <a class="btn btn-primary btn-block" href="/logout" role="button">Log out</a>
                        </div>
                    </div>
                </div>
            </div>
        <div class="right-sidebar">
            <div class="content">
                <br />
                <button class="btn btn-primary btn-sm">#POLITICS</button>
                <button class="btn btn-primary btn-sm">#GAMES</button>
                <button class="btn btn-primary btn-sm">#BOREDOM</button>
                <button class="btn btn-primary btn-sm">#WORK</button>
                <button class="btn btn-primary btn-sm">#HEALTHCARE</button>
                <button class="btn btn-primary btn-sm">#ART</button>
                <button class="btn btn-primary btn-sm">#MOTIVATION</button>
                <button class="btn btn-primary btn-sm">#CATS</button>
                <button class="btn btn-primary btn-sm">#MUSIC</button>
                <button class="btn btn-primary btn-sm">#HOME</button>
                </div>
            </div>
        </div>
    )
}