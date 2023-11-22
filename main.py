from fastapi import FastAPI
from fastapi.responses import JSONResponse
from clickhouse_driver import Client

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the ClickHouse top words service. Use /getWords to get the top 100 words."}


@app.get("/getWords")
def get_top_words():
    client = Client(host='localhost', port=9000)

    query = """
    SELECT word, count(*) as count
    FROM (
        SELECT arrayJoin(splitByChar(' ', text)) AS word
        FROM lenta_news)
    GROUP BY word
    ORDER BY count DESC
    LIMIT 100;

    """
    result = client.execute(query)

    words_count = [{"text": row[0], "count": row[1]} for row in result]
    return JSONResponse(content=words_count)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=9090)
