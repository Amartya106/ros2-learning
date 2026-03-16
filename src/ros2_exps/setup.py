from setuptools import find_packages, setup

package_name = 'ros2_exps'

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
    maintainer='amartya',
    maintainer_email='amartyamishra@live.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "sin_wave = ros2_exps.sine_wave_pub:main",
            "sin_turtle = ros2_exps.sine_turtle:main"            
        ],
    },
)
