from setuptools import setup

setup(
    name='weather-cli',
    version='1.0.0',
    packages=['weather'],
    entry_points={
        'console_scripts': [
            'weatherat = weather.weather:main',
        ]
    }
)
