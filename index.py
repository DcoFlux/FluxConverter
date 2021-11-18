from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/mp3')
def mp3():
    return render_template('main2.html')

@app.route('/download-mp4', methods=['POST'])
def downloadmp4():
    link = request.form['link']
    try:
        p = YouTube(link).streams.get_highest_resolution().download('/Downloads')
        return send_file(p, as_attachment=True)
    except:
        return render_template('error.html')


@app.route('/download-mp3', methods=['POST'])
def downloadmp3():
    link = request.form['link']
    try:
        p = YouTube(link).streams.filter(only_audio=True).first().download('/Downloads')
        name = YouTube(link).streams.get_highest_resolution().title
        return send_file(p, attachment_filename=f"{name}.mp3", as_attachment=True)
    except:
        return render_template('error2.html')

	
if __name__ == '__main__':
    app.run(debug=True)