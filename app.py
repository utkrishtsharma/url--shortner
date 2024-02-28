from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, StringField, validators
import random
import string

app = Flask(__name__, static_url_path='/static')

class URLForm(Form):
    url = StringField('URL', validators=[validators.URL()])
    custom_slug = StringField('Custom Slug')

url_mapping = {}

def generate_slug():
    """Generate a random 6-character slug"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/')
def index():
    form = URLForm()
    # Fetch all slugs in the url_mapping
    slugs = url_mapping.keys()
    return render_template('index.html', form=form, slugs=slugs,  url_mapping=url_mapping)

@app.route('/success')
def success():
    original_url = request.args.get('original_url')
    return render_template('success.html', original_url=original_url)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    
    # Get custom_slug from form data if present, otherwise set it to None
    custom_slug = request.form.get('custom_slug')

    # Check if a custom slug is provided and is unique
    if custom_slug:
        if custom_slug in url_mapping:
            return render_template('index.html', form=URLForm(), error="Custom slug is not unique, please choose another.")
        else:
            slug = custom_slug
    else:
        # Generate a random slug
        slug = generate_slug()
        while slug in url_mapping:
            slug = generate_slug()

    url_mapping[slug] = original_url

    return render_template('success.html', short_url=request.url_root + slug ,original_url=original_url)

@app.route('/<slug>')
def redirect_to_url(slug):
    if slug in url_mapping:
        return redirect(url_mapping[slug])
    else:
        return "404 Not Found", 404

if __name__ == '__main__':
    app.run(debug=True)
