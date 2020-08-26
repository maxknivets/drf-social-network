import React from 'react';
import ReactDOM, { render } from 'react-dom';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { Index } from './Index'
import { Comments } from './Comments'
import { Sidebar } from './Sidebar'

function App() {
  return (
    <BrowserRouter>
      <main>
        <Sidebar />
        <Switch>
          <Route path='/' component={Index} exact />
          <Route path='/post/:id/comments/' component={Comments} exact />
          <Route component={Error} />
        </Switch>
      </main>
    </BrowserRouter>
  )
}



export default App;

const container = document.getElementById('app');
render(<App />, container);