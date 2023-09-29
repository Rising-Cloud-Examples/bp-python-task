cp ./rcTests/requests/$1.json ./request.json
python3 main.py
cp ./response.json ./rcTests/responses/$1.json