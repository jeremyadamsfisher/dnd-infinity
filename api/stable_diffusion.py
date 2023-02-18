import base64
import os
import uuid

import baseten
import streamlit as st


@st.cache_data
def get_model():
    baseten.login(os.environ["BASETEN_API_KEY"])
    model = baseten.deployed_model_id("nBrx48P")
    return model


def get_image(prompt, url):
    res = get_model().predict({"prompt": prompt})
    b64_im = res["data"]
    bytes_ = base64.b64decode(b64_im)
    with open(fp := f"{uuid.uuid4()}.png", "wb") as f:
        f.write(bytes_)
    return fp


# def get_image_(prompt, url):
#     local_filename = f"{uuid.uuid4()}.png"
#     with requests.post(url, json={"prompt": prompt}, stream=True) as r:
#         r.raise_for_status()
#         with open(local_filename, "wb") as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)
#     return local_filename
