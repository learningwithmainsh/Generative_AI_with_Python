# Command to create a Python environment using Conda
conda create --name myenv python=3.11

# To activate this environment, use:
conda activate myenv

# To deactivate an active environment, use:
conda deactivate

# Install packages
conda install numpy pandas

# List all environments
conda env list

# Remove an environment
conda remove --name myenv --all

# List all packages
conda list
