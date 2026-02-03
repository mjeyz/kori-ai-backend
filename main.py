from flask import Flask, session
import psycopg2
import redis
app = Flask(__name__)

DATABASE_URL = 'postgresql://postgres:9992@localhost/kori-ai-backend'

conn = psycopg2.connect(DATABASE_URL)

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    password=None,
    decode_responses=True
)

try:
    response = r.ping()
    print(f"Redis connection successful: {response}")
except redis.ConnectionError as e:
    print(f"Redis connection failed: {e}")


if __name__ == "__main__":
    app.run(debug=True)