from setuptools import find_packages, setup

setup(
        name='pyobjc_trac_examples', version='1.0',
        packages=find_packages(),
        entry_points = """
        [trac.plugins]
        pyobjc_trac_examples = pyobjc_trac_examples
        """,
        package_data={'pyobjc_trac_examples': ['templates/*.html']},
        zip_safe=False,
)
