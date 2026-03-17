import mysql.connector
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


class SqlConnection:
    def __init__(self, logger: logging.Logger):
        self.logger = logger
    
    def connection(self):
        try: 
            
            mydb = mysql.connector.connect(
                host="mysql",
                port=3306,
                user="root",
                password="root",
                database="digital_hunter",
            )
            self.logger.info("connected to mysql sucssfully")
            return mydb
        except Exception as e:
            self.logger.error(f"faild to connect. {e}")
