# build_files.sh
pip install -r requirements.txt
pip install whitenoise
python3.9 manage.py collectstatic
