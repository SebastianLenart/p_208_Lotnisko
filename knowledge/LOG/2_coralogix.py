# app/io.py
import logging

def _init_logger():
    logger = logging.getLogger('app.io')
    logger.setLevel(logging.INFO)

_init_logger()
_logger = logging.getLogger('app.io')

def write_data(file_name, data):
    try:
        # write data
        _logger.info('Successfully wrote %d bytes into %s', len(data), file_name)
        _logger.info('Successfully wrote %(data_size)s bytes into %(file_name)s',
                     {'data_size': len(data), 'file_name': file_name})
    except FileNotFoundError:
        _logger.exception('Failed to write data into %s', file_name)
