# Create environment
python -m venv .venv

# Activate it (Windows PowerShell):
.venv\Scripts\activate

# Enable ExecutionPolicy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Setup kernel
.\.venv\Scripts\python.exe -m pip install ipykernel 
.\.venv\Scripts\python.exe -m ipykernel install --user --name kaggle-competition --display-name "Python (.venv)"

# Install packages
pip install numpy pandas matplotlib scikit-learn scikit-elcs scipy jupyter ipykernel torch torchvision

# Using CUDA
pip install --force-reinstall torch torchvision --index-url https://download.pytorch.org/whl/cu126