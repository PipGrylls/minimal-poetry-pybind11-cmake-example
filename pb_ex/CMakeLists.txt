# Simple CMakeLists.txt for building a Pybind11 module
cmake_minimum_required(VERSION 3.4...3.22)
project(pb_ex VERSION 0.1.0 LANGUAGES CXX)

message("Building example module")

# Find pybind11 package
set(PYBIND11_FINDPYTHON ON)
# Assuming you are running in a virtual environment and the site-packages directory is set from build.py
set(pybind11_DIR "${PYTHON_SITE_PACKAGES}/pybind11/share/cmake/pybind11")
message("pybind11_DIR: ${pybind11_DIR}")
find_package(pybind11 CONFIG REQUIRED)

# Get the cpp source files
# Extend this with further .cpp or .h files as required for compilation
file(GLOB EXAMPLE_SRC
    src/example.cpp
)
message("EXAMPLE_SRC: ${EXAMPLE_SRC}")

# Instruct pybind11 to create a module named pb_ex
pybind11_add_module(example ${EXAMPLE_SRC})
# Link the module with the pybind11 headers
target_link_libraries(example
    PUBLIC
        pybind11::headers
)

# Set the include directories for the module
target_include_directories(example
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)

# Set the RPATH for the module
set_target_properties(example PROPERTIES
    INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib"
    BUILD_WITH_INSTALL_RPATH TRUE
    INSTALL_RPATH_USE_LINK_PATH TRUE
    BUILD_RPATH_USE_ORIGIN TRUE
)

# Install the module
install(TARGETS example
    EXPORT exampleTargets
    LIBRARY DESTINATION ${CMAKE_SOURCE_DIR}
    ARCHIVE DESTINATION ${CMAKE_SOURCE_DIR}
    RUNTIME DESTINATION ${CMAKE_SOURCE_DIR}
)
