import React, { Component, useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import Cookies from 'js-cookie';
import classnames from 'classnames'

import { TextForm, MiscellaneousCountButton, ToggleFormButton, DeleteButton, LikeButton } from './Misc';
import styles from './App.css';

export class Posts extends Component {
  constructor(props) {
    super(props)
    this.state = {
      posts: [],
    };
    this.getPosts = this.getPosts.bind(this)
    this.getPosts();
  }

  getPosts() {
    fetch(this.props.url, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': Cookies.get('sessionid')
      }
    })
      .then(response => { return response.json() })
      .then(data => {
        this.setState({ posts: data })
      })
  }

  render() {
    return (
      <ul>
        {this.state.posts.map(post =>
          <li key={post.id}><Post post={post} /></li>
        )}
      </ul>
    )
  }
}

export function QuerySinglePost(props) {
  const [post, setPost] = useState(
    {
      "id": null,
      "post_belongs_to_user": null,
      "posted_by": {
        "id": null,
        "username": null
      },
      "pub_date": null,
      "text": null,
      "image": null,
      "likes_count": null,
      "dislikes_count": null,
      "comments_count": null
    });

  useEffect(() => {
    fetch(`/api/post/${props.id}/`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': Cookies.get('sessionid'),
      },
    })
      .then(response => { return response.json() })
      .then(data => { setPost(data) })
  }, [])

  return (
    <div className={styles.indexPosts}>
      <Post props={undefined} post={post} />
    </div>
  )
}

export function Post(props) {
  return (
    <div className={classnames(styles.post, styles.separator)} id={`post-${props.post.id}`}>
      <p className={styles.postText} id='post-text'>{props.post.text}</p>

      {props.post.image && // this is for later
        <img className='img-fluid' src={`${props.post.image.url}`} alt='post-image' />
      }

      <span className='text-left' id="post-header">
        <a href={`/profile/${props.post.posted_by.id}/`}>{props.post.posted_by.username}</a>
        <span className={styles.postDate} id="post-date"> {props.post.pub_date} </span>
      </span>

      <PostOptionsJSX post={props.post} />
    </div>
  )
}

export function PostOptionsJSX(props) {
  return (
    <span>
      <LikeButton post={props.post} like={true} />
      <LikeButton post={props.post} like={false} />
      <MiscellaneousCountButton buttonURL={`/post/${props.post.id}/comments/`} buttonClass={'btn btn-sm btn-outline-primary'} icon={'comment'} id={`post-comment-count-${props.post.id}`} count={props.post.comments_count} />
      <EditDeleteCommentButtons post={props.post} />
      <EditDeleteCommentForms post={props.post} />
    </span>
  );
}


export function EditDeleteCommentButtons(props) {
  return (
    <span>
      {props.post.post_belongs_to_authenticated_user && 
        <span>
          <ToggleFormButton post={props.post} formId='edit-post' icon='pencil-alt' classname='btn-outline-primary' />
          <ToggleFormButton post={props.post} formId='delete-post' icon='trash-alt' classname='btn-outline-danger' />
        </span>
      }
      <ToggleFormButton post={props.post} formId='comment-on-post' icon='arrow-down' classname='btn-outline-primary' />
    </span>
  )
}

export function EditDeleteCommentForms(props) {
  return (
    <div>
      {props.post.post_belongs_to_authenticated_user && 
        <span>
          <TextForm url={`/api/post/${props.post.id}/`} method={'PATCH'} label={<p>Edit post</p>} formClass={'btn-block'} buttonValue={'Edit post'} divClass='hidden my-2 text-left' divId={`edit-post-${props.post.id}`} />
          <DeleteButton post={props.post} />
        </span>
      }
      <TextForm url={'/api/post/'} method={'POST'} additionalData={{ 'in_reply_to_post': props.post.id }} label={<p>Comment</p>} formClass={'btn-block'} buttonValue={'Comment'} divClass={'hidden my-2 text-left'} divId={`comment-on-post-${props.post.id}`} />
    </div>
  )
}