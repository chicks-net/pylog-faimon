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
fm = logfai.FaimonHandler(address=(os.environ['monserver'],4711))
fai_formatter = logging.Formatter('FAIMON: %(name)s - %(levelname)s - %(message)s')
fm.setFormatter(fai_formatter)
logger.addHandler(fm)

logger.info('started')

logger.warning('done')
```
