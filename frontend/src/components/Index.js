import React from 'react';
import ReactDOM from 'react-dom';
import classnames from 'classnames'

import { Posts } from './Post'
import { TextForm } from './Misc'

import styles from './App.css';

export function Index() {
  return (
    <div className={styles.homepage}>
      <div className={styles.homecenter}>
        <TextForm url={'/api/post/'} method={'POST'} post={true} label={<p>Publish post</p>} formClass={'post-input'} buttonValue={'Publish'} />
      </div>
      <div className={classnames(styles.homecenter, styles.separator )}>
        <Posts url={'/api/post/'} />
      </div>
    </div>
  );
}