import os
import bmemcached
from flask import Flask, jsonify

memcache = bmemcached.Client(os.environ['MEMCACHEDCLOUD_SERVERS'].split(','),
                             os.environ['MEMCACHEDCLOUD_USERNAME'],
                             os.environ['MEMCACHEDCLOUD_PASSWORD'])
app = Flask(__name__)


@app.route('/emote.json')
def emote_json():
    return jsonify(memcache.get('emote'))


@app.route('/')
def e():
    return 'e'


if __name__ == '__main__':
    app.run()
