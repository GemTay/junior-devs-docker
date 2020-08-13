from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://media.giphy.com/media/yFQ0ywscgobJK/giphy.gif",
   "https://media.giphy.com/media/BLCHvwl9C5j1u/giphy.gif",
   "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif",
   "https://media.giphy.com/media/4Iw2OzgiiTc4M/giphy.gif",
   "https://media.giphy.com/media/WYEWpk4lRPDq0/giphy.gif",
   "https://media.giphy.com/media/GvMSpPx44XlFm/giphy.gif",
   "https://media.giphy.com/media/GvMSpPx44XlFm/giphy.gif",
   "https://i.imgur.com/kGpB3FF.gif",
   "https://i.imgur.com/4SUrRgI.gif",
   "https://i.imgur.com/b9IZinu.gif",
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")