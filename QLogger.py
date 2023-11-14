import logging
import sys


class QLogHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, message=''):
        if isinstance(message, str):
            raise ValueError('参数message必须是string类型')
        sys.stdout.write('this is QLogger')





if __name__ == '__main__':
    logging.getLogger().addHandler(QLogHandler())
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info('1')















