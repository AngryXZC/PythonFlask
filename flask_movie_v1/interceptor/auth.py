from application import app


@app.before_request
def before_request():
    app.logger.info("------------befor_request___________")
    return


@app.after_request
def after_request(response):
    app.logger.info("___________after_request___________")
    return response
