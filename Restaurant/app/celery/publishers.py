import pika

params = pika.URLParameters('amqp://event-bus/')
print('>>>>> publisher1')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    print('publish')
    channel.basic_publish(exchange='', routing_key='restaurant', body='hello')
