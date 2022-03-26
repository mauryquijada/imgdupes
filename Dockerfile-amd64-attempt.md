FROM python:3.6.8-slim-stretch

WORKDIR /app

ENV LD_LIBRARY_PATH /usr/local/lib

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y cmake git libgtk2.0-dev libblas-dev liblapack-dev \
  && rm -rf /var/lib/apt/lists/*

# install ngt
RUN git clone https://github.com/yahoojapan/NGT.git \
  && cd NGT \
  && git checkout v1.7.6 \
  && mkdir build && cd build \
  && cmake .. \
  && make \
  && make install \
  && ldconfig \
  && cd ../python \
  && pip install pybind11-global \
  && python setup.py sdist \
  && pip install dist/ngt-1.4.0.tar.gz

# install hnsw
RUN git clone https://github.com/nmslib/hnsw.git \
  && cd hnsw/python_bindings \
  && pip install numpy pybind11 \
  && python setup.py install

RUN apt-get update \
    && apt-get install -y wget libssl-dev \
  && wget https://github.com/Kitware/CMake/releases/download/v3.19.3/cmake-3.19.3.tar.gz \
  && tar xvzf cmake-3.19.3.tar.gz \
  && cd cmake-3.19.3/ \
  && ./configure \
  && make

RUN git clone https://github.com/facebookresearch/faiss.git \
  && cd faiss

RUN apt-get install -y swig

/app/cmake-3.19.3/bin/cmake -B build -DFAISS_ENABLE_GPU=OFF  -DPython_EXECUTABLE=$(which python3) -DFAISS_OPT_LEVEL=generic -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=ON


make -C build -j faiss


=======
/app/cmake-3.19.3/bin/cmake -B build

/app/cmake-3.19.3/bin/cmake -B build -DCMAKE_CXX_COMPILER=g++ -DFAISS_ENABLE_GPU=OFF  -DPython_EXECUTABLE=$(which python3) -DFAISS_OPT_LEVEL=generic -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=ON
  

https://github.com/pybind/pybind11/issues/698

