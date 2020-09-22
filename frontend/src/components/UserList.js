import React, { Component, useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import Cookies from 'js-cookie';
import classnames from 'classnames'
import styles from './App.css';

export function UserList(props) {
  const profileId = parseInt(props.match.params.id);
  const url = props.followers ? 'followers': 'following';
  const [userList, setFollowersList] = useState(
    [{
      "user": {
        "id": null,
        "username": null,
      },
      "is_followed_by": {
        "id": null,
        "username": null,
      },
  }]);
  
  useEffect(() => {
    fetch(`/api/${url}/${profileId}/`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': Cookies.get('sessionid'),
        'X-CSRFToken': Cookies.get('csrftoken')
      },
      method: "GET",
    })
      .then(response => { return response.json() })
      .then(data => { setFollowersList(data) })
  }, [])
  return (
    <ul className={styles.homecenter}>
      { props.followers ?
        userList.map(follower =>
          <li key={follower.is_followed_by.id}>
            <a href={`/profile/${follower.is_followed_by.id}`}>
              {follower.is_followed_by.username}
            </a>
          </li>
        )
        :
        userList.map(follower =>
          <li key={follower.user.id}>
            <a href={`/profile/${follower.user.id}`}>
              {follower.user.username}
            </a>
          </li>
        )
      }
    </ul>
  )
}