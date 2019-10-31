BootStrap: docker
From: ubuntu:16.04

%help
  Special thanks goes to https://gist.github.com/lvisintini/e07abae48f099b913f9cf1c1f0fe43ba

%labels
  Maintainer: Chris Cotter
  Version v0.01

%setup
  mkdir ${SINGULARITY_ROOTFS}/opt/code/

%files
  ./* /opt/code

%post
  #######################################################################################
  # Install dependencies
  apt update
  apt install -y \
      wget \
      build-essential \
      python3 \
      python-setuptools \
      python-numpy \
      python-opencv \
      unzip \
      glew-utils \
      imagemagick \
      libgtk2.0-dev \
      libglew-dev \
      libdevil-dev \
      libboost-all-dev \
      libatlas-cpp-0.6-dev \
      libatlas-dev \
      libatlas-base-dev \
      liblapack3 \
      libblas3 \
      libcminpack-dev \
      libgfortran3 \
      libmetis-edf-dev \
      libparmetis-dev \
      libjpeg-turbo8 \
      libgsl-dev \
      freeglut3-dev
      

  cd /opt/code
  make clean
  make all
  
  mkdir /lscratch /db /work /scratch
  
  chmod -R a+rwx /opt/code

%environment
  PATH=$PATH:/opt/code/vsfm/bin/
  export PATH
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/code/vsfm/bin/
  export LD_LIBRARY_PATH

%runscript
  #/opt/code/vsfm/bin/VisualSFM "$@"
  
   echo "Arguments received: $*"
   exec /usr/bin/python "$@"

%test
  #----------------------------------------------------------
  # commands to be executed within container at close of bootstrap process
  #----------------------------------------------------------
   python --version
   #python requirement.py 
