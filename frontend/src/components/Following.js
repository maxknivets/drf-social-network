import React, { Component, useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import Cookies from 'js-cookie';

export function Following(props) {
  const profileId = parseInt(props.match.params.id);

  const [list, setFollowingList] = useState(
    [{
      "id": null,
      "username": null,
    }]);
  
  useEffect(() => {
    fetch(`/api/following/${profileId}/`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': Cookies.get('sessionid'),
        'X-CSRFToken': Cookies.get('csrftoken')
      },
      method: "GET",
    })
      .then(response => { return response.json() })
      .then(data => { setFollowingList(data)
        debugger;
      })
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