# -*- coding: utf-8 -*-
from os.path import join

from django.template.defaultfilters import slugify


def uploadFilename(basepath, instance, filename):
    """
    Helper to upload files in FileField fields.

    To use in FiledField argument 'upload_to':
        upload_to=partial(uploadFilename, basepath )
    Where basepath is the path where the file will save.

    @param basepath: Base path to save the file (list or string)
    @param instance: Model instance
    @param filename: The filename that was originally given to the file.
    @return: string with file path.
    """
    if isinstance(basepath, basestring):
        # Converts to lowercase, removes non-word characters
        # (alphanumerics and underscores) and converts spaces
        # to hyphens. Also strips leading and trailing whitespace.
        basepath = slugify(basepath)
    else:
        # if basepath is a list
        basepath = join(*map(slugify, basepath))

    return join(basepath, filename)
