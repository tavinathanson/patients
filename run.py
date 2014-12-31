from patients import app


if __name__ == '__main__':
    app.run(use_reloader=app.config['USE_RELOADER'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'],
            host='0.0.0.0')
