import logging
logging.basicConfig(level=logging.DEBUG, filename='runtime.log', filemode='w', format = (
                                                    '%(levelname)s:\t'
                                                    '%(filename)s:'
                                                    '%(funcName)s():'
                                                    '%(lineno)d\t'
                                                    '%(message)s'
                                                )
                    )