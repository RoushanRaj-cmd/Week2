from setuptools import find_packages, setup

package_name = 'turtlebot_control'

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
    maintainer='roushan',
    maintainer_email='roushan@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'constant_velocity = turtlebot_control.constant_velocity:main',
            'move_to_goal = turtlebot_control.move_to_goal:main',
            'obstacle_avoidance = turtlebot_control.obstacle_avoidance:main',
            'keyboard_control = turtlebot_control.keyboard_control:main',
        ],
    },
)
