import pyximport
pyximport.install(language_level=2)

from ._s3FileObject import s3FileObject
#from ._s3aioFileObject import s3aioFileObject as s3FileObject