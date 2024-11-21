from setuptools import find_packages, setup

package_name = 'me495_cvbridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Matthew Elwin',
    maintainer_email='elwin@northwestern.edu',
    description='Demonstration of ROS 2 cv_bridge',
    license='GPLv3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bridge = me495_cvbridge.bridger:main'
        ],
    },
)
