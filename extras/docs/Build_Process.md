# Build Process for SAS Studio Custom Steps (suggested)

For any future modifications you wish to apply to your custom steps,  here is a build process that may help you.  
These are **entirely** optional practices.

## Requirements

1. On your workstation, in a directory parallel to the folder containing your custom step, clone the following git repo:

```
git clone https://github.com/SundareshSankaran/py-sas-studio-build-tools.git

cd py-sas-studio-build-tools

```

2. Run the build.sh file located in the repo.  Note that this creates a virtual environment in Python, and then install packages located in the adjoining requirements.txt.

```
./build.sh
```

3. Examine the script inside build.sh.   You will notice some commented lines referring Python scripts in the scripts folder, which helps you in your custom step build process.




