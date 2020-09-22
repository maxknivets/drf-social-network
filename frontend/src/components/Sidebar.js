import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

import styles from './App.css';
import Cookies from 'js-cookie';

export function Sidebar() {

  const [currentAuthenticatedUserId, setCurrentAuthenticatedUserId] = useState(1);

  useEffect(() => {
    fetch(`/api/get-current-authenticated-user-id/`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': Cookies.get('sessionid'),
      },
    })
      .then(response => { return response.json() })
      .then(data => { setCurrentAuthenticatedUserId(data.current_authenticated_user_id) })
  }, [])

  return (
    <div className="sidebars">
      <div className={styles.leftSidebar}>
        <div className={styles.content}>
          <div>
            <div>
              <br />
              <a className="btn btn-primary btn-block" href="/" role="button">Home</a>
              <br />
              <a className="btn btn-primary btn-block" href={`/profile/${currentAuthenticatedUserId}`} role="button">Your profile</a>
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