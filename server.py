from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psutil
import platform
import cpuinfo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status")
def get_status():
    osi_type = platform.system()
    osi_version=platform.version()
    architecture=platform.machine()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    cpu_info = cpuinfo.get_cpu_info()
    processor = cpu_info.get("brand_raw", platform.processor())
    return {"cpu": cpu, "memory": memory, "disk": disk,"os_type": osi_type, "os_version": osi_version, "architecture":architecture , "processor": processor}
