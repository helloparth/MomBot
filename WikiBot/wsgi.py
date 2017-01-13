import cherrypy
from app import Root

#constants
HOST = '127.0.0.1'
PORT = 8081

app = cherrypy.tree.mount(Root(), '/api')

if __name__ == '__main__':

        cherrypy.config.update({
                'server.socket_host':HOST,
                'server.socket_port':POST,
        })

        #run app using cherrypy server
        cherrypy.quickstart(Root())
