FROM iterativeai/cml:latest-gpu

RUN python -m pip install --upgrade pip
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt