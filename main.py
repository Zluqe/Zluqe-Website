from flask import Flask, render_template, send_from_directory, redirect
import requests
import random
import config
import os

app = Flask(__name__, static_folder='static', template_folder='views')

# Render Templates / HTML's
@app.route('/')
def index():
    return render_template('main/index.html')


# Redirects
@app.route('/discord')
def discord_invite():
    return redirect(config.DISCORD_INVITE, code=302)

@app.route('/github')
def github_link():
    return redirect(config.GITHUB, code=302)

@app.route('/create')
def zluqe_create():
    return redirect(config.PANEL_STORE_CREATE, code=302)

@app.route('/panel')
def zluqe_panel():
    return redirect(config.PANEL, code=302)


# Static Files privacy-policy.pdf
@app.route('/tos', defaults={'path': ''})
@app.route('/terms', defaults={'path': ''})
@app.route('/terms-of-service', defaults={'path': ''})
def zluqe_terms(path):
    return send_from_directory(os.path.join('static', 'misc'), 'terms.pdf', as_attachment=False)

@app.route('/priv-p', defaults={'path': ''})
@app.route('/pp', defaults={'path': ''})
@app.route('/privacy-policy', defaults={'path': ''})
def zluqe_pp(path):
    return send_from_directory(os.path.join('static', 'misc'), 'privacy-policy.pdf', as_attachment=False)

# errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html')

if __name__ == '__main__':
    app.run(debug=True)
