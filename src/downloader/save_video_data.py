from aiofiles import open
import json


async def save_video_data(self, dir, data: dict):
    try:
        file_path = f"{dir}/{data['id']}.json"
        async with open(file_path, 'w', encoding='utf-8') as f:
            await f.write(json.dumps(data, indent=4))
    except Exception as e:
        self.log.warning((f"save video data fail: {e}"))
