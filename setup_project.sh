#! /bin/sh

echo "Starting the setup script"

mkdir -p src data output

cat > src/data_analysis.py << EOF
#! /usr/bin/python
EOF

cat > data/students.csv << EOF
#! /usr/bin/python

#Input data for students
name, age, grade, subject
Amy, 22, 53, Data Science
Paul, 22, 67, Data Science
Pia, 22, 93, Psychology
Mark, 25, 80, Psychology
Johnny, 23, 88, History
Peter, 25, 95, Anatomy
Jenny, 27, 75, History
Theo, 25, 90, Data Science
Lucy, 23, 95, Math
Elizabeth, 24, 100, Math