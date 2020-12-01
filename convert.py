#!/usr/bin/env python3
from xml.etree.ElementTree import Element, SubElement, tostring
import json

subscription_in_file = "subscriptions.json"
subscription_out_file = "subscriptions.opml"

with open(subscription_in_file, "r") as f:
   data = json.load(f)

root = Element('opml')
root.set('version', '1.1')

body = SubElement(root, 'body')
child = SubElement(body, 'outline', {'text': "YouTube Subscriptions", 'title': "YouTube Subscriptions"})

for entry in data:
    title = entry["snippet"]["title"]
    channel_id = entry["snippet"]["resourceId"]["channelId"]
    url = "https://www.youtube.com/feeds/videos.xml?channel_id="+channel_id
    SubElement(child, 'outline', {'text': title, 'title': title, 'type': "rss", 'xmlUrl': url})

with open(subscription_out_file, "wb") as f:
    f.write(tostring(root, 'utf-8'))

