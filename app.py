# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
from wtforms import Form, StringField, validators
import random
import string

# Initialize Flask app
app = Flask(__name__, static_url_path='/static')

# Define form for URL submission
class URLForm(Form):
    url = StringField('URL', validators=[validators.URL()])
    custom_slug = StringField('Custom Slug')

# Dictionary to store URL mappings (slug to original URL)
url_mapping = {}

# Function to generate a random 6-character slug
def generate_slug():
    """Generate a random 6-character slug"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# Route for handling URL shortening
@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm(request.form)
    if request.method == 'POST' and form.validate():
        original_url = form.url.data
        custom_slug = form.custom_slug.data

        # Generate slug based on custom input or randomly if not provided
        if custom_slug:
            if custom_slug in url_mapping:
                return render_template('index.html', form=form, error="Custom slug is not unique, please choose another.")
            else:
                slug = custom_slug
        else:
            slug = generate_slug()
            while slug in url_mapping:
                slug = generate_slug()

        # Store the original URL with the generated slug
        url_mapping[slug] = original_url

        # Redirect to success page with the generated short URL
        return redirect(url_for('success', slug=slug))

    # Render index page with URL submission form and list of existing slugs
    slugs = url_mapping.keys()
    return render_template('index.html', form=form, slugs=slugs, url_mapping=url_mapping)

# Route for displaying the success page with short URL
@app.route('/success/<slug>')
def success(slug):
    original_url = url_mapping.get(slug)
    short_url = request.url_root + slug
    return render_template('success.html', original_url=original_url, short_url=short_url)

# Route for redirecting short URLs to their original long URLs
@app.route('/<slug>')
def redirect_to_url(slug):
    if slug in url_mapping:
        return redirect(url_mapping[slug])
    else:
        return "404 Not Found", 404

# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(host='172.31.6.44', port=5000, debug=True)
