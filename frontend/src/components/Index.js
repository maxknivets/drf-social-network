import React from 'react';
import ReactDOM from 'react-dom';

import { Posts } from './Post'
import { TextForm } from './Misc'

export function Index() {
  return (
    <div>
      <div className="homecenter">
        <TextForm url={'/api/post/'} method={'POST'} post={true} label={<p>Publish post</p>} formClass={'post-input'} buttonValue={'Publish'} />
      </div>
      <div className="homecenter">
        <Posts url={'/api/post/retrieve-posts/'}/>
      </div>
    </div>
  );
}