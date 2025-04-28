# Create a python wheel with Poetry using Pybind11 and Cmake

I cobbled this together from multiple places this is my attempt to refine it into a minimal example.

## Use

>
> `poetry lock`
>
> `poetry build`
>
> Check for the wheel `.whl` in dist there should also be a `.tar.gz`.
> The wheel will have a different name depending on the platform you build on.
>
> Copy that wheel to wherever you want to use it and run
>
> `pip3 install *.whl`
>
> The example module is now avalible
>
>
> > from pb_ex import example
> >
> > print(example.add(1, 2))
>
> This should output 3

## Detail

The top level folder containing this README has the pyproject.toml.
Using poetry lock you will resolve the dependencies on your system.

Building the project invokes the build script in pb_ex.
The build script parses the environment it is running in and gets the pybind11 directory from python site packages.
It then runs the configuration build and install for cmake.

The CMakeLists.txt firstly resolves the pybind11 settings allowing it to configure itself.
See their documentation for a full explanation.
The step I find useful is giving the pybind11_DIR using the `PYTHON_SITE_PACKAGES` we passed from the build script.

After running `poetry build` the `.so` file is created in the pb_ex folder.
We tell poetry to include this so file in both the sdist and the wheel.

>
> [tool.poetry]
> include = [
> { path = "pb_ex/*.so", format = ["sdist", "wheel"] }
> ]
>

Poetry will then bundle this into the wheel and source and the module is available as `pb_ex.example`

Note: I have in some cases been able to make this work without the include path but it then seems to invariably go wrong in the future.

## Additionally

Potentially preferably another structure with:

```
pb-ex/
    pyproject.toml
    build.py
    CMakeLists.txt
    pb_ex/
        __init__.py
    src/
        source.cpp
        source.h
        pybind_boiler.cpp
```

This separates the c++, build.py, and CMakeLists from the python module pb_ex.
Then the .so file created by CMakeLists must then be targeted to exist within pb_ex.
