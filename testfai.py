#!/usr/bin/env python

import logfai
import logging
import os

if __name__ == '__main__':
	logger = logging.getLogger('faimon_test')
	logger.setLevel(logging.DEBUG)

	# STDOUT logging
	ch = logging.StreamHandler()
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)
	logger.addHandler(ch)

	# FAIMON logging
	fm = logfai.FaimonHandler(address=(os.environ['monserver'],4711))
	fai_formatter = logging.Formatter('FAIMON: %(name)s - %(levelname)s - %(message)s')
	fm.setFormatter(fai_formatter)
	logger.addHandler(fm)

	logger.info('started')

	logger.warning('done')
