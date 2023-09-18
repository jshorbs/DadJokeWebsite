import os
import sys
from invoke import task

venv = "source venv/bin/activate"
GOOGLE_CLOUD_PROJECT = os.environ.get('GOOGLE_CLOUD_PROJECT')
REGION = os.environ.get('REGION', "us-central1")

@task
def require_project(c): 
    """Check if GOOGLE_CLOUD_PROJECT is set"""
    if GOOGLE_CLOUD_PROJECT is None:
        sys.exit("GOOGLE_CLOUD_PROJECT environment variable must be set")

@task
def require_venv(c, quiet=True):
    """Check if virtual environment is setup, requirements are installed"""

    c.run("python3 -m venv venv")

    quite_param = "-q" if quiet else ""

    with c.prefix(venv):
        c.run(f"pip install {quite_param} --upgrade pip")
        c.run(f"pip install {quite_param} -r requirements.txt")

@task
def setup_virtualenv(c):
    """Setup virtual environment"""

    require_venv(c, quiet=False)

@task(pre=[require_venv])
def start(c): 
    """Start Flask server"""

    with c.prefix(venv):
        c.run("python app.py")

@task(pre=[require_venv])
def dev(c):
    """Start Flask server in development mode"""

    with c.prefix(venv):
        c.run("FLASK_ENV=development python app.py")

@task(pre=[require_project])
def deploy(c):
    """Deploy to Google Cloud Run"""

    c.run(
        "gcloud run deploy dad-jokes "
        f"--image us-central1-docker.pkg.dev/{GOOGLE_CLOUD_PROJECT}/aidadjokes/dad-jokes "
        f"--platform managed --region {REGION}"
    )