import os

import floodfill_pathfinding
import ai
import board

import cherrypy

"""
Introducing taipan-no-prisoners
"""

taipans_brain = ai.SnakeAI()

class Battlesnake(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return {
            "apiversion": "1",
            "author": "Lewis Hamilton",
            "color": "#bf5422",
            "head": "do-sammy",
            "tail": "small-rattle",
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        data = cherrypy.request.json

        print("START")
        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        data = cherrypy.request.json

        move = taipans_brain.move(data)

        print(f"MOVE: {move}")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        data = cherrypy.request.json

        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "10069")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
