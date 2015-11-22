#!/usr/bin/env python
"""demonstrate logfai module"""

import logfai
import logging
import os

if __name__ == '__main__':
	logger = logging.getLogger('faimon_test')
	logger.setLevel(logging.DEBUG)

	# STDOUT logging
	log_stdout = logging.StreamHandler()
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	log_stdout.setFormatter(formatter)
	logger.addHandler(log_stdout)

	# FAIMON logging
	log_faimon = logfai.FaimonHandler(address=(os.environ['monserver'], 4711))
	fai_formatter = logging.Formatter('FAIMON: %(name)s - %(levelname)s - %(message)s')
	log_faimon.setFormatter(fai_formatter)
	logger.addHandler(log_faimon)

	logger.info('started')

	logger.warning('done')
