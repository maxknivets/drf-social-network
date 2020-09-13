import React from 'react';
import ReactDOM from 'react-dom';
import classnames from 'classnames'

import styles from './App.css';

export function Sidebar() {
  var placeholder = 1
  
  return (
    <div className="sidebars">
      <div className={styles.leftSidebar}>
        <div className={styles.content}>
          <div>
            <div>
              <br />
              <a className="btn btn-primary btn-block" href="/" role="button">Home</a>
              <br />
              <a className="btn btn-primary btn-block" href={`/profile/${placeholder}`} role="button">Your profile</a>
              <br />
              <a className="btn btn-primary btn-block" href="/settings" role="button">Settings</a>
              <br />
              <a className="btn btn-primary btn-block" href="/logout" role="button">Log out</a>
            </div>
          </div>
        </div>
      </div>
      <div className={styles.rightSidebar}>
        <div className={styles.content}>
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