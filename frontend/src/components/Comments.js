import React from 'react';
import ReactDOM from 'react-dom';

import { Posts, QuerySinglePost } from './Post'

export function Comments(props) {

  const postId = parseInt(props.match.params.id);


  return (
    <div>
      <div className="homecenter">
        <QuerySinglePost props={props} id={postId} />
      </div>
      <div className="homecenter comment-separator">
        <Posts url={`/api/post/retrieve-comments/${postId}/`} />
      </div>
    </div>
  );

}
