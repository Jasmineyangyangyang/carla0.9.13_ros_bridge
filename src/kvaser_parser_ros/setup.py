from setuptools import setup
import os
from glob import glob

package_name = 'kvaser_parser_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cec20',
    maintainer_email='1021802264@qq.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'write_to_kvaser = kvaser_parser_ros.write_to_kvaser:main',
        'read_from_kvaser = kvaser_parser_ros.read_from_kvaser:main',
        'kvaser_ros = kvaser_parser_ros.kvaser_ros:main',
        'read_from_kvaser_queue  = kvaser_parser_ros.read_from_kvaser_queue:main',
        'read_from_kvaser_adjacent  = kvaser_parser_ros.read_from_kvaser_adjacent:main'
        ],
    },
)
