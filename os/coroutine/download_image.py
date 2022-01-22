import asyncio
from pathlib import Path
import logging
from urllib.request import urlopen, Request
import os
from time import time
import aiohttp

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

CODEFLEX_IMAGES_URLS = ['https://codeflex.co/wp-content/uploads/2021/01/pandas-dataframe-python-1024x512.png',
                        'https://codeflex.co/wp-content/uploads/2021/02/github-actions-deployment-to-eks-with-kustomize-1024x536.jpg',
                        'https://codeflex.co/wp-content/uploads/2021/02/boto3-s3-multipart-upload-1024x536.jpg',
                        'https://codeflex.co/wp-content/uploads/2018/02/kafka-cluster-architecture.jpg',
                        'https://codeflex.co/wp-content/uploads/2016/09/redis-cluster-topology.png']


async def download_image_async(session, dir, img_url):
    download_path = dir / os.path.basename(img_url)
    async with session.get(img_url) as response:
        with download_path.open('wb') as f:
            while True:
                chunk = await response.content.read(512)
                if not chunk:
                    break
                f.write(chunk)
    logger.info('Downloaded: ' + img_url)


async def main():
    images_dir = Path("codeflex_images")
    Path("codeflex_images").mkdir(parents=False, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        tasks = [(download_image_async(session, images_dir, img_url)) for img_url in CODEFLEX_IMAGES_URLS]
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    start = time()

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()

    logger.info('Download time: %s seconds', time() - start)
