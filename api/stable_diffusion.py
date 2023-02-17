import uuid

import requests


def get_image(prompt, url):
    local_filename = f"{uuid.uuid4()}.png"
    with requests.post(url, json={"prompt": prompt}, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename
