def statement_file(ts_code, stat, year, quarter):
    return 'statements/{}/{}/{}/{}'.format(ts_code, year, quarter, stat)


def file_path(data_path: str, type: str):
    return '{}/{}'.format(data_path, type)
