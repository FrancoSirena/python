import logging
import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:], 'l:', ['log='])

log_level = logging.DEBUG
for opt, arg in opts:
    if opt in ('-l', '--log'):
        log_level = getattr(logging, arg.upper())

logging.basicConfig(filename='./demo.log', level=log_level, format='%(asctime)s %(levelname)s: %(message)s')

for i in range(0, 100):
    if i% 5:
        logging.debug('Found a number divisible by 5: {0}'.format(i))
    else:
        logging.info('At number {0}'.format(i))
logging.warning('End')
