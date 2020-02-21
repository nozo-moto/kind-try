from logging import getLogger

logger = getLogger(__name__)

def main():
    logger.debug('This is a Debug message')
    logger.info('This is a Info message')
    logger.warning('This is a Warning message')
    logger.error('This is a Error message')
    logger.critical('This is a Critical message')
    
if __name__ == '__main__':
    main()
