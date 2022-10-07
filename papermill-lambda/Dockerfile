FROM lambci/lambda:python3.8

ENV IPYTHONDIR '/tmp/ipythondir'

USER root
COPY requirements.txt .
RUN pip install -r requirements.txt
USER sbx_user1051
