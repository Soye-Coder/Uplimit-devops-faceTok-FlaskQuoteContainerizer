FROM python:3.8-slim-buster
WORKDIR /app
COPY . .
COPY /workspaces/Uplimit-devops-faceTok-FlaskQuoteContainerizer/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]