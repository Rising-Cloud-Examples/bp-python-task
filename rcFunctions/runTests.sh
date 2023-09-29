for f in /app/app/rcTests/requests/*; do \
    cp $f ./request.json && \
    python3 main.py && \
    cp ./response.json /app/app/rcTests/responses/${f#/app/app/rcTests/requests/}; \
done