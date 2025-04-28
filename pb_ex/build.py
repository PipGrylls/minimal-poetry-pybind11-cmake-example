import os
import subprocess
import site


def main():
    # This script executes the Cmakelists.txt file in the current directory
    # and builds the project using CMake.

    # Define the source and build directories 
    source_dir = os.path.dirname(os.path.abspath(__file__))  # The directory of the current script
    build_dir = os.path.join(source_dir, 'build')  # Make a build directory in the same directory as the script
    os.makedirs(build_dir, exist_ok=True)  # Create the build directory if it doesn't exist

    # Get the location of the python site-packages directory
    python_site_dir = site.getsitepackages()[0]  # This is required to pass pybind11 config to CMake
    print(f"Python site-packages directory: {python_site_dir}")

    # Configure the project using CMake
    subprocess.check_call([
        'cmake',
        '-S', source_dir,
        '-B', build_dir,
        '-DPYTHON_SITE_PACKAGES=' + python_site_dir,
    ])
    print("CMake configuration complete.")

    # Build the project using CMake
    subprocess.check_call([
        'cmake',
        '--build', build_dir
    ])
    print("Build complete.")

    # Install the built shared object file to the py_subs directory
    print("Installing the built shared object file")
    subprocess.check_call([
        'cmake',
        '--install', build_dir,
        '--prefix', f'{source_dir}/',
    ])
    print("Installation complete")


if __name__ == '__main__':
    main()
