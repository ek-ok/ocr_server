#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Test OCR application
'''

from flask import Flask, request, jsonify, render_template
from ocr import extract_text
import os

application = Flask(__name__)


@application.route('/')
def main():
    return render_template('index.html')


@application.route('/ocr', methods=['POST'])
def ocr():
    url = request.json['image_url']
    text = extract_text(url)
    return jsonify({'text': text, 'url': url})


if __name__ == '__main__':

    if os.uname()[1] == 'MacBookPro.local':
        port = 8080
        debug = True
    else:
        port = 80
        debug = False

    application.run(host='0.0.0.0', port=port, debug=debug)
