# pylog-faimon

python logging to [FAImond](http://fai-project.org/doc/man/faimond.html)

## usage

```python
import logfai
import logging
import os

logger = logging.getLogger('faimon_test')
logger.setLevel(logging.DEBUG)

# FAIMON logging
log_faimon = logfai.FaimonHandler(address=(os.environ['monserver'],4711))
fai_formatter = logging.Formatter('FAIMON: %(name)s - %(levelname)s - %(message)s')
log_faimon.setFormatter(fai_formatter)
logger.addHandler(log_faimon)

logger.info('started')

logger.warning('done')
```

## requirements

* python 2.x
* standard modules `os`, `logging`, and `socket`

## support

Please file [an issue on github](https://github.com/chicks-net/pylog-faimon/issues)
if you have difficulty.
