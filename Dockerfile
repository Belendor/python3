FROM python
ADD . .
RUN pip install flask flask-restful 
EXPOSE 5000
CMD [ "python", "pingAPI.py" ]