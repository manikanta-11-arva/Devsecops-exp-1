import sys
import sklearn
import pandas as pd

def check_environment():
    print("Python executable :", sys.executable)
    print("Python version :", sys.version.split()[0])
    print("scikit-learn :", sklearn.__version__)
    print("pandas :", pd.__version__)
    print("ML environment is ready!")

if __name__ == "__main__":
    check_environment()
