DB_NAME="project_database"
DB_USER="Alisa"
DB_PASSWORD="2003"
DB_OWNER="Alisa"

# creating db
sudo -u postgres createdb $DB_NAME

# creating the user and settng the password
sudo -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"

# set the owner of the db
sudo -u postgres psql -c "ALTER DATABASE $DB_NAME OWNER TO $DB_OWNER;"


