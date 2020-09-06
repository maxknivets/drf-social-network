import React from 'react';
import ReactDOM from 'react-dom';
import { Component, useState, useEffect } from 'react';

export function Settings(props) {
  return (
    <div>
      <MultipleTextForms />
    </div>
  )
}

export class MultipleTextForms extends Component { // not making this a reusable component because no need + time consuming

  constructor(props) {
    super(props)
    this.state = {
      firstName: "",
      lastName: "",
      bio: "",
      location: "",
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    const value = event.target.value;
    setState({
      ...this.state,
      [evt.target.name]: value
    });
  };

  handleSubmit(event) {
    event.preventDefault();
    fetch(`/profile/change/`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': Cookies.get('sessionid'),
        'X-CSRFToken': Cookies.get('csrftoken')
      },
      method: 'POST',
      body: JSON.stringify(defaultData)
    })
      .then(response => { return response.json() })
      .then(data => this.setState({ fetchData: data }))
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Your first name
            <textarea className={`form-control my-3`} type='text' value={this.state.firstName} onChange={this.handleChange} cols='90' rows='3' required />
          </label>
          <label>
            Your second name
            <textarea className={`form-control my-3`} type='text' value={this.state.secondName} onChange={this.handleChange} cols='90' rows='3' required />
          </label>
          <label>
            Your bio
            <textarea className={`form-control my-3`} type='text' value={this.state.bio} onChange={this.handleChange} cols='90' rows='3' required />
          </label>
          <label>
            Your location
            <textarea className={`form-control my-3`} type='text' value={this.state.location} onChange={this.handleChange} cols='90' rows='3' required />
          </label>
          <button className='form-control btn btn-primary' type='submit'>Change</button>
        </form>
      </div>
    );
  }

}
