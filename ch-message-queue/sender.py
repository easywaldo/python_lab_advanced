import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))

channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(10000):
    # 10,000 개의 메시지를 큐에 적재!!
    channel.basic_publish(exchange='', routing_key='hello', body=f'this is message number {i}')
    print('# 메시지를 보냈습니다!!! %s' % str(i))

connection.close()