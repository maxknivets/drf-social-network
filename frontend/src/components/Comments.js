import React from 'react';
import ReactDOM from 'react-dom';

import { Posts, QuerySinglePost } from './Post'

import styles from './App.css';

export function Comments(props) {
  const postId = parseInt(props.match.params.id);

  return (
    <div>
      <div className={styles.homecenter}>
        <QuerySinglePost props={props} id={postId} />
      </div>
      <div className={styles.homecenter}>
        <Posts url={`/api/post/retrieve-comments/${postId}/`} />
      </div>
    </div>
  );
}
