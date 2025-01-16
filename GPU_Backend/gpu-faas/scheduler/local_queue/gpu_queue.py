# local_queue/gpu_queue.py
from typing import Dict, List, Any
import time
from collections import deque

# local_queue/gpu_queue.py
class LocalQueueManager:
    def __init__(self, config: Dict[str, Any]):
        self.per_gpu_size = config["per_gpu_size"]
        self.timeout = config["timeout_seconds"]
        self.queues = {}

    async def add_to_queue(self, gpu_id: str, request: Dict):
        if gpu_id not in self.queues:
            self.queues[gpu_id] = deque(maxlen=self.per_gpu_size)
        self.queues[gpu_id].append(request)