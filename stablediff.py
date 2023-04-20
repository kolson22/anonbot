import requests
import io
import base64
from PIL import Image, PngImagePlugin

class Stable:
  url = ""
  payload = {}
  def __init__(self, url, steps=15, sampler_index="Euler a"):
    self.url = url
    self.payload['steps'] = steps
    self.payload['sampler_index'] = sampler_index

  def create_image(self, prompt):
    self.payload['prompt'] = prompt
    response = requests.post(url=f'{self.url}/sdapi/v1/txt2img', json=self.payload)
    r = response.json()
    return r['images']

    # for i in r['images']:
    #     image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

    #     png_payload = {
    #         "image": "data:image/png;base64," + i
    #     }
    #     response2 = requests.post(url=f'{self.url}/sdapi/v1/png-info', json=png_payload)

    #     pnginfo = PngImagePlugin.PngInfo()
    #     pnginfo.add_text("parameters", response2.json().get("info"))
    #     image.save('output.png', pnginfo=pnginfo)
