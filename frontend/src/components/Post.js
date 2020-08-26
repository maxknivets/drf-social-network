import React from 'react';
import ReactDOM from 'react-dom';
import Cookies from 'js-cookie';
import { Component } from 'react';

import {TextForm, MiscellaneousCountButton, ToggleFormButton, DeleteButton, LikeButton} from './Misc';

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
      .then(response => {return response.json()})
      .then(data => {
        if (this.props.postId) {
          debugger;
          data = data[0]
        }
        this.setState({posts: data})
        
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
  

export function Post(props) {
    return (
        <div className='post' id={`post-${props.post.id}`}>
            <p className='post-text' id='post-text'>{props.post.text}</p>
            <a href={`/user/${props.post.posted_by.id}/`}>{props.post.posted_by.username}</a> 
            {props.post.image &&
                <img className='img-fluid' src={`${props.post.image.url}`} alt='post-image' />
            }
  
            <span className='text-left'>
                <span className='post-date'> { props.post.pub_date } </span>
                <PostOptionsJSX post={props.post} />
            </span>
        </div>
    )
}

export function PostOptionsJSX(props) {
    return (
        <div>
            <LikeButton post={props.post} like={true} />
            <LikeButton post={props.post} like={false} />

            <MiscellaneousCountButton fetchURL={`/api/post/comment-count/${props.post.id}/`} buttonURL={`/post/${props.post.id}/comments/`} buttonClass={'btn btn-sm btn-outline-primary'} icon={'comment'} id={`post-comment-count-${props.post.id}`} />

            <EditDeleteButtons post={props.post} />
            <ToggleFormButton post={props.post} formId='comment-on-post' icon='arrow-down' classname='btn-outline-primary' />

            <EditDeleteCommentForms post={props.post} />
        </div>
    );
}


export function EditDeleteButtons(props) {
    //const sessionUser = genericAJAXRequest('api/get-user/', 'GET', undefined)
  
    // query user info and check with the session user
  
    return (
        <span>
            <ToggleFormButton post={props.post} formId='edit-post' icon='pencil-alt' classname='btn-outline-primary' />
            <ToggleFormButton post={props.post} formId='delete-post' icon='trash-alt' classname='btn-outline-danger' />
        </span>
    )
}

export function EditDeleteCommentForms(props) {

    //const sessionUser = genericAJAXRequest('api/get-user/', 'GET', undefined)
  
    return (
    
        <div>
          
            <TextForm url={`/api/post/edit/${props.post.id}/`} method={'PUT'} additionalData={{'id':props.post.id}} label={<p>Edit post</p>} formClass={'btn-block'} buttonValue={'Edit post'} divClass='hidden my-2 text-left' divId={`edit-post-${props.post.id}`} />

            <DeleteButton post={props.post} />

            <TextForm url={'/api/post/'} method={'POST'} additionalData={{'in_reply_to_post':props.post.id}} label={<p>Comment</p>} formClass={'btn-block'} buttonValue={'Comment'} divClass={'hidden my-2 text-left'} divId={`comment-on-post-${props.post.id}`} />  
        
        </div>

    )
}