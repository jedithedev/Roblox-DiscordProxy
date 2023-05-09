from flask import Flask, request
from discord import SyncWebhook

app = Flask(__name__)


@app.route('/api/webhooks/<data1>/<data2>', methods=['GET', 'POST'])
def index(data1, data2):
  if request.method == 'POST':
    print(request.get_json())
    webhook=SyncWebhook.from_url('https://discord.com/api/webhooks/'+data1+'/'+data2)
    webhook.send(request.get_json()['content'])
    return ''
  return 'Error, get methods cannot be used here'


app.run(host='0.0.0.0', port=81)
