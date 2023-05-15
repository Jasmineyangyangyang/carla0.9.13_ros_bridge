from setuptools import setup

package_name = 'set_transform'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zhang',
    maintainer_email='zhang@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
    "transform_manualset=set_transform.manual_set:main",
    "transform_autoset=set_transform.auto_set:main",
    "test1=set_transform.test1:main",
    "test2=set_transform.test2:main",
        ],
    },
)
