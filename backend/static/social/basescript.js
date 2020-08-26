function genericAJAXRequest(url, method, data) {
	$.ajax({
	  url: url,
	  headers: { 
		'Content-Type': 'application/json',
		'Authorization': Cookies.get('sessionid'),
		'X-CSRFToken': Cookies.get('csrftoken'),
	  },
	  method: method,
	  data: JSON.stringify(data),
	  success: (request) => {
		return request;
	  },
	});
};

function rate(post_id, like) {
	var url = (like ? `/ajax/like/${post_id}` : `/ajax/dislike/${post_id}`);
	var data = genericAJAXRequest(url, "get", undefined);
	$(`#total_likes_${post_id}`).text(data.total_likes);
	$(`#total_dislikes_${post_id}`).text(data.total_dislikes);
};

function followUser(user_id) {
	$.ajax({
		url: '/ajax/follow/',
		data: { id: user_id },
		dataType: 'json',
		success: function (data) {
			$(`#follow`).text(data.status);
			$(`#followers`).text(data.count);
			console.log('success');
		},
		error: function() {
			console.log('error!');
		}
	});
};    



function bioChange() {
	event.preventDefault();
	var firstName = $(`#first-name-field`).val();
	var lastName = $(`#last-name-field`).val();
	var bio = $(`#bio-field`).val();
	var location = $(`#location-field`).val();
	$.ajax({
		url: '/ajax/settings/',
		data: { csrfmiddlewaretoken: profileChangeToken, first_name: firstName, last_name: lastName, bio: bio, location: location },
		dataType: 'json',
		type: 'POST',
		success: function (data) {
			$('#first-name-field').val('');
			$('#last-name-field').val('');
			$('#bio-field').val('');
			$('#location-field').val('');
			$('#first_name').text(data.first_name);
			$('#last_name').text(data.last_name);
			$('#bio').text(data.bio);
			$('#location').text(data.location)
			console.log('success');
		},
		error: function() {
			console.log('error!');
		}
	});
}


 
function changeProfilePicture() {
	$.ajax({
		url:`/ajax/changepfp`,
		dataType:'json',
		type:'GET',
		success: function (data) {
			console.log('bruh')
		}
	});
}


/*

function editPost(post_id) {
	event.preventDefault();
	var text=$('#edit-field').val()
	$.ajax({
		url: '/ajax/edit/'+post_id+'/',
		data: { csrfmiddlewaretoken: postEditToken, id: post_id, new_text: text },
		dataType: 'json',
		success: function (data) {
			$(`#post_text${post_id}`).text(data.new_text);
			toggleVisibility(`edit${post_id}`)
			console.log('success');
		},
		error:function (xhr, ajaxOptions, thrownError){
			if(xhr.status==404) {
				alert("Something went wrong. Probably the post has been deleted.");
				$("#posts li").filter(`#post${post_id}`).remove()
			}
		}
	});
};



function deletePost(post_id) {
	event.preventDefault() 
	$.ajax({
		url: '/ajax/delete/'+post_id+'/',
		success: function () {
			$(`#post${post_id}`).remove();
			console.log('success');
		},
		error:function (xhr, ajaxOptions, thrownError){
			if(xhr.status==404) {
				alert("Something went wrong. Probably the post has been deleted.");
				$("#posts li").filter(`#post${post_id}`).remove()
			}
		}	
	});
};
    


function commentInReply(post_id, comment_id=false) {
	event.preventDefault();
	var text=$(`#comment_in_reply${post_id} #comment-field`).val()
	comment_data={ 'csrfmiddlewaretoken': commentToken, 'id': post_id, 'comment': text, 'in_reply_to_user': 0, 'in_reply_to_comment': 0 }
	if (comment_id) {
		comment_data['comment'] = $(`#comment_in_reply${comment_id} #comment-field`).val();
		comment_data['in_reply_to_user'] = $(`#in_reply_to_user${comment_id}`).val();
		comment_data['in_reply_to_comment'] = $(`#in_reply_to_comment${comment_id}`).val();
	}
	$.ajax({
		url: '/ajax/comment/',
		data: comment_data,
		dataType: 'json',
		type: 'POST',
		success: function (data) {
			var post_id=data.post_id;
			var comment_text=data.comment_text;
			var comment_id=data.comment_pk;
			var comment_posted_by=data.posted_by;
			var comment_posted_by_id=data.posted_by_id;
			var comment_type='comment';
			var user_id=data.user_id;
			var post_date=data.date;
			var in_reply_to_user=data.in_reply_to_user;
			var in_reply_to_comment=data.in_reply_to_comment;
			if (in_reply_to_user && in_reply_to_comment) {
				$(`#comment_in_reply${in_reply_to_comment} #comment-field`).val('');
				var get_username=data.get_username;
				var reply=`in reply to <a href="/user/${in_reply_to_user}">${get_username}</a>\'s <a href="/${in_reply_to_comment}/showcomment">comment</a>`;
				var comment_type='inreply';
			}
			else {
				$(`#comment_in_reply${post_id} #comment-field`).val('');
				reply=``;
			}
			$(`#comment_section${post_id}`).append(`

<li class="${comment_type}" id="comment${comment_id}"><div class="comment" id="comment_text${comment_id}">${comment_text}</div><img class="reply" alt="down" src="/static/icons/arrow-down.svg" onclick="toggleVisibility('comment_in_reply${comment_id}');">

<img class="reply" alt="delete" src="/static/icons/trash-alt.svg" onclick="toggleVisibility('delete_comment${comment_id}');">
<img class="reply" src="/static/icons/pencil-alt.svg" onclick="toggleVisibility('edit_comment${comment_id}');">

<div class="commentsub"> commented by <a href="/user/${user_id}">${comment_posted_by}</a>${reply}<small><br> Posted on ${post_date}</small></div>

<span class="changenone" id="delete_comment${comment_id}"><strong class="stronger">Delete the comment? </strong><button class="coolButton" onclick="deleteComment(${comment_id})">Yes, delete it.</button></span>

<span class="changenone" id="edit_comment${comment_id}">
<form onsubmit="editComment(${comment_id})">
New text: <input type="text" placeholder="Edit here" minlength="1" maxlength="2500"  id="edit-field" value="${comment_text}">
<input type="submit" value="edit">
</form>
</span>


<span class="none" id="comment_in_reply${comment_id}">
<form onsubmit="commentInReply(${post_id}, ${comment_id})">
<input type="hidden" id="in_reply_to_user${comment_id}" value="${user_id}">
<input type="hidden" id="in_reply_to_comment${comment_id}" value="${comment_id}">
<label for="comment-field">Comment:</label><input type="text" minlength="1" maxlength="2500" id="comment-field" placeholder="What do you think?">
<input type="submit" value="comment">
</form>
</span>
</li>

`);
		console.log('success');
		},
		
		error:function (xhr, ajaxOptions, thrownError){
			if(xhr.status==404) {
				alert("Something went wrong. Probably the post has been deleted.");
				$("#posts li").filter(`#post${post_id}`).remove()
			}
		}        
	});
};



function editComment(comment_id) {
	event.preventDefault();
	var text=$(`#edit_comment${comment_id} #edit-field`).val();
	$.ajax({
		url: '/ajax/commentedit/',
		data: { csrfmiddlewaretoken: commentEditToken, id: comment_id, new_text: text },
		dataType: 'json',
		type: 'POST',
		success: function (data) {
			toggleVisibility(`edit_comment${comment_id}`)
			$(`#comment_text${comment_id}`).text(data.new_text);
			console.log('success');
		},
		error: function() {
			console.log('error!');
		}
	});
};



function deleteComment(comment_id) {
	$.ajax({
		url: '/ajax/commentdelete/',
		data: { id: comment_id },
		dataType: 'json',
		success: function (data) {
			$(`#comment${comment_id}`).remove();
			console.log('success');
			},
		error: function() {
			console.log('error!');
		}
	});
};    


function renderPost(data){
	var post_text=data.post_text;
	var post_date=data.post_date;
	var post_id=data.post_id;
	var post_username=data.username;
	var post_user_id=data.user_id;
	var post_image=""
	if (data.image) {
		var post_image=`<img src="${data.image}" alt="post-image${data.post_id}">`
	}
	$('#posts').prepend(`

<li id="post${post_id}"><div class="main" id="post_text${post_id}">${post_text}</div>${post_image}<div class="sub">Posted by <a href="/user/${post_user_id}">${post_username}</a> on ${post_date}</div>

<img class="main" onclick="like(${post_id}, ${this.postToken})" alt="like" src="static/icons/thumbs-up.svg"><div id="total_likes${post_id}" class="like">0</div>
<img class="main" onclick="dislike(${post_id}, ${this.postToken})" alt="dislike" src="/static/icons/thumbs-down.svg"><div id="total_dislikes${post_id}" class="dislike">0</div>

<img class="main" src="/static/icons/pencil-alt.svg" onclick="toggleVisibility('edit${post_id}');">
<img class="main" alt="delete" src="/static/icons/trash-alt.svg" onclick="toggleVisibility('delete${post_id}');">

<span class="changenone" id="delete${post_id}"><strong class="stronger">Delete the post?</strong><button class="coolButton" onclick="deletePost(${post_id})">Yes, delete it.</button></span>

<span class="changenone" id="edit${post_id}">
<form onsubmit="editPost(${post_id})">
<input type="hidden" id="edit-id" value="${post_id}">
<label for="edit-field">New text:</label> <input type="text" placeholder="Edit here" minlength="1" maxlength="2500" id="edit-field" value="${post_text}">
<input type="submit">
</form>
</span>

<span class="extrapadding" id="comment_in_reply${post_id}">
<form onsubmit="commentInReply(${post_id})">
<label for="comment-field">Comment:</label> <input type="text" minlength="1" maxlength="2500" id="comment-field" placeholder="What do you think?">
<input type="submit" value="comment">
</form>
</span>

<ul id="comment_section${post_id}"></ul>

`);
console.log("success");
}

function createPostWithImage() {
	var image=$('#id_post_image')[0].files[0];
	var text=$('#post-field').val();
	var formData = new FormData();
	formData.append('post_text', text)
	formData.append('image', image);
	formData.append('csrfmiddlewaretoken', postToken)
	$.ajax({
		url: '/ajax/post/',
		data: formData,
		dataType: 'json',
		method: 'POST',
		contentType: false,
		processData: false,
		cache: false,
		success: function(data) {
			renderPost(data)
		},
		error: function() {
			console.log("Error!");
		}
	});
}

function createPost() {
	event.preventDefault();
	var image=$('#id_post_image')[0].files[0];
	if (image){
		createPostWithImage()
	}
	var text=$('#post-field').val();
	var formData = new FormData();
	formData.append('post_text', text)
	formData.append('csrfmiddlewaretoken', postToken)
	$.ajax({
		url: '/ajax/post/',
		data: formData,
		dataType: 'json',
		method: 'POST',
		contentType: false,
		processData: false,
		success: function(data) {
			renderPost(data)
		},
		error: function() {
			console.log("Error!");
		}
	});
}
*/
