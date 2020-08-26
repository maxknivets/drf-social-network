import React from 'react';
import ReactDOM from 'react-dom';
import Cookies from 'js-cookie';
import $ from 'jquery';
import { Component, useState, useEffect } from 'react';

export function ToggleFormButton(props) {
  
    function handleClick(e) {
        $(`#${props.formId}-${props.post.id}`).toggle()
    }
  
    return (
        <button className={`btn btn-sm ${props.classname}`} onClick={handleClick}>
            <img className='icon' alt={props.icon} src={`/static/icons/${props.icon}.svg`} />
        </button>
    )

}

export class TextForm extends Component {
    
    constructor(props){
      super(props)
      this.state = {
        value: '',
      };
      this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handleChange(event) {
      this.setState({ value: event.target.value });
    };
  
    handleSubmit(event) {
      event.preventDefault();
      var defaultData = {'text': this.state.value, 'posted_by': 1}// fix this later
      if (this.props.additionalData) {
        defaultData = Object.assign({}, defaultData, this.props.additionalData)
      }

      fetch(this.props.url, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': Cookies.get('sessionid'),
          'X-CSRFToken': Cookies.get('csrftoken')
        },
        method: this.props.method,
        body: JSON.stringify(defaultData)
      })
        .then(response => {return response.json()})
        .then(data => this.setState({posts: data}))
      }
    
    render() {
      return (
        <div className={this.props.divClass} id={this.props.divId}>
          <form onSubmit={this.handleSubmit}>
            <label>
              {this.props.label}
              <textarea className={`form-control my-3 ${this.props.formClass}`} type='text' value={this.state.value} onChange={this.handleChange} cols='90' rows='3' required />
            </label>
            <button className='form-control btn btn-primary' type='submit'>{this.props.buttonValue}</button>
          </form>
        </div>
      );
    }

}  

export function MiscellaneousCountButton(props) {
    
    const [count, setCount] = useState(0);
  
    useEffect(() => {
        fetch(props.fetchURL, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': Cookies.get('sessionid'),        
            },
        })
        .then(response => {return response.json()})
        .then(data => {setCount(Object.values(data)[0]);});
    }, []);
  
    return (
        <a href={props.buttonURL} className={props.buttonClass}>
            <img className='icon' alt={props.icon} src={`/static/icons/${props.icon}.svg`} />
            <span id={props.id}> {count}</span>
        </a>
    )
  
}

export function LikeButton(props) {

    const [rating, setRating] = useState(0);
  
    useEffect(() => {
      fetch(`/api/post/rating/${props.post.id}/`, {
        headers: {
          'Content-Type': 'application/json',
              'Authorization': Cookies.get('sessionid'),
        },
      })
        .then(response => {return response.json();})
        .then(data => {setRating(props.like ? data.total_likes : data.total_dislikes)});
    }, []);
  
    function handleClick(e) {
      fetch('/api/post/rate/', {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': Cookies.get('sessionid'),
          'X-CSRFToken': Cookies.get('csrftoken')
        },
        method: 'POST',
        body: JSON.stringify({'liked': props.like, 'rated_post': props.post}),
      })
      .then(response => {return response.json();})
      .then(data => {
        setRating(props.like ? data.total_likes : data.total_dislikes);
        $(`#total-post-likes-${props.post.id}`).text(data.total_likes);
        $(`#total-post-dislikes-${props.post.id}`).text(data.total_dislikes);
      })
    }
  
    var buttonClass = props.like ? 'btn-outline-success': 'btn-outline-secondary';
    var idName = props.like ? 'total-post-likes' : 'total-post-dislikes';
    var icon = props.like ? 'thumbs-up' : 'thumbs-down';
  
    return (
      <button className={`btn btn-sm ${buttonClass}`} onClick={handleClick}>
        <img className='icon' alt={icon} src={`/static/icons/${icon}.svg`} />
        <span id={`${idName}-${props.post.id}`}>{rating}</span>
      </button>
    )

}

export function DeleteButton(props) {

    function handleClick(e) {
        fetch(`/api/post/delete/${props.post.id}/`, {
            headers: {
                'Authorization': Cookies.get('sessionid'),
                'X-CSRFToken': Cookies.get('csrftoken')
            },
            method: 'DELETE',
            body: JSON.stringify({id:props.post.id}),
        })
        .then(response => {
            $(`#post-${props.post.id}`).remove();
            return response.json();
        });
    };
    
    return (
      <div className='hidden my-2 text-left' id={`delete-post-${props.post.id}`}>
        <button className='btn btn-danger' onClick={handleClick}>Delete Post <br /><small>this action is irreversible</small></button>
      </div>
    )
  
}