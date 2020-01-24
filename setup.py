from distutils.core import setup

setup(
    name='pyexecutors',
    packages=['pyexecutors', 'pyexecutors.executors', 'pyexecutors.holders', 'pyexecutors.utils'],
    version='0.1.1',
    license='MIT',  
    description=
    """
         a light-weight library to efficiently run series of 
        asynchronous and synchronous tasks concurrently
        without worrying about managing different threads
        on your own.
        
    """,  
    author='TANMAY MAJUMDAR',  
    author_email='tanmaymajumdar5612@gmail.com',  
    url='https://github.com/tanmay23235616/pyexecutors',  
    download_url='https://github.com/tanmay23235616/pyexecutors/archive/0.1.0.tar.gz',
    keywords=['PYEXECUTOR', 'TANMAY23235616', 'MULTITHREADING'],  
    classifiers=[
        'Development Status :: 4 - Beta',
        
        'Intended Audience :: Developers',  
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3',  
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
