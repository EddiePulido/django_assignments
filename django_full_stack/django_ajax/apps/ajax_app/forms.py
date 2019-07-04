from django import forms

class PostForm(forms.Form):
    post = forms.CharField(widget=forms.Textarea)
    post.render("post_id")
