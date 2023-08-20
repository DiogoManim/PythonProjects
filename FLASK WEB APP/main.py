from website import create_app

app = create_app()

if __name__ == '__main__':  # This makes the server run only when the file is executed.
    app.run(debug=True)     # Every time we make a change in our code, it's going to automatically re-run the web server.
                            # If the debug was False, we would have to re-run manually the code to update the server.