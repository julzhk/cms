from invoke import task

@task
def deploy(c, docs=False, bytecode=False, extra=''):
    c.run("heroku run python manage.py migrate --settings=cms.settings.prod -a cms")
    c.run("heroku run python manage.py collectstatic --settings=cms.settings.prod -a cms")