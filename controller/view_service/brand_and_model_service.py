import logging

from database.dao.stock import brand_handler, model_handler

logger = logging.getLogger(__name__)


def get_brand_by_name(name: str):
    brand_in_db = brand_handler.get_brand_by_name(name)
    if brand_in_db:
        return brand_in_db['id']
    else:
        logger.info('新增商品品牌')
        return brand_handler.add_brand(name)


def get_model_by_name(brand_id, model_name):
    model_in_db = model_handler.get_model_by_name(model_name, brand_id)
    if model_in_db:
        return model_in_db['id']
    else:
        logger.info('新增商品型号')
        return model_handler.add_model(model_name, brand_id)


def get_all_brand():
    brands = []
    for brand in brand_handler.get_all_brand():
        brands.append(brand['brand_name'])

    return brands


def get_all_model():
    models = []
    for model in model_handler.get_all_model():
        models.append(model['model_name'])
    return models
