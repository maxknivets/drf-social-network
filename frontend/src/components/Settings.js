import React, { Component, useState } from 'react';
import ReactDOM from 'react-dom';

import Cookies from 'js-cookie';
import classnames from 'classnames'
import styles from './App.css';

export function Settings(props) {
  return (
    <div>
      <Form />
    </div>
  )
}
function Form() {
  const [state, setState] = useState({
    first_name: "",
    last_name: "",
    bio: "",
    location: "",
  })
  function handleChange(event) {
    const value = event.target.value;
    setState({
      ...state,
      [event.target.name]: value
    });
  };

  function handleSubmit(event) {
    event.preventDefault();
    fetch(`/api/profile/`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': Cookies.get('sessionid'),
        'X-CSRFToken': Cookies.get('csrftoken')
      },
      method: 'PATCH',
      body: JSON.stringify(state)
    })
      .then(response => { return response.json() })
      .then(data => setState({ fetchData: data }))
  }

  return (
    <div className={styles.homecenter}>
      <form onSubmit={handleSubmit}>
        <label>
          Your first name
          <textarea name="first_name" className={`form-control my-3`} value={state.first_name} onChange={handleChange} />
        </label>
        <br />
        <label>
          Your second name
          <textarea name="last_name" className={`form-control my-3`} value={state.last_name} onChange={handleChange} />
        </label>
        <br />
        <label>
          Your bio
          <textarea name="bio" className={`form-control my-3`} value={state.bio} onChange={handleChange} />
        </label>
        <br />
        <label>
          Your location
          <textarea name="location" className={`form-control my-3`} value={state.location} onChange={handleChange} />
        </label>
        <button className='form-control btn btn-primary' type='submit'>Change</button>
      </form>
    </div>
  )
}

export class ProfileChangeForms extends Component {

  constructor(props) {
    super(props)
    this.state = {
      firstName: "",
      lastName: "",
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    const value = event.target.value;
    this.setState({
      ...this.state,
      [event.target.name]: value
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
      <div className={styles.homecenter}>
        <form onSubmit={this.handleSubmit}>
          <label>
            Your first name
            <textarea className={`form-control my-3`} type='text' value={this.state.firstName} onChange={this.handleChange} cols='90' rows='3' required />
          </label>
          <br />
          <label>
            Your second name
            <textarea className={`form-control my-3`} type='text' value={this.state.secondName} onChange={this.handleChange} cols='90' rows='3' required />
          </label>
          <br />
          <label>
            Your bio
            <textarea className={`form-control my-3`} type='text' value={this.state.bio} onChange={this.handleChange} cols='90' rows='3' required />
          </label>
          <br />
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
