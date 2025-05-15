from website import create_app
from website.views import jinja2_zip

app = create_app()
app.jinja_env.globals['jinja2_zip'] = jinja2_zip

if __name__ == '__main__':
    app.run(debug=True)
