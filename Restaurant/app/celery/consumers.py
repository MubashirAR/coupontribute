import pika
print('>>> consumers')
params = pika.URLParameters('amqp://event-bus')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='restaurant')

def callback(ch, method, properties, body):
    print('Received in restaurant')
    print(body)


channel.basic_consume(queue='restaurant', on_message_callback=callback, auto_ack=True)

print('start consuming')
channel.start_consuming()

channel.close()
print('callback')
callback()