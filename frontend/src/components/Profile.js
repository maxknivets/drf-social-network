import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom';
import Cookies from 'js-cookie';
import classnames from 'classnames'

import styles from './App.css';
import { FollowButton } from './Misc'

export function Profile(props) {
  const profileId = parseInt(props.match.params.id);

  const [userInfo, setUserInfo] = useState({
    "user_id": null,
    "username": null,
    "first_name": null,
    "last_name": null,
    "bio": null,
    "location": null,
    "total_followers": null,
    "total_followed": null,
    "user_info": null,
  });

  useEffect(() => {
    fetch(`/api/profile/${profileId}/`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': Cookies.get('sessionid'),
      },
    })
      .then(response => { return response.json() })
      .then(data => { setUserInfo(data) })
  }, [])

  return (
    <div>
      <div className={styles.userInfoCentered}>
        <div className={styles.userPfp}>
          {
            (userInfo.profile_picture)
            ? <img className={styles.pfp} src={`/media/${ userInfo.profile_picture }`} alt={ `${userInfo.username}'s profile picture` } />
            : <img className={styles.pfp} src={`/static/icons/user.svg`} alt={ `${userInfo.username}'s profile picture` } />
          }
        </div>
  
        <div className={styles.userInfoBox}>

          <div className="font-weight-bold">
            { userInfo.username }
          </div>

          <div>
            { userInfo.first_name } { userInfo.last_name }
          </div>

          <div>
            <img className={styles.userInfoLocation} src="/static/icons/location.svg" />
            {
              (userInfo.location)
              ? <span> {userInfo.location} </span>
              : <span> The Earth </span>
            }
          </div>

          <div>
            following: <a href={`/following/${ userInfo.user_id }`} id="following">{ userInfo.following_count }</a>
            <br />
            followers: <a href={`/followers/${ userInfo.user_id }`} id="followers">{ userInfo.followers_count }</a>
          </div>

          <div className={styles.userInfoBio}>
            {
              (userInfo.bio)
              ? <span> {userInfo.bio} </span>
              : <span className="secondary"> Bio mising </span>
            }
          </div>

          <div>
            <div className={classnames(styles.center, styles.userInfoPostsMargin)}>
              {
                (!userInfo.profile_belongs_to_authenticated_user)
                ? <FollowButton followStatus={userInfo.follow_status} profileId={profileId} />
                : <button className="btn btn-secondary btn-sm" disabled> Can't follow yourself </button>
              }
            </div>
          </div>
        </div>
      <div className="border-bottom border-dark"></div>
      </div>
    </div>
  )
}