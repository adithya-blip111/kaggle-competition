# Create environment
python -m venv .venv

# Activate it (Windows PowerShell):
.venv\Scripts\activate

# Enable ExecutionPolicy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Setup kernel
.\.venv\Scripts\python.exe -m pip install ipykernel 
.\.venv\Scripts\python.exe -m ipykernel install --user --name data_ai_project --display-name "Python (.venv)"

# Install packages
pip install numpy pandas scikit-learn matplotlib jupyter scipy

# Install packages
pip install -r requirements.txt