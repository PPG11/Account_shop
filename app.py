from app import create_app

app = create_app()
# bootstrap = bootstrap_app(app)


@app.route('/hello')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5111)