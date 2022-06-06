import pika
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message_list = [str(i) + ":" + str(random.randrange(1, 11)) for i in range(100)]
def send_message(message):
    channel.basic_publish(exchange='', routing_key='task_queue', body=str(message),
                          properties=pika.BasicProperties(delivery_mode=2,))
    
for msg in message_list:
    send_message(msg)
    print('# 메시지를 보냈습니다: %r' % msg)

# for i in range(10000):
#     # 10,000 개의 메시지를 큐에 적재!!
#     channel.basic_publish(exchange='', routing_key='hello', body=f'this is message number {i}')
#     print('# 메시지를 보냈습니다!!! %s' % str(i))

connection.close()