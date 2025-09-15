@app.route("/")
def index():
    return """
    <html>
      <head>
        <title>CloudOps Sentinel</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 40px; background: #f4f4f9; color: #333; }
          h1 { color: #2c3e50; }
          code { background: #eee; padding: 3px 6px; border-radius: 4px; }
          .endpoints { margin-top: 20px; }
          .endpoint { margin-bottom: 10px; }
        </style>
      </head>
      <body>
        <h1>🚀 CloudOps Sentinel API</h1>
        <p>Welcome! This is your DevOps monitoring & automation microservice.</p>
        <div class="endpoints">
          <h3>Available Endpoints:</h3>
          <div class="endpoint">
            <code>/health</code> → Service health check
          </div>
          <div class="endpoint">
            <code>/metrics</code> → CPU & Memory usage snapshot
          </div>
        </div>
        <p><em>Built with Python + Flask + psutil</em></p>
      </body>
    </html>
    """
