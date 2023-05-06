from setuptools import setup

package_name = 'webserver'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zach',
    maintainer_email='zachfsx83@gmail.com',
    description='Minimal webserver implementation for live threshold editing',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [

            'webserver = webserver.app:main'

        ],
    },
)
