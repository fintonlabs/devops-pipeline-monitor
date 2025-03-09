import requests
from flask import Flask, render_template, jsonify
from threading import Thread
from time import sleep

app = Flask(__name__)

JENKINS_URL = 'http://your-jenkins-url'
JOB_NAME = 'your-job-name'
USERNAME = 'your-username'
PASSWORD = 'your-password'


def get_last_build_status():
    """
    Fetches the status of the last build of a Jenkins job.

    Returns:
        str: The status of the last build.
    """
    url = f'{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json'
    response = requests.get(url, auth=(USERNAME, PASSWORD))
    data = response.json()

    return data['result']


@app.route('/')
def home():
    """
    Renders the home page with the status of the last build.

    Returns:
        str: The rendered HTML of the home page.
    """
    status = get_last_build_status()
    return render_template('home.html', status=status)


def monitor_job():
    """
    Monitors a Jenkins job and sends an alert if the build fails.
    """
    while True:
        status = get_last_build_status()
        if status == 'FAILURE':
            print('ALERT: Build failed!')
        sleep(60)


if __name__ == '__main__':
    # Start the job monitoring in a separate thread
    Thread(target=monitor_job).start()
    # Start the Flask application
    app.run(debug=True)