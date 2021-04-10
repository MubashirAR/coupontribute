import pika

print('before consuming')
params = pika.URLParameters('amqp://event-bus')
print('before consuming')
connection = pika.BlockingConnection(params)
print('before consuming')
channel = connection.channel()
print('before consuming')
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Sterted Consuming!')

channel.start_consuming()

# channel.close()
