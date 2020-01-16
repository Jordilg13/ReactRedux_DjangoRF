FROM nvidia/cuda:10.1-cudnn7-devel

# custom
# RUN apt install nvidia-driver-418

# Install face recognition dependencies

RUN apt update -y; apt install -y \
git \
cmake \
libsm6 \
libxext6 \
libxrender-dev \
python3 \
python3-pip

RUN pip3 install scikit-build

# Install compilers

RUN apt install -y software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test
RUN apt update -y; apt install -y gcc-6 g++-6

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 50
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-6 50

#Install dlib 
RUN rm -rf /dlib
RUN git clone --single-branch https://github.com/davisking/dlib.git
RUN mkdir -p /dlib/build

RUN cmake -H/dlib -B/dlib/build -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1
RUN cmake --build /dlib/build

RUN cd /dlib; python3 /dlib/setup.py install

# Install the face recognition package

RUN pip3 install face_recognition


# DJANGO
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt install libpq-dev python-dev -y
WORKDIR /drf
ADD ./requirements.txt /drf/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /drf/requirements.txt
# CMD python3 manage.py runserver 0.0.0.0:8000