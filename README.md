Elites Syndicate Server

1. Create virtual environment
2. Activate virtual environment
3. Install dependencies with: "pip install -r requirements.txt"
4. Create "cert" directory on the projects root directory
5. Create self-signed certificate: 
    "openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365"
6. Run server with: "python run.py"
