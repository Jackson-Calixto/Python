from wsgiref.simple_server import make_server
from tg import expose, TGController, AppConfig

class MyController(TGController):
    @expose()
    def index(self):
        return "<p> SimpleApp Landing Page </p>"
    @expose()
    def greeting(self):
        return "<h4> SimpleApp: Hello there!</h4>"

config = AppConfig(minimal=True, root_controller=MyController())
print("Serving on port 7250...")
httpd = make_server('', 7250, config.make_wsgi_app())
httpd.serve_forever()
