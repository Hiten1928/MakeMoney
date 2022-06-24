#Deriving the latest base image
FROM python:latest
RUN pip install --upgrade pip && \
    pip install pandas && \
    pip install pandas_datareader && \
    pip install datetime

#Labels as key value pair
LABEL Maintainer="hiten3008"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /Users/hitengupta/Documents/MakeMoney

#to COPY the remote file at working directory in container
COPY app ./
COPY data ./

# Now the structure looks like this '/usr/app/src/test.py'


#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python3", "./app/money.py", "tail -f /dev/null"]
# CMD tail -f /dev/null