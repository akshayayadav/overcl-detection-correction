FROM ubuntu:16.04

RUN apt-get update \
  && apt-get install -y python-pip python-dev \
  && apt-get install -y hmmer \
  && apt-get install -y mafft \
  && apt-get install -y python-numpy \
  && apt-get install -y python-qt4 \
  && apt-get install -y python-lxml \
  && apt-get install -y python-six \
  && apt-get autoremove \
  && apt-get clean

RUN pip install 'ete3==3.1.1'

COPY scripts/overcl-fam-analysis /overcl-fam-analysis
RUN chmod +x /overcl-fam-analysis/*

ADD scripts/FastTreeMP /usr/local/bin/
RUN chmod +x /usr/local/bin/FastTreeMP

ADD scripts/run_analysis.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/run_analysis.sh
