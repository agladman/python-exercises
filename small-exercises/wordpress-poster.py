#!/usr/bin/env python3


from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost

from config import blog_url, username, password


wp = Client(blog_url, username, password)
post = WordPressPost()
post.title = 'Testing post.title.'
post.content = 'Testing post.content. This is a test.'
post.slug = 'Testing post.slug'
post.terms_names = {
	'post_tag': ['IPA', 'UK'],
	'category': ['BeerBods cheat sheets']
	}
wp.call(NewPost(post))
