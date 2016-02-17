from setuptools import setup, find_packages
from commands import docker_build, docker_start, docker_stop, setup_riak

setup(
    name='aioriak',
    version='0.0.1',
    description='Async implementation of Riak DB python client',
    author='Makc Belousov',
    author_email='m.belousov@rambler-co.ru',
    long_description='',
    url='',
    # package_dir={'': ''},
    packages=find_packages('', exclude=('*.tests',)),
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    install_requires=[
        'python3-riak-pb==2.1.0.6',
        'riak==2.3.0',
    ],
    tests_require=['nose==1.3.7',
                   'coverage==4.0.3'],
    cmdclass={
        'docker_build': docker_build,
        'docker_start': docker_start,
        'docker_stop': docker_stop,
        'setup_riak': setup_riak
    }
)
