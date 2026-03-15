from setuptools import find_packages, setup

package_name = 'my_py_pkg'

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
            "py_node = my_py_pkg.my_first_node:main",
            "num_pub = my_py_pkg.number_publisher:main",
            "num_count = my_py_pkg.number_counter:main",
            "my_pub = my_py_pkg.my_own_pub:main",
            "reset_counter_client = my_py_pkg.reset_counter_clinet:main"

        ],
    },
)
