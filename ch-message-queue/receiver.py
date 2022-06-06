import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(' # 메시지를 받았습니다. : %r' % body)
    
channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

print('메시지를 기다리고 있습니다. 종료를 하려면 CTRL+C를 누르세요.')

channel.start_consuming()