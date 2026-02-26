def php_http_build_query(data, parent_key='', result=None):
    if result is None:
        result = {}

    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}[{key}]" if parent_key else key
            php_http_build_query(value, new_key, result)

    elif isinstance(data, list):
        for index, value in enumerate(data):
            new_key = f"{parent_key}[{index}]"
            php_http_build_query(value, new_key, result)

    else:
        result[parent_key] = str(data)

    return result
