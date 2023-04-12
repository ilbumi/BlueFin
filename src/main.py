from common.config import settings
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "api.app:app",
        host=settings.service_host,
        port=settings.service_port,
        reload=True,
    )
