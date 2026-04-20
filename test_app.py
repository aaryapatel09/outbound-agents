"""Minimal FastAPI stub used by cloudbuild-test.yaml to smoke-test Cloud Run.

This is not an application entry point — the real services live in lead_finder/,
sdr/, lead_manager/, ui_client/, and gmail_pubsub_listener/. It exists only so
the deployment pipeline has a trivial image to verify build + deploy + health
endpoints work before deploying the actual services.
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/health")
def health():
    return JSONResponse(status_code=200, content={"status": "ok"})


@app.get("/")
def root():
    return {"message": "outbound-agents deploy smoke-test"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
