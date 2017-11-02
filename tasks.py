from invoke import task


@task
def start(ctx, docs=False):
    """ start development server """
    ctx.run('export DJANGO_SETTINGS_MODULE="app.settings"')
    ctx.run('python manage.py makemigrations')
    ctx.run('python manage.py collectstatic --noinput')
    ctx.run('python manage.py migrate --noinput')
    ctx.run('python manage.py runserver 0.0.0.0:8001')
