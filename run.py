from elites import app, path, cert

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6660, ssl_context=(
        path.join(cert, 'cert.pem'), path.join(cert, 'key.pem')), debug=True)
