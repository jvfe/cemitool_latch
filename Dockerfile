FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/latch-base:6839-main

# Install R
RUN apt-get update
RUN apt-get install -y software-properties-common &&\
    add-apt-repository "deb http://cloud.r-project.org/bin/linux/debian buster-cran40/" &&\
    apt-get install -y r-base r-base-dev libxml2-dev libcurl4-openssl-dev libssl-dev wget
RUN apt-get install -y r-cran-rcppeigen r-cran-catools r-cran-latticeextra
RUN add-apt-repository "deb http://deb.debian.org/debian bullseye main"
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key '95C0FAF38DB3CCAD0C080A7BDC78B2DDEABC47B7'
RUN apt-get update
RUN apt-get install -y r-cran-wgcna r-cran-network r-cran-sna 

# Install some packages (replace with your own)
RUN R -e "install.packages('BiocManager')"
RUN R -e "install.packages('remotes')"
RUN R -e "remotes::install_github('r-lib/rlang')" &&\
    R -e "install.packages(c('pillar', 'vctrs', 'pillar', 'tibble', 'dplyr'))" &&\
    R -e "BiocManager::install('CEMiTool', force = TRUE)"

# You can add other R files here by copying them over.
# You can then run them within your tasks.
COPY cemitool.R /root/cemitool.R

# STOP HERE:
# The following lines are needed to ensure your build environement works
# correctly with latch.
RUN python3 -m pip install --upgrade latch
COPY wf /root/wf
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
WORKDIR /root
