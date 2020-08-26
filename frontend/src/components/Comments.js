import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import Cookies from 'js-cookie';

import { Posts, Post } from './Post'

export function Comments(props) {
    const [post, setPost] = useState();
  
    useEffect (() => {
      fetch(`/api/post/get/${props.match.params.id}/`, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': Cookies.get('sessionid'),
        },
      })
      .then(response => {return response.json()})
      .then(data => {setPost({"post": data})})
    }, []);

    return (
        <div>
            <Posts post={post} />
            <Posts url={`/api/post/retrieve-comments/${props.match.params.id}/`}/>
        </div>
    );
}
