#Пример кода для отправки сообщения от producer в очередь:
import pika
#В данном примере мы

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) #создаем соединение с RabbitMQ,
channel = connection.channel()

channel.queue_declare(queue='hello') #объявляем очередь 'hello',

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')  #и отправляем сообщение 'Hello World!' в эту очередь.
print(" [x] Sent 'Hello World!'")

connection.close()