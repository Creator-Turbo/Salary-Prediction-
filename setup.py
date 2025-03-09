from setuptools import setup, find_packages

setup(
    name="salary_prediction",  # Use a valid package name (no spaces)
    version="0.1",  
    author="Bablu Kumar Pandey",
    author_email="bablupandey446@gmail.com",
    description="A machine learning model for salary prediction",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Creator-Turbo/Salary-Prediction-",  # Update if necessary
    packages=find_packages(), 
    include_package_data=True,
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "xgboost",
        "joblib",
        "flask",  # Optional, for deployment
        "mlflow",
        "dvc",
    ],
)
