#!/Learning/Python/Web Application Development/TurboGears
# -*- coding: utf-8 -*-
"""
@author: Jackson Calixo
"""

from wsgiref.simple_server import make_server
from tg import expose, TGController, AppConfig

class RootController(TGController):
    @expose('index.xhtml')
    def index(self):
        return {}
    @expose('about.xhtml')
    def about(self):
        kjinfo = "The Kajiki template engine is a fast and validated template that provides python3 support. You first have to install Kajiki then add it to the list of available engines inside AppConfig."
        return dict(kajiki_info=kjinfo)

config = AppConfig(minimal=True, root_controller=RootController())
config.renderers = ['kajiki']
config.serve_static = True
config.paths['static_files'] = 'public'
print("Serving on port 7250...")
httpd = make_server('', 7250, config.make_wsgi_app())
httpd.serve_forever()
