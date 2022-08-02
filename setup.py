from setuptools import setup

package_name = 'imgpub'

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
    maintainer='sachan0v0',
    maintainer_email='okwlb0v0sada@gmail.com',
    description='image pub/sub',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_publisher = img_pub:main'
            'image_subscriber = img_sub:main'
            
        ],
    },
)
