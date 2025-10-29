from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store feedbacks in memory (for now)
feedback_list = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    subject = request.form['subject']
    rating = request.form['rating']
    comments = request.form['comments']

    feedback = {
        'name': name,
        'subject': subject,
        'rating': rating,
        'comments': comments
    }

    feedback_list.append(feedback)
    return redirect(url_for('view_feedbacks'))

@app.route('/feedbacks')
def view_feedbacks():
    return render_template('feedbacks.html', feedbacks=feedback_list)

@app.route('/health')
def health_check():
    return {"status": "OK", "message": "Feedback app is running smoothly!"}

"""
    Returns a simple JSON status to indicate the application is running.
    This route is tested by tests/test_health.py. hi
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

