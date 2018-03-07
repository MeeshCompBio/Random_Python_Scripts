#These commands are meant to be run from the linux terminal
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
#follow the prompts and say yes to adding local path to .bashrc

#source .bashrc to take .bashrc changes into effect
source ~/.bashrc

#create env, this one is called MutMot using python3 followed by desired pacakges
conda create --name CSBIO python=3 numpy scipy pandas matplotlib

# Start environment
source activate CSBIO

# Exit environment
source deactivate

# How to list all of your environments
conda info --envs

# Install specific package and version to  an environment
conda install --name CSBIO scipy=0.15.0

# Remove specific environment and all packages
conda remove --name CSBIO --all

