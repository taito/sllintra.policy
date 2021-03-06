from setuptools import find_packages
from setuptools import setup


setup(
    name='sllintra.policy',
    version='0.1',
    description="Turns Plone site into SLL intra site.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='https://github.com/taito/sllintra.policy',
    license='None-free',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['sllintra'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.PloneFormGen',
        'eea.facetednavigation',
        'setuptools',
        'sllintra.content',
        'sllintra.theme'],
    extras_require={'test': ['Products.CMFPlacefulWorkflow', 'hexagonit.testing']},
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
