from distutils.core import setup

setup(
    name='pyexecutors',
    packages=['pyexecutors'],
    version='0.0.1',
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description=
    """
         a lite-weight library to efficiently run series of 
        asynchronous and synchronous tasks concurrently
        without worrying about managing different threads
        in your own.
        
    """,  # Give a short description about your library
    author='TANMAY MAJUMDAR',  # Type in your name
    author_email='tanmaymajumdar5612@gmail.com',  # Type in your E-Mail
    url='https://github.com/tanmay23235616/pyexecutors',  # Provide either the link to your github or to your website
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',  # I explain this later on
    keywords=['SOME', 'MEANINGFULL', 'KEYWORDS'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'validators',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
