cmake_minimum_required(VERSION 3.15)
project(r1_model_cpp)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(r1_model_cpp
        lista.cpp
        lista.h
        main.cpp)
