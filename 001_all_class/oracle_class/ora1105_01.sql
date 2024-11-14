-- join
-- inner join, equi join, non-equi-join, self join, outer join

-- employees 사원번호, 사원명, 부서번호, 부서명 - departments 을 출력하시오.
SELECT employee_id, emp_name, a.department_id, department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id
;

SELECT * FROM stu_grade;
SELECT * FROM students;

-- 두 테이블간 동일한 컬럼없이 데이터를 가져오는 방법 : non-equi join
-- avg 값을 가지고 다른 컬럼을 다른 테이블에서 가져와 출력
SELECT name, avg, grade FROM students, stu_grade
WHERE FLOOR(avg) BETWEEN loavg AND hiavg
;

-- self join 자신의 테이블을 2번 호출
SELECT a.employee_id, a.emp_name, a.manager_id, b.emp_name manager_name
FROM employees a, employees b
WHERE a.manager_id = b.employee_id
;

SELECT * FROM students;

SELECT * FROM stu;

-- 컬럼 삭제
ALTER TABLE stu DROP COLUMN result;

-- 컬럼 추가
ALTER TABLE stu ADD result VARCHAR(10);

-- avg 의 컬럼을 가지고, stu_grade 활용해서 이 값을 result 컬럼에 모두 입력하시오.
UPDATE stu a SET result = (
    SELECT grade FROM (
        SELECT no, grade FROM stu, stu_grade
        WHERE FLOOR(avg) BETWEEN loavg AND hiavg
    ) b
    WHERE a.no = b.no
);

-- non-equi join update 구문
UPDATE stu SET result = (
    SELECT grade FROM stu_grade
    WHERE FLOOR(avg) BETWEEN loavg AND hiavg
);

SELECT * FROM stu;

-- RANK()
UPDATE stu SET rank = 0;

SELECT no, name, avg, RANK() OVER(ORDER BY avg DESC) AS ranks FROM stu;

-- RANK() 의 결과 값을 rank 컬럼에 모두 입력하시오.
UPDATE stu a SET rank = (
    SELECT ranks FROM (
        SELECT no, RANK() OVER(ORDER BY avg DESC) AS ranks
        FROM stu
    ) b
    WHERE a.no = b.no
);

SELECT * FROM stu
ORDER BY rank
;

-- 107개
SELECT employee_id, emp_name, manager_id FROM employees;

-- null 값을 포함한 개수 : 107개
SELECT manager_id FROM employees;

-- null 값을 제외한 개수 : 106개
SELECT manager_id FROM employees
WHERE manager_id IS NOT NULL
;

-- null 값에 0 출력, CEO
SELECT NVL(manager_id, 0) FROM employees;
SELECT NVL(TO_CHAR(manager_id), 'CEO') manager_id FROM employees;

-- self join manager_id, 매니저의 이름을 출력하시오.
-- self join 106개
-- outer join : 해당 컬럼에 null 값이 존재할 시 null값을 포함해서 출력
SELECT a.employee_id, a.emp_name, a.manager_id, b.emp_name, a.salary
FROM employees a, employees b
WHERE a.manager_id = b.employee_id(+)
;

SELECT * FROM employees
WHERE emp_name = 'Martha Sullivan';

-- 사원번호, 사원명, 부서번호, 부서명 출력하시오.
-- equi-join, employees에 부서번호 null값도 출력하시오.
SELECT employee_id, emp_name, a.department_id, department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id(+)
;

-- ansi cross join
SELECT * FROM employees CROSS JOIN departments;

-- cross join
SELECT * FROM employees, departments;

-- ansi inner join
SELECT a.department_id, department_name
FROM employees a INNER JOIN departments b
ON a.department_id = b.department_id
;

-- ansi join : using
SELECT department_id, department_name
FROM employees INNER JOIN departments
USING (department_id)
;

-- ansi join : natural join - 두개의 공통부분의 컬럼이 있으면 자동으로 인식해서 검색
SELECT department_id, department_name
FROM employees NATURAL JOIN departments;

-- equi-join
SELECT a.department_id, department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id
;

-- outer join ( left, right, full )
SELECT employee_id, emp_name, a.department_id, department_name
FROM employees a LEFT OUTER JOIN departments b
ON a.department_id = b.department_id
;

-- 오라클 outer-join : 두개의 컬럼의 (+)는 에러
SELECT employee_id, emp_name, a.department_id, department_name
FROM employees a, departments b
WHERE a.department_id(+) = b.department_id(+)
;


-- union
SELECT * FROM students;

SELECT * FROM students
WHERE total >= 250; -- 24개

SELECT * FROM students
WHERE name LIKE '%a%'; -- 35개

-- union : 24 + 35 = 59개, 49개 중복은 제외
-- union all : 중복 허용
SELECT * FROM students
WHERE total >= 250
UNION ALL
SELECT * FROM students
WHERE name LIKE '%a%'
;

SELECT * FROM students
WHERE total >= 250 OR name LIKE '%a%'
;

-- UNION : 같은 테이블, 다른테이블 모두 사용이 가능하고 컬럼의 타입만 맞으면 모두 출력
-- 조건 1. 위쪽쿼리문과 아래쪽 쿼리문 개수가 동일
-- 조건 2. 타입 무조건 일치
SELECT employee_id, emp_name FROM employees;
SELECT no, name FROM students;

SELECT employee_id, emp_name, manager_id name FROM employees
UNION
SELECT no, name, kor FROM students
;

-- 자유 게시판 free_board, 공지사항 noticeboard, 이벤트 eventboard, 종합 게시판 totalboard
-- 통합적으로 검색해서 출력하고 싶을 때 union


-- employees department_id가 50인 사원 검색 -> 부서번호, 부서이름
SELECT a.department_id, department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id AND a.department_id = 50
;

-- employees에 salary 5000 and 8000 작은 사원의 부서번호, 부서이름
-- employees에 없는 departments의 부서 검색 -> 부서번호, 부서이름
SELECT department_id, department_name
FROM departments a
WHERE NOT EXISTS (
    SELECT 1 FROM employees b WHERE a.department_id = b.department_id
)
;

-- 두개를 union 하시오

SELECT a.department_id, department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id AND a.department_id = 50
UNION
SELECT department_id, department_name
FROM departments a
WHERE NOT EXISTS (
    SELECT 1 FROM employees b WHERE a.department_id = b.department_id
)
;

DESC member; -- name, mdate
DESC students; -- name, sdate

SELECT name, mdate FROM member
UNION
SELECT name, sdate FROM students
;

SELECT * FROM board;

DROP TABLE board2;

create table board2 (
	bno NUMBER(4),
	btitle VARCHAR2(1000),
	bcontent CLOB,
	id VARCHAR2(30),
	bgroup NUMBER(4),
	bstep NUMBER(4),
	bindent NUMBER(4),
	bhit NUMBER(4),
	bdate DATE,
	bfile VARCHAR2(100)
);
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (1, 'Maury County Airport', 'Software Engineer IV', 'Dex', 1, 0, 0, 0, '2024-07-31', 'Garth');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (2, 'Ras Al Khaimah International Airport', 'Electrical Engineer', 'Thorstein', 2, 0, 0, 0, '2024-11-03', 'Carnoghan');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (3, 'Miller Field', 'Senior Sales Associate', 'Killian', 3, 0, 0, 0, '2023-12-10', 'Soughton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (4, 'Garowe Airport', 'Physical Therapy Assistant', 'Marleah', 4, 0, 0, 0, '2024-01-14', 'Naisey');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (5, 'Kiryat Shmona Airport', 'Junior Executive', 'Boothe', 5, 0, 0, 0, '2024-01-13', 'Bassano');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (6, 'Playa Baracoa Airport', 'Software Consultant', 'Alfred', 6, 0, 0, 0, '2024-09-22', 'Houston');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (7, 'Southampton Airport', 'Media Manager IV', 'Goddard', 7, 0, 0, 0, '2024-05-21', 'Stroton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (8, 'Nushki Airport', 'Account Representative I', 'Jehu', 8, 0, 0, 0, '2024-07-27', 'Ginsie');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (9, 'Kashan Airport', 'Safety Technician IV', 'Reggie', 9, 0, 0, 0, '2024-01-02', 'Gillingham');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (10, 'Land''s End Airport', 'Teacher', 'Grace', 10, 0, 0, 0, '2024-07-02', 'Dinnington');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (11, 'Marau Airport', 'Senior Sales Associate', 'Carrissa', 11, 0, 0, 0, '2024-09-26', 'Vannucci');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (12, 'Paros National Airport', 'Computer Systems Analyst IV', 'Charline', 12, 0, 0, 0, '2024-08-30', 'Pearn');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (13, 'Kazan International Airport', 'Web Designer IV', 'Petra', 13, 0, 0, 0, '2024-05-25', 'Tench');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (14, 'Abadan Airport', 'Social Worker', 'Guenevere', 14, 0, 0, 0, '2023-12-25', 'Whatford');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (15, 'Alerta Airport', 'Human Resources Manager', 'Rainer', 15, 0, 0, 0, '2023-12-13', 'Kagan');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (16, 'Ambatolhy Airport', 'Statistician II', 'Clemence', 16, 0, 0, 0, '2024-07-25', 'Abelovitz');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (17, 'Antrim County Airport', 'Graphic Designer', 'Atlanta', 17, 0, 0, 0, '2024-01-24', 'Puvia');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (18, 'Dayton-Wright Brothers Airport', 'Financial Analyst', 'Meriel', 18, 0, 0, 0, '2024-06-24', 'Towl');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (19, 'Caransebeş Airport', 'Media Manager III', 'Eada', 19, 0, 0, 0, '2023-11-12', 'Foresight');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (20, 'Kédougou Airport', 'Mechanical Systems Engineer', 'Franky', 20, 0, 0, 0, '2024-06-26', 'Connell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (21, 'Hosea Kutako International Airport', 'Operator', 'Aleta', 21, 0, 0, 0, '2024-06-04', 'O''Shields');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (22, 'Norsup Airport', 'Accountant I', 'Lucky', 22, 0, 0, 0, '2024-04-08', 'Peatman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (23, 'Kota Kinabalu International Airport', 'Business Systems Development Analyst', 'Wolf', 23, 0, 0, 0, '2024-11-03', 'Whymark');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (24, 'Yeva Airport', 'Systems Administrator I', 'Germain', 24, 0, 0, 0, '2024-06-13', 'Burril');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (25, 'Ampara Airport', 'Software Consultant', 'Costanza', 25, 0, 0, 0, '2024-01-11', 'De Giorgis');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (26, 'Madeira Airport', 'Executive Secretary', 'Jeane', 26, 0, 0, 0, '2024-05-01', 'Northedge');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (27, 'Manang Airport', 'Electrical Engineer', 'Ramona', 27, 0, 0, 0, '2024-10-30', 'Camellini');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (28, 'Dirranbandi Airport', 'Teacher', 'Evelyn', 28, 0, 0, 0, '2024-10-22', 'Smitherham');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (29, 'Chevak Airport', 'Senior Editor', 'Alfi', 29, 0, 0, 0, '2024-08-05', 'Skiggs');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (30, 'Along Airport', 'Legal Assistant', 'Sinclare', 30, 0, 0, 0, '2024-08-31', 'Jay');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (31, 'Tongliao Airport', 'Graphic Designer', 'Randi', 31, 0, 0, 0, '2024-06-01', 'Nias');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (32, 'Videira Airport', 'Social Worker', 'Alfi', 32, 0, 0, 0, '2024-06-27', 'Rodge');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (33, 'Lawrenceville Vincennes International Airport', 'Product Engineer', 'Ortensia', 33, 0, 0, 0, '2024-10-19', 'Cornew');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (34, 'St Marys Municipal Airport', 'Health Coach III', 'Edik', 34, 0, 0, 0, '2024-07-31', 'Greenway');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (35, 'Pimaga Airport', 'Nuclear Power Engineer', 'Melantha', 35, 0, 0, 0, '2024-06-07', 'Eixenberger');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (36, 'Sand Point Airport', 'Automation Specialist II', 'Mario', 36, 0, 0, 0, '2024-10-07', 'Szanto');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (37, 'Syangboche Airport', 'Tax Accountant', 'Goran', 37, 0, 0, 0, '2024-06-27', 'Height');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (38, 'Healy Lake Airport', 'Librarian', 'Mela', 38, 0, 0, 0, '2024-06-02', 'Collough');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (39, 'Midgard Airport', 'Database Administrator III', 'Bambie', 39, 0, 0, 0, '2024-05-09', 'Verduin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (40, 'Heglig Airport', 'Programmer IV', 'Bernelle', 40, 0, 0, 0, '2024-07-04', 'Sidry');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (41, 'Mossel Bay Airport', 'Health Coach IV', 'Perice', 41, 0, 0, 0, '2024-06-29', 'Moye');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (42, 'Siwo Airport', 'VP Marketing', 'Dallis', 42, 0, 0, 0, '2024-02-04', 'McGiff');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (43, 'Danilo Atienza Air Base', 'Speech Pathologist', 'Thaine', 43, 0, 0, 0, '2024-01-19', 'Tribbeck');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (44, 'Shelby Airport', 'Assistant Media Planner', 'Francyne', 44, 0, 0, 0, '2023-12-13', 'Crookshanks');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (45, 'Gage Airport', 'GIS Technical Architect', 'Hyacintha', 45, 0, 0, 0, '2023-12-23', 'Hearnes');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (46, 'Gelephu Airport', 'Internal Auditor', 'Hanny', 46, 0, 0, 0, '2024-09-12', 'McJerrow');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (47, 'Sugraly Airport', 'Chemical Engineer', 'Quentin', 47, 0, 0, 0, '2023-11-11', 'Brydell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (48, 'Myrtle Beach International Airport', 'Senior Developer', 'Karrah', 48, 0, 0, 0, '2024-03-16', 'McKue');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (49, 'Rustaq Airport', 'Accounting Assistant IV', 'Stepha', 49, 0, 0, 0, '2024-10-10', 'Charity');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (50, 'Southwest Oregon Regional Airport', 'Design Engineer', 'Marcille', 50, 0, 0, 0, '2024-08-16', 'Philbin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (51, 'New Stuyahok Airport', 'Data Coordinator', 'Armand', 51, 0, 0, 0, '2024-04-10', 'Bianco');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (52, 'Rabil Airport', 'Clinical Specialist', 'Abelard', 52, 0, 0, 0, '2024-03-23', 'D''eathe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (53, 'Walvis Bay Airport', 'Food Chemist', 'Janine', 53, 0, 0, 0, '2024-01-23', 'Klousner');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (54, 'Willow Airport', 'Executive Secretary', 'Tamar', 54, 0, 0, 0, '2024-02-10', 'Nanuccioi');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (55, 'Maquinchao Airport', 'Staff Scientist', 'Jobina', 55, 0, 0, 0, '2024-03-27', 'Danshin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (56, 'Smithton Airport', 'Structural Analysis Engineer', 'Pablo', 56, 0, 0, 0, '2024-03-20', 'Dulwitch');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (57, 'Los Menucos Airport', 'Health Coach IV', 'Ashlin', 57, 0, 0, 0, '2023-12-06', 'Serot');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (58, 'Jersey Airport', 'Occupational Therapist', 'Sarene', 58, 0, 0, 0, '2024-02-27', 'Fullard');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (59, 'Mikkeli Airport', 'Research Associate', 'Juana', 59, 0, 0, 0, '2024-08-11', 'Wolver');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (60, 'Granville Airport', 'Computer Systems Analyst II', 'Perl', 60, 0, 0, 0, '2024-05-14', 'Barkess');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (61, 'Mont Joli Airport', 'Sales Associate', 'Bradley', 61, 0, 0, 0, '2024-01-08', 'Crosi');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (62, 'Moabi Airport', 'Marketing Manager', 'Kiah', 62, 0, 0, 0, '2024-01-04', 'Wardel');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (63, 'Provo Municipal Airport', 'Paralegal', 'Mallory', 63, 0, 0, 0, '2024-03-26', 'Nashe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (64, 'Belgorod International Airport', 'Programmer III', 'Lory', 64, 0, 0, 0, '2024-04-24', 'Bowdrey');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (65, 'Northern Peninsula Airport', 'Professor', 'Augustin', 65, 0, 0, 0, '2023-12-01', 'Mantrip');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (66, 'Makemo Airport', 'Chief Design Engineer', 'Karia', 66, 0, 0, 0, '2024-07-06', 'Leppingwell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (67, 'Croker Island Airport', 'Software Test Engineer III', 'Baily', 67, 0, 0, 0, '2024-07-07', 'Vader');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (68, 'Vestmannaeyjar Airport', 'Electrical Engineer', 'Whit', 68, 0, 0, 0, '2024-03-28', 'Gill');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (69, 'Buri Ram Airport', 'Executive Secretary', 'Renato', 69, 0, 0, 0, '2023-11-07', 'Krug');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (70, 'Brochet Airport', 'Research Nurse', 'Dyanna', 70, 0, 0, 0, '2024-04-29', 'Milbourn');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (71, 'Mbarara Airport', 'Structural Analysis Engineer', 'Sydney', 71, 0, 0, 0, '2024-05-07', 'Rendell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (72, 'Manchester-Boston Regional Airport', 'Teacher', 'Jose', 72, 0, 0, 0, '2024-10-29', 'Northover');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (73, 'Kushiro Airport', 'Financial Advisor', 'Lyle', 73, 0, 0, 0, '2024-07-16', 'Lockyer');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (74, 'Ulusaba Airport', 'Chemical Engineer', 'Marti', 74, 0, 0, 0, '2023-12-06', 'Readman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (75, 'Corvallis Municipal Airport', 'Software Engineer II', 'Terrill', 75, 0, 0, 0, '2024-07-21', 'Ianno');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (76, 'Anshan Air Base', 'Physical Therapy Assistant', 'Coleen', 76, 0, 0, 0, '2024-09-09', 'Philpot');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (77, 'Longdongbao Airport', 'Software Engineer I', 'Filberto', 77, 0, 0, 0, '2024-07-01', 'Simunek');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (78, 'Apple Valley Airport', 'Editor', 'Joycelin', 78, 0, 0, 0, '2023-11-22', 'Clampin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (79, 'Arthur N Neu Airport', 'Financial Advisor', 'El', 79, 0, 0, 0, '2024-06-18', 'Foggo');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (80, 'Inukjuak Airport', 'Nurse Practicioner', 'Dylan', 80, 0, 0, 0, '2024-09-07', 'Buzza');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (81, 'Rochester International Airport', 'Registered Nurse', 'Lindsay', 81, 0, 0, 0, '2023-11-10', 'O''Kenny');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (82, 'Prado Airport', 'Electrical Engineer', 'Fiorenze', 82, 0, 0, 0, '2024-04-18', 'Benterman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (83, 'Craig Seaplane Base', 'Health Coach I', 'Michaella', 83, 0, 0, 0, '2023-12-06', 'Gibbons');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (84, 'Fayetteville Municipal Airport', 'Software Engineer III', 'Alfredo', 84, 0, 0, 0, '2024-05-11', 'Karczinski');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (85, 'Whiting Field Naval Air Station - North', 'Research Associate', 'Randie', 85, 0, 0, 0, '2024-10-13', 'Holdworth');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (86, 'Harry P Williams Memorial Airport', 'Human Resources Assistant III', 'Shane', 86, 0, 0, 0, '2024-07-07', 'Longbone');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (87, 'Geilenkirchen Air Base', 'Programmer Analyst I', 'Margarita', 87, 0, 0, 0, '2024-01-26', 'Bryce');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (88, 'Cornélio Procópio Airport', 'Programmer IV', 'Arlene', 88, 0, 0, 0, '2024-03-11', 'Ranns');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (89, 'Witu Airport', 'Paralegal', 'Shawn', 89, 0, 0, 0, '2024-10-30', 'Hamblington');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (90, 'Milyakburra Airport', 'Social Worker', 'Marion', 90, 0, 0, 0, '2024-02-22', 'Gillies');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (91, 'Monkey Bay Airport', 'Executive Secretary', 'Nedi', 91, 0, 0, 0, '2024-02-07', 'Tatterton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (92, 'Aeroclube de Bento Gonçalves Airport', 'Human Resources Manager', 'Lucila', 92, 0, 0, 0, '2024-10-20', 'Fust');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (93, 'Gregory Downs Airport', 'Marketing Assistant', 'Toddie', 93, 0, 0, 0, '2024-01-07', 'Dancer');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (94, 'Bunyu Airport', 'Pharmacist', 'Francisco', 94, 0, 0, 0, '2024-02-08', 'Bordis');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (95, 'Lake Macquarie Airport', 'Financial Advisor', 'Georgi', 95, 0, 0, 0, '2024-09-02', 'Sparhawk');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (96, 'Nain Airport', 'Senior Quality Engineer', 'Carolan', 96, 0, 0, 0, '2024-02-20', 'O''Cuddie');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (97, 'Touggourt Sidi Madhi Airport', 'Civil Engineer', 'Roma', 97, 0, 0, 0, '2024-07-18', 'Berrington');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (98, 'Lae Island Airport', 'Quality Control Specialist', 'Edin', 98, 0, 0, 0, '2024-06-21', 'Walewski');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (99, 'Chipinge Airport', 'Nurse', 'Hubie', 99, 0, 0, 0, '2023-11-08', 'Bristoe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (100, 'Tapini Airport', 'Product Engineer', 'Katine', 100, 0, 0, 0, '2024-01-13', 'Scrine');


SELECT * FROM board2;

COMMIT;

-- 8, 11, 12, 16, 21, 22, 25, 29, 35, 38, 44, 46, 57, 61, 66, 74, 88, 95, 96, 98
DELETE board2 WHERE bno = 98;

SELECT * FROM board2
WHERE bno BETWEEN 1 AND 20
;

-- rownum : 번호를 새롭게 부여
SELECT rownum, bno, btitle, bdate FROM board2
ORDER BY bdate DESC, btitle ASC
;

-- rownum 번호가 순서대로 정렬됨. 서브쿼리 사용
SELECT rnum, bno, btitle FROM (
    SELECT rownum rnum, bno, btitle FROM (
        SELECT bno, btitle FROM board2 ORDER BY bdate DESC
    )
)
WHERE rnum BETWEEN 11 AND 20
;

-- 모든 컬럼을 출력하시오.
-- 11 ~ 20
SELECT * FROM (
    SELECT rownum rnum, b.* FROM (
        SELECT * FROM board2
        ORDER BY bdate DESC
    ) b
)
WHERE rnum BETWEEN 11 AND 20
;

SELECT * FROM (
    SELECT ROW_NUMBER() OVER(ORDER BY bdate DESC) rnum, b.* FROM board2 b
)
WHERE rnum BETWEEN 11 AND 20
;


-- ROW_NUMBER() OVER() : 정렬한 후, 번호를 부여
SELECT rnum, btitle, bdate FROM (
    SELECT ROW_NUMBER() OVER(ORDER BY bdate DESC) rnum, bno, btitle, bdate
    FROM board2
)
WHERE rnum BETWEEN 11 AND 20
;

SELECT * FROM (
    SELECT ROW_NUMBER() OVER(ORDER BY bdate DESC) rnum, a.* FROM board2 a
)
WHERE rnum BETWEEN 11 AND 20
;

SELECT bgroup, bno, a.* FROM board2 a;

SELECT bno, btitle, bcontent, id, bgroup, bstep, bindent, bdate, bfile FROM board2;

-- rownum
SELECT * FROM (
    SELECT rownum rnum, a.* FROM (
        SELECT no, name, avg, RANK() OVER(ORDER BY avg DESC) ranks FROM students
    ) a
)
WHERE rnum BETWEEN 11 AND 20
;

-- ROW_NUMBER() OVER()
SELECT * FROM (
    SELECT no, name, avg, ROW_NUMBER() OVER(ORDER BY avg DESC) rnum FROM students
)
WHERE rnum BETWEEN 11 AND 20
;

-- RANK() 함수
SELECT rownum, no, name, avg, RANK() OVER(ORDER BY avg DESC) FROM students;

-- RANK() 값 rank컬럼에 모두 입력하시오.
UPDATE students SET rank = 1
WHERE no = 1
;

SELECT * FROM students;

UPDATE students a SET rank = (
    SELECT ranks FROM (
        SELECT no, RANK() OVER(ORDER BY avg DESC) ranks FROM students
    ) b
    WHERE a.no = b.no
)
;

SELECT * FROM students
ORDER BY rank
;

COMMIT;

-- view
-- 상담원 : 사원들 전화를 가지고 사원들에 마케팅을 하려고 함.
-- 100명에게 사원 테이블 오픈 제공해달라고 요청 : 마케팅
-- 직원가 100만원 90% 10만원 아이폰16
SELECT * FROM employees;

CREATE OR REPLACE VIEW employees_view
AS
SELECT employee_id, emp_name, email, phone_number, hire_date
FROM employees
;

-- employees_view
SELECT * FROM employees_view;

-- 사원번호, 사원명, 이메일, 폰번호, 입사일, 부서번호, 부서명 출력하시오.
SELECT employee_id, emp_name, email, phone_number, hire_date, a.department_id, department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id
;

CREATE OR REPLACE VIEW emp_view
AS
SELECT employee_id, emp_name, email, phone_number, hire_date, a.department_id, department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id
;

SELECT * FROM emp_view;

-- view 삭제
DROP VIEW emp_view;

-- view 컬럼 커멘트(주석 - 설명문) 추가
COMMENT ON COLUMN employees_view.employee_id IS '사원번호에 해당됩니다.';
-- 컬럼 커멘트 주석 확인
SELECT * FROM user_col_comments;
-- 테이블 커멘트 주석확인
SELECT * FROM user_tab_comments;
--

SELECT * FROM emp02;

DESC emp02;

DROP TABLE emp02;

CREATE TABLE emp02 (
    employee_id NUMBER(6),
    emp_name VARCHAR2(80),
    hire_date DATE,
    salary NUMBER(8,2),
    department_id NUMBER(6)
);

DESC emp02;

INSERT INTO emp02 (employee_id, emp_name, hire_date, salary, department_id)
SELECT employee_id, emp_name, hire_date, salary, department_id
FROM employees
;

SELECT * FROM emp02;

-- view 생성
-- WITH READ ONLY : SELECT만 가능, INSERT, UPDATE, DELETE 불가
CREATE OR REPLACE VIEW emp02_view
AS
SELECT employee_id, emp_name, hire_date
FROM emp02
WITH READ ONLY
;

DROP VIEW emp02_view;

-- view select
SELECT * FROM emp02_view ORDER BY employee_id;

-- 단순 view : 1개 테이블로 구성된 것.
-- insert, update, delete 가능
-- 복합 view : 2개 이상 테이블 조인, 함수 사용, group by 같은 경우는 INSERT, UPDATE, DELETE 불가

-- 100번 이름 홍길동 변경
UPDATE emp02_view SET emp_name = '홍길동'
WHERE employee_id = 100
;

INSERT INTO emp02_view VALUES (
    207, '유관순', SYSDATE
);

DELETE emp02 WHERE employee_id = 207;
COMMIT;

SELECT * FROM emp02;
SELECT * FROM emp02_view ORDER BY employee_id DESC;

DESC emp02;
ALTER TABLE emp02 MODIFY salary NUMBER(8,2) NOT NULL;

SELECT * FROM students;
-- no : seq
-- 입력데이터 : name, kor, eng, math
-- total : 오라클에서 입력
-- avg : 오라클에서 입력
-- rank : 오라클에서 입력
-- sdata : SYSDATE 오라클에서 입력

INSERT INTO students VALUES
(students_seq.NEXTVAL, name, kor, eng, math, kor + eng + math, (kor + eng + math) / 3, 0, SYSDATE)
;

-- avg 소수점 2자리까지만 출력하시오.
-- no, name, kor, eng, math, total, avg, rank, sdate
SELECT no, name, kor, eng, math, total, ROUND(avg, 2) avg, rank, TO_CHAR(sdate, 'yyyy') sdate FROM students;

SELECT * FROM students;
COMMIT;

UPDATE students SET
  eng = 50, total = 210, avg = 70
WHERE no = 105
;

ROLLBACK;
