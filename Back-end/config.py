import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_secret_key'
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY') or 'AIzaSyDX2celKEp4nGzuUi0cdXrk2bMktGWY7Fs'
