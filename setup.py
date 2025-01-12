from setuptools import find_packages, setup

package_name = 'isdc_sensors'

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
    maintainer='karthikeya',
    maintainer_email='davasamkarthikeya@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ms8607 = isdc_sensors.ms8607_test:main',
            'dfrobot_mics = DFRobot_MICS_All:main'
        ],
    },
)
