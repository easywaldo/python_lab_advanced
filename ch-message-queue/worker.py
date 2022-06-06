import pika
import time
import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' # 메시지를 기다리고 있습니다. 종료하려면 CTRL+C를 누르세요.')

def callback(ch, method, properties, body):
    msg = str(body, 'utf8').split(":")
    
    print(' [%s] %s 메시지를 받았습니다. \n %r' % (datetime.datetime.now(), msg[0], body))
    
    # 메시지에서 가져온 숫자만큼 잠시 대기
    time.sleep(int(str(msg[1])) / 10)
    print(' # [%s] 완료 했습니다.' % datetime.datetime.now())
    
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
# 메시지를 미리 가져오게 설정
# 만약 이 설정이 없는 경우 큐에 메시지를 요청할 때 무제한으로 가져온다
# 중간에 새로운 컨슈머를 실행하는 경우 기존에 큐에 들어가 있던 메시지를 분배하지 않는다
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='task_queue', auto_ack=False, on_message_callback=callback)

channel.start_consuming()