from apps import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host=app.config['LOCAL_IP'], port=app.config['LOCAL_PORT'])

