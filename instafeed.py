"""
Pulls recent images from instagram and uses wget to download
new images

Author: Rick Wolf
"""

from instagram.client import InstagramAPI
from os import listdir, system
import requests

client_id = 'a9ec09a9ba834019a48394823fde48b7'
client_secret = '9fd810284766482eb7bc7ed9bfbfd0f5'
dl_path = "/home/pi/vivianne"


api = InstagramAPI(client_id=client_id, client_secret=client_secret)
vivs_media = api.tag_recent_media(tag_name="viviannewolf", count=30)


# a list of links for the images
photos = []
for media in vivs_media[0]:
    photos.append(media.images['standard_resolution'].url)

# a list of only the filenames of the images
fnames = [ tmp.split("/")[5] for tmp in photos]

# a list of downloaded filenames
downloaded = listdir(dl_path)

# download new images
for i in range(len(fnames)):
    if fnames[i] not in downloaded:
        r = requests.get(photos[i])
        image_file = open(dl_path + fnames[i], 'w')
        image_file.write(r.content)
        image_file.close()