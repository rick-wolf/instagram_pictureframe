"""
Pulls recent images from instagram and uses wget to download
new images

Author: Rick Wolf
"""

from instagram.client import InstagramAPI
from os import listdir, system
import requests

client_id = ''
client_secret = ''
dl_path = "/home/pi/viv"


api = InstagramAPI(client_id=client_id, client_secret=client_secret)
vivs_media = api.tag_recent_media(tag_name="XXXXXXXXX", count=30)


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
