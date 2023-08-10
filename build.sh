set -o errexit

# poetry install
pip install -r requirements.txt

python manage.py collectstatic --no-imput
python manage.py migrate