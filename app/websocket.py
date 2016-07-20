import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template

clientes = set()


class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        clientes.add(self)
        print 'Nuevo cliente'
        self.write_message("Conexion socket aceptada")

    def on_message(self, message):
        print 'Recibido:', message
        self.write_message("Servidor eco: " + message)

    def on_close(self):
        print 'Conexion cerrada'
