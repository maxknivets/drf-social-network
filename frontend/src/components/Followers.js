import React, { Component, useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import Cookies from 'js-cookie';

export function Followers(props) {
  const profileId = parseInt(props.match.params.id);

  const [list, setFollowersList] = useState(
    [{
      "id": null,
      "username": null,
    }]);
  
  useEffect(() => {
    fetch(`/api/followers/${profileId}/`, {
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
    <ul>
      {list.map(follower =>
        <li key={follower.id}>
          <a href={`/profile/${follower.id}`}>
            {follower.username}
          </a>
        </li>
      )}
    </ul>
  )
}