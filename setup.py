from setuptools import setup
setup(
    name='image_encryption',
    version='0.1',
    packages=['app', 'encryptor'],
    py_modules=['main'],
    install_requires=[
        # Gerekli bağımlılıkları burada belirtebilirsiniz.
        'Crypto',
        'argparse'
    ],
    entry_points={
        'console_scripts': {
            'image_encryption = main:main',
        },
    },
    author='Muhammed Ali Bekdaş',
    author_email='m.ali.software.dev@gmail.com',
    description='Image Encryption Application For Linux',
    url='',
)