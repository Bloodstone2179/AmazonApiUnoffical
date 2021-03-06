from distutils.core import setup
setup(
  name = 'AmazonApiUnoffical',         # How you named your package folder (MyLib)
  packages = ['AmazonApiUnoffical'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'a module for amazon that gets the price and name of the product',   # Give a short description about your library
  author = 'tim harris',                   # Type in your name
  author_email = 'your.email@domain.com',      # Type in your E-Mail
  url = 'https://github.com/Bloodstone2179/AmazonApiUnoffical',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Bloodstone2179/AmazonApiUnoffical/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['AMAZON', 'API', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)