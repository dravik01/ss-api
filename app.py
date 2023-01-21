"""
    Application
"""


import time
import pyautogui
import base64
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/screenshot')
def auto_ip():
    data = pyautogui.click('static\LockButton.png')
    time.sleep(0.5)
    img = pyautogui.screenshot('newIp.png')
    with open("newIp.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    return {"img" : my_string.decode()}


if __name__ == '__main__':
    app.run(debug=True)
