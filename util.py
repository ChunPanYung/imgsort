"""
Includes various utility functions
"""
def sizeof_fmt(num):
    """ Credit to Fred Cirera
        print human readable file size
    """
    for unit in ['Bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, unit)
        num /= 1024.0
    return num
