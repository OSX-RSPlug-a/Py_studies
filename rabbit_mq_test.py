import pika
import sys
from pika.exceptions import AMQPConnectionError, ChannelClosedByBroker
#pip install pika


def test_rabbitmq_connection(host='localhost', port=5672, username='guest', password='guest', virtual_host='/'):
    """
    Attempts to establish a blocking connection to a RabbitMQ server.
    """
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(
        host=host,
        port=port,
        virtual_host=virtual_host,
        credentials=credentials,
    )

    try:
        print(f"Attempting to connect to RabbitMQ at amqp://{username}:***@{host}:{port}{virtual_host}...")
        
        connection = pika.BlockingConnection(parameters)
        
        
        channel = connection.channel()
        
        print("\n✅ Success! Connection to RabbitMQ established and channel opened.")
        
        channel.close()
        connection.close()
        print("Connection closed cleanly.")
        
    except AMQPConnectionError as e:
        print(f"\n❌ Failed to connect to RabbitMQ.")
        print(f"   Error: {e.__class__.__name__} - {e}")
        print("   Possible reasons: RabbitMQ is not running, incorrect host/port, or firewall is blocking the connection.")
        sys.exit(1)
        
    except ChannelClosedByBroker as e:
        print(f"\n❌ Connection established, but failed to open channel (ChannelClosedByBroker).")
        print(f"   Error: {e}")
        print("   Possible reasons: Incorrect virtual host or user permissions issue (e.g., wrong username/password).")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e.__class__.__name__} - {e}")
        sys.exit(1)

if __name__ == "__main__":
    RABBITMQ_HOST = 'localhost' 
    RABBITMQ_PORT = 5672        
    RABBITMQ_USER = 'guest'     
    RABBITMQ_PASS = 'guest'     
    RABBITMQ_VHOST = '/'         

    test_rabbitmq_connection(
        host=RABBITMQ_HOST, 
        port=RABBITMQ_PORT, 
        username=RABBITMQ_USER, 
        password=RABBITMQ_PASS,
        virtual_host=RABBITMQ_VHOST
    )