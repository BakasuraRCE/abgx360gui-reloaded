cmake_minimum_required(VERSION 3.21)
if(WIN32)
set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
endif()

project(abgx360gui)


set(CMAKE_CXX_STANDARD 23)

include(CMakeRC.cmake)
cmrc_add_resource_library(foo-resources
        ALIAS foo::rc
        NAMESPACE foo
        src/Images/logo_reloaded.png
        src/Images/favicon.png
        src/Images/info_tip.png
        src/Images/open_button.png
        src/Images/save_button.png
        src/Images/save_button_disabled.png
        src/Images/launch_button_normal.png
        src/Images/launch_button_click.png
        src/Images/launch_button_over.png
        src/Images/dotted_open_button.png
        src/Images/dotted_open_button_disabled.png)

include_directories(src)

if (UNIX)
    # Set GTK3 for wxWidgets
    set(wxWidgets_CONFIG_OPTIONS --toolkit=gtk3)
endif ()
# Find wxWidgets
# Note that for MinGW users the order of libs is important!
find_package(wxWidgets REQUIRED net gl core base adv)
include(${wxWidgets_USE_FILE})

# Add executable
add_executable(abgx360gui WIN32
        src/abgx360gui.cpp
        src/abgx360gui.h
        src/abgx360guiApp.cpp
        src/abgx360guiApp.h
        abgx360gui.rc)

# Link wxWidgets deps
# and for each of your dependent executable/library targets:
target_link_libraries(abgx360gui PRIVATE ${wxWidgets_LIBRARIES})
# Link resources
target_link_libraries(abgx360gui PRIVATE foo::rc)