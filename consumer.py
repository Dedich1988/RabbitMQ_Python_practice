#Пример кода для получения сообщения от consumer из очереди:
#В данном примере мы создаем соединение с RabbitMQ, объявляем очередь 'hello', и ожидаем сообщения из этой очереди. Когда сообщение приходит, вызывается функция callback, которая выводит сообщение в консоль.
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()