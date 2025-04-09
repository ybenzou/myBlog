from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=443,
        ssl_context=(
            '/etc/letsencrypt/live/ybenzou.work/fullchain.pem',  
            '/etc/letsencrypt/live/ybenzou.work/privkey.pem'   
        )
    )