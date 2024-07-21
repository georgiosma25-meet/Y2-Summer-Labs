from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app=Flask(__name__, template_folder='templates', static_folder='static')

