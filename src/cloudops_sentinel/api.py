from flask import Flask, jsonify
from .metrics import snapshot


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return """
        <html>
          <head>
            <title>CloudOps Sentinel</title>
            <style>
              body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; padding: 0; background: #f9fafb; color: #333; }
              header { background: linear-gradient(135deg, #2c3e50, #3498db); color: white; padding: 40px 20px; text-align: center; }
              header h1 { margin: 0; font-size: 2.5em; }
              header p { margin-top: 10px; font-size: 1.2em; }
              main { padding: 30px; max-width: 800px; margin: auto; }
              section { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
              h2 { color: #2c3e50; margin-top: 0; }
              .endpoint { margin: 10px 0; font-size: 1.1em; }
              .endpoint code { background: #eef; padding: 4px 8px; border-radius: 6px; }
              footer { text-align: center; padding: 20px; font-size: 0.9em; color: #555; }
              img.icon { width: 32px; vertical-align: middle; margin-right: 8px; }
            </style>
          </head>
          <body>
            <header>
              <h1>🚀 CloudOps Sentinel</h1>
              <p>By Akash – Your DevOps Monitoring & Automation Microservice</p>
            </header>
            <main>
              <section>
                <h2>📊 Available Endpoints</h2>
                <div class="endpoint">
                  <img src="https://img.icons8.com/ios-filled/50/2c3e50/ok.png" class="icon"/> 
                  <code>/health</code> → Service health check
                </div>
                <div class="endpoint">
                  <img src="https://img.icons8.com/ios-filled/50/3498db/computer.png" class="icon"/> 
                  <code>/metrics</code> → CPU & Memory usage snapshot
                </div>
              </section>
              <section>
                <h2>🛠️ Tech Stack</h2>
                <p>Built with <b>Python</b>, <b>Flask</b>, and <b>psutil</b></p>
              </section>
            </main>
            <footer>
              <p>© 2025 CloudOps Sentinel | Open Source Project</p>
            </footer>
          </body>
        </html>
        """

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.route("/metrics")
    def metrics():
        return jsonify(snapshot())

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)

