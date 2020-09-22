import React from 'react';
import ReactDOM, { render } from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import { Index } from './Index';
import { Comments } from './Comments';
import { Sidebar } from './Sidebar';
import { Settings } from './Settings';
import { Profile } from './Profile';
import { UserList } from './UserList';

function App() {
  return (
    <BrowserRouter>
      <main>
        <Sidebar />
        <Switch>
          <Route path='/' component={Index} exact />
          <Route path='/post/:id/comments/' component={Comments} exact />
          <Route path='/settings/' component={Settings} exact />
          <Route path='/profile/:id/' component={Profile} exact />
          <Route path='/followers/:id/' render={(props) => (<UserList {...props} followers={true} />)} exact />
          <Route path='/following/:id/' render={(props) => (<UserList {...props} followers={false} />)} exact />

          <Route component={Error} />
        </Switch>
      </main>
    </BrowserRouter>
  )
}

export default App;

const container = document.getElementById('app');
render(<App />, container);