-- Base de datos SQLite
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone_number TEXT,
    address TEXT,
    date_of_birth DATE,
    course_id INTEGER,
    FOREIGN KEY(course_id) REFERENCES courses(course_id)
);

CREATE TABLE professors (
    professor_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone_number TEXT,
    department TEXT
);

CREATE TABLE administrators (
    admin_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    department TEXT
);

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    department TEXT,
    professor_id INTEGER,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY(professor_id) REFERENCES professors(professor_id)
);

-- Insertar datos
INSERT INTO professors (name, email, phone_number, department) VALUES ('Sergio', 'sergio@gmail.com', '3152828280', 'Mathematics');
INSERT INTO professors (name, email, phone_number, department) VALUES ('Andrés', 'andres@gmail.com', '3142828280', 'Physics');
INSERT INTO professors (name, email, phone_number, department) VALUES ('David', 'david@gmail.com', '3132828280', 'Chemistry');

INSERT INTO courses (course_name, department, professor_id, start_date, end_date) VALUES ('Calculus', 'Mathematics', 1, '2024-02-01', '2024-05-30');
INSERT INTO courses (course_name, department, professor_id, start_date, end_date) VALUES ('Physics I', 'Physics', 2, '2024-02-01', '2024-05-30');
INSERT INTO courses (course_name, department, professor_id, start_date, end_date) VALUES ('Organic Chemistry', 'Chemistry', 3, '2024-02-01', '2024-05-30');

INSERT INTO students (name, email, phone_number, address, date_of_birth, course_id) VALUES ('Lopez', 'Lopez@gmail.com', '3112828280', '123 Main St', '2000-01-15', 1);
INSERT INTO students (name, email, phone_number, address, date_of_birth, course_id) VALUES ('Ajiaco', 'Ajiaco@gmail.com', '3112828240', '456 Elm St', '2001-03-20', 2);
INSERT INTO students (name, email, phone_number, address, date_of_birth, course_id) VALUES ('Pineros', 'Pineros@gmail.com', '3112828284', '789 Oak St', '2002-05-25', 3);

-- Seleccionar estudiantes de un curso específico
SELECT * FROM students WHERE course_id = 1;

-- Seleccionar profesores por nombre
SELECT * FROM professors WHERE name = 'Sergio';

-- Inner Join: Combinar estudiantes con cursos y profesores
SELECT students.name AS student_name, courses.course_name, professors.name AS professor_name
FROM students
INNER JOIN courses ON students.course_id = courses.course_id
INNER JOIN professors ON courses.professor_id = professors.professor_id;

-- Left Join: Listar todos los cursos y los profesores asociados (si los hay)
SELECT courses.course_name, courses.department, professors.name AS professor_name, professors.department AS professor_department
FROM courses
LEFT JOIN professors ON courses.professor_id = professors.professor_id;

-- Right Join: Listar todos los profesores y los cursos que imparten (si los hay)
SELECT professors.name AS professor_name, professors.department AS professor_department, 
       courses.course_name, courses.department
FROM professors
LEFT JOIN courses ON professors.professor_id = courses.professor_id;



-- Eliminar restricciones de clave externa
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;

-- Ahora puedes eliminar la tabla professors
DROP TABLE IF EXISTS professors;
DROP TABLE IF EXISTS administrators;
