# syntax=docker/dockerfile:experimental
FROM ros:noetic AS base
# Base image for both "builder" and the final output "app"
RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
        apt-get update && apt-get install -y \
        curl \
        git \
        python3-catkin-tools \
        python3-osrf-pycommon \
        python3-pip \
        python3-vcstool \
        stow emacs vim \
        clang-format \
        clangd

RUN --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
        apt-get update -y && \
	apt-get install -y \
	liblog4cxx-dev \
	libopenscenegraph-dev \
	python2-dev \
	python-setuptools \
	g++ gfortran git cmake pkg-config debhelper gettext zlib1g-dev libminizip-dev \
	libxml2-dev liburiparser-dev libpcre3-dev libgmp-dev libmpfr-dev qtbase5-dev \
	libavcodec-dev libavformat-dev libswscale-dev libsimage-dev libode-dev \
	libqhull-dev libann-dev libhdf5-serial-dev liblapack-dev libboost-iostreams-dev \
	libboost-regex-dev libboost-filesystem-dev libboost-system-dev libboost-thread-dev \
	libboost-date-time-dev libboost-test-dev libmpfi-dev ffmpeg libtinyxml-dev \
	libflann-dev sqlite3 libccd-dev python-coverage python-opengl \
	ninja-build cmake-curses-gui silversearcher-ag

# Python dependencies: It is better to hardcode directly instead of
# copying requirements.txt file. This is because the file might change
# (timestamp) without actually changing.
RUN --mount=type=cache,target=/root/.cache/pip \
        python3 -m pip install -U pip && \
        python3 -m pip install \
        msgpack==1.0.0 \
        fastapi==0.61.1 \
        grpcio==1.32.0 \ 
        protobuf==3.13.0 \
        redis==3.5.3 \
        pymongo==3.11.0 \
        uvicorn[standard]==0.12.1 \
        networkx==2.5 \
        lmfit==1.0.1 \
        python-json-logger==2.0.1 \
        requests==2.24.0 \
        typer==0.3.2 \
        serial==0.0.97 \
        pymodbus==2.4.0 \
        aiofiles==0.6.0 \
        websockets==8.1 \
        invoke \
        tqdm==4.50.2 \
        pytest==6.1.1 \
        pytest-mock==3.3.1 \
        mypy==0.782 \
        ipython==7.18.1 \
        jupyter==1.0.0 \
        pandas==1.1.3 \
        mkdocs \
        pymdown-extensions \
        matplotlib \
        ipdb \
        jinja2

# python 2
RUN --mount=type=cache,target=/root/.cache/pip \
        curl https://bootstrap.pypa.io/2.7/get-pip.py --output get-pip.py && python2 get-pip.py  && \
	pip install numpy==1.14.2 sympy==0.7.1 IPython==5.8.0 && \
	pip install scipy==1.1.0

FROM base AS builder
RUN git clone https://github.com/bulletphysics/bullet3.git && mkdir bullet3/build && \
	cd bullet3/build && \
	git checkout tags/2.82 && \
	cmake .. -GNinja -DINSTALL_LIBS=ON -DBUILD_SHARED_LIBS=ON -DCMAKE_C_FLAGS=-fPIC -DCMAKE_CXX_FLAGS=-fPIC && \
	ninja -j4 && ninja install

RUN git clone https://github.com/rdiankov/collada-dom.git && mkdir collada-dom/build
RUN cd collada-dom/build && cmake .. -GNinja && ninja -j4 && ninja install

RUN git clone https://github.com/Tencent/rapidjson.git && mkdir rapidjson/build && \
        cd rapidjson/build && cmake .. -GNinja \
        -DRAPIDJSON_BUILD_EXAMPLES=OFF \
        -DRAPIDJSON_BUILD_DOC=OFF \
        -DRAPIDJSON_BUILD_TESTS=OFF \
        && ninja -j4 && ninja install

RUN git clone https://github.com/rdiankov/assimp.git && mkdir assimp/build && cd assimp/build && \
        cmake .. -GNinja && ninja -j4 && ninja install

RUN git clone https://github.com/rdiankov/fcl.git && mkdir fcl/build && \
        cd fcl/build && git checkout origin/kenjiSpeedUpAdditions && \
        cmake .. -GNinja -DFCL_BUILD_TESTS=OFF && \
        ninja -j4 && ninja install

RUN git clone https://github.com/pybind/pybind11.git && mkdir pybind11/build && cd pybind11/build && \
	git remote add woody https://github.com/woodychow/pybind11.git && \
	git fetch woody && \
	git config --local user.email 'knife-solo@vagrant.example.com' && \
	git config --local user.name 'knife-solo' && \
	git checkout v2.2.4 && \
	git cherry-pick 94824d68a037d99253b92a5b260bb04907c42355 && \
	git cherry-pick 98c9f77e5481af4cbc7eb092e1866151461e3508 && \
	cmake .. -GNinja -DPYBIND11_TEST=OFF -DPythonLibsNew_FIND_VERSION=2 && \
	ninja -j4 && ninja install

RUN git clone https://github.com/rdiankov/openrave.git && mkdir openrave/build && \
	cd openrave/build && \
	git remote add ciel https://github.com/cielavenir/openrave.git && \
	git fetch ciel && \
	git config --local user.email 'knife-solo@vagrant.example.com' && \
	git config --local user.name 'knife-solo' && \
# before using pybind11::dict::keys
	git checkout ec154952fe7c628fe173ea7a9ef454296bda036c   && \
# https://github.com/rdiankov/openrave/pull/706 (fix bulletrave compilation)
	git cherry-pick cb96ec7318af7753e947a333dafe49bf6cacef01 && \
	git cherry-pick 53b90e081139a8d9c903d2e702322ba97a8bc494 && \
# https://github.com/rdiankov/openrave/pull/708 (fix FCL_LDFLAGS)
	git cherry-pick 40d1e31e431523bfd1ec2c0a7c351a008ca93f91  && \
	git cherry-pick 18831785c536f801f1af66fffff7eb7bec60d8e8 && \
# force PythonInterp to 2
	git cherry-pick 03d085f51e3db5b94a1049f09fdfd0c0a981fb42

RUN cd openrave/build && \
	cmake .. -GNinja -DUSE_PYBIND11_PYTHON_BINDINGS=ON -DCMAKE_CXX_FLAGS=-std=gnu++11 -DBoost_NO_BOOST_CMAKE=1 && \
	ninja -j4 && ninja install

FROM base AS app
RUN --mount=type=bind,from=builder,source=bullet3,target=bullet3,rw \
        cd bullet3/build && ninja install
RUN --mount=type=bind,from=builder,source=collada-dom,target=collada-dom,rw \
        cd collada-dom/build && ninja install
RUN --mount=type=bind,from=builder,source=rapidjson,target=rapidjson,rw \
        cd rapidjson/build && ninja install
RUN --mount=type=bind,from=builder,source=assimp,target=assimp,rw \
        cd assimp/build && ninja install
RUN --mount=type=bind,from=builder,source=pybind11,target=pybind11,rw \
        cd pybind11/build && ninja install
RUN --mount=type=bind,from=builder,source=fcl,target=fcl,rw \
        cd fcl/build && ninja install
RUN --mount=type=bind,from=builder,source=openrave,target=openrave,rw \
        cd openrave/build && ninja install
