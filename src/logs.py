import logging

masks_logger = logging.getLogger('masks')
masks_handler = logging.FileHandler('logs.log', 'w')
masks_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
masks_handler.setFormatter(masks_formatter)
masks_logger.addHandler(masks_handler)
masks_logger.setLevel(logging.INFO)

utils_logger = logging.getLogger('utils')
utils_handler = logging.FileHandler('logs.log', 'w')
utils_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
utils_handler.setFormatter(utils_formatter)
utils_logger.addHandler(utils_handler)
utils_logger.setLevel(logging.DEBUG)
