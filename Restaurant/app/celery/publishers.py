import pika

params = pika.URLParameters('amqp://event-bus/')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')
