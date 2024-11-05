DROP TABLE emp02;
DROP TABLE mem2;

SELECT * FROM mem;

CREATE TABLE emp02(
    empno NUMBER(4) NOT NULL,
    ename VARCHAR2(30) NOT NULL,
    job VARCHAR2(9),
    deptno NUMBER(2)
);

INSERT INTO emp02 VALUES (
    1, '홍길동', 'clerk', 2
);

INSERT INTO emp02 VALUES (
    2, '유관순', NULL, NULL
);

-- NULL
INSERT INTO emp02 VALUES (
    NULL, '유관순', NULL, NULL
);

DROP TABLE emp02;

CREATE TABLE emp02(
    empno NUMBER(4) UNIQUE,
    ename VARCHAR2(30) NOT NULL,
    job VARCHAR2(9),
    deptno NUMBER(2)
);

INSERT INTO emp02 VALUES (
    1, '홍길동', 'clerk', 2
);

INSERT INTO emp02 VALUES (
    2, '유관순', NULL, NULL
);

INSERT INTO emp02 VALUES (
    3, '이순신', NULL, NULL
);

INSERT INTO emp02 VALUES (
    NULL, '강감찬', NULL, NULL
);

-- UNIQUE 에러
INSERT INTO emp02 VALUES (
    2, '김구', NULL, NULL
);

SELECT * FROM emp02;

DELETE emp02 WHERE empno IS NULL;

-- 제약조건 변경 ALTER
ALTER TABLE emp02 MODIFY empno NOT NULL;
ALTER TABLE emp02 MODIFY empno;

-- NOT NULL, pk_emp02_empno 별칭
ALTER TABLE emp02 ADD CONSTRAINT pk_emp02_empno PRIMARY KEY (empno);

CREATE TABLE emp02(
    empno NUMBER(4) PRIMARY KEY,
    ename VARCHAR2(30) NOT NULL,
    job VARCHAR2(9),
    deptno NUMBER(2)
);

DROP TABLE mem;

CREATE TABLE mem (
    id VARCHAR2(30) PRIMARY KEY,
    pw VARCHAR2(30) NOT NULL,
    name VARCHAR2(1000) DEFAULT '무명',
    gender VARCHAR2(6) CHECK (gender IN ('Male', 'Female')) -- male, female, MALE, FEMALE 입력시 에러
);

INSERT INTO mem VALUES (
    'aaa', '1111', '홍길동', 'Male'
);

INSERT INTO mem VALUES (
    'bbb', '1111', '유관순', 'Female'
);

COMMIT;

CREATE TABLE board2 (
    bno NUMBER(4) PRIMARY KEY,
    btitle VARCHAR2(1000) NOT NULL,
    id VARCHAR2(30),
    CONSTRAINT fk_board2_id FOREIGN KEY (id) REFERENCES mem(id)
);

SELECT * FROM mem;

DELETE mem WHERE id = 'aaa';

-- 외래키로 등록 시 부모키에 해당 값이 없을 시 에러
INSERT INTO board2 VALUES(
    2, '제목2', 'bbb'
);

-- 외래키 삭제
ALTER TABLE board2 DROP CONSTRAINT fk_board2_id;

-- 부모키 삭제 시 외래키로 등록된 값들을 모두 삭제
ALTER TABLE board2 ADD CONSTRAINT fk_board2_id FOREIGN KEY (id) REFERENCES mem (id) ON DELETE CASCADE;

-- DEFAULT : ON DELETE RESTRICTED : 부모 키 삭제 시, 외래키에 등록된 값이 있으면, 삭제가 되지 않음.
-- ON DELETE SET NULL : 부모키 삭제 시 외래키로 등록된 값을 삭제는 하지 않고, 해당되는 값만 NULL 처리

-- 부모테이블의 aaa삭제 시 자식 테이블의 aaa글이 모두 삭제
DELETE mem WHERE id = 'aaa';
SELECT * FROM mem;
SELECT * FROM board2;

DROP TABLE board2;
DROP TABLE mem;

CREATE TABLE mem(
    id VARCHAR2(3) PRIMARY KEY,
    pw VARCHAR2(100) NOT NULL,
    name VARCHAR2(100),
    deptno NUMBER(4)
);

INSERT INTO mem VALUES (
    'aaa', '1111', '홍길동', 10
);

INSERT INTO mem VALUES (
    'ccc', '1111', '이순신', 30
);

COMMIT;

SELECT * FROM mem;

-- 10 '총무부', 20 '인사부', 30 '마케팅'
SELECT id, pw, name, deptno,
DECODE(deptno, 
    10, '총무부',
    20, '인사부',
    30, '마케팅'
) FROM mem;

SELECT * FROM employees;

SELECT job_id FROM employees;

-- clerk : 5%, rep : 10%, man : 15%

-- 1, clerk, rep, man 사람을 출력하시오.
SELECT SUBSTR(job_id, 4) j_id FROM employees
WHERE SUBSTR(job_id, 4) IN ('CLERK', 'REP', 'MAN')
;

SELECT SUBSTR(job_id, 4) j_id, salary,
DECODE(SUBSTR(job_id, 4),
'CLERK', salary * 1.05,
'REP', salary * 1.1,
'MAN', salary * 1.15
) AS sal
FROM employees
WHERE SUBSTR(job_id, 4) IN ('CLERK', 'REP', 'MAN')
;

SELECT job_id, emp_name FROM employees
WHERE job_id LIKE '%_CLERK' OR job_id LIKE '%_REP' OR job_id LIKE '%_MAN';

create table lavel_data (
	id VARCHAR2(50) primary key,
	lavel number(1) not null
);
insert into lavel_data (id, lavel) values ('Arlen', 4);
insert into lavel_data (id, lavel) values ('Catie', 4);
insert into lavel_data (id, lavel) values ('Adoree', 5);
insert into lavel_data (id, lavel) values ('Cher', 4);
insert into lavel_data (id, lavel) values ('Dorita', 5);
insert into lavel_data (id, lavel) values ('Zulema', 1);
insert into lavel_data (id, lavel) values ('Richy', 4);
insert into lavel_data (id, lavel) values ('James', 5);
insert into lavel_data (id, lavel) values ('Aeriel', 5);
insert into lavel_data (id, lavel) values ('Reinald', 3);
insert into lavel_data (id, lavel) values ('Bernardina', 1);
insert into lavel_data (id, lavel) values ('Tiertza', 2);
insert into lavel_data (id, lavel) values ('Carolyne', 5);
insert into lavel_data (id, lavel) values ('Jonis', 1);
insert into lavel_data (id, lavel) values ('Abigael', 5);
insert into lavel_data (id, lavel) values ('Pauli', 4);
insert into lavel_data (id, lavel) values ('Sheffie', 2);
insert into lavel_data (id, lavel) values ('Tully', 2);
insert into lavel_data (id, lavel) values ('Ricard', 5);
insert into lavel_data (id, lavel) values ('Jameson', 3);
insert into lavel_data (id, lavel) values ('Thorstein', 1);
insert into lavel_data (id, lavel) values ('Arlyne', 5);
insert into lavel_data (id, lavel) values ('Mela', 5);
insert into lavel_data (id, lavel) values ('Yetta', 3);
insert into lavel_data (id, lavel) values ('Corilla', 4);
insert into lavel_data (id, lavel) values ('Adoree', 1);
insert into lavel_data (id, lavel) values ('Sabine', 3);
insert into lavel_data (id, lavel) values ('Nelson', 3);
insert into lavel_data (id, lavel) values ('Isahella', 5);
insert into lavel_data (id, lavel) values ('Mandel', 5);
insert into lavel_data (id, lavel) values ('Sasha', 4);
insert into lavel_data (id, lavel) values ('Deanne', 1);
insert into lavel_data (id, lavel) values ('Thorny', 1);
insert into lavel_data (id, lavel) values ('Jacki', 3);
insert into lavel_data (id, lavel) values ('Sibby', 2);
insert into lavel_data (id, lavel) values ('Jack', 2);
insert into lavel_data (id, lavel) values ('Chandra', 2);
insert into lavel_data (id, lavel) values ('Cecilla', 5);
insert into lavel_data (id, lavel) values ('Saunder', 1);
insert into lavel_data (id, lavel) values ('Way', 4);
insert into lavel_data (id, lavel) values ('Velma', 3);
insert into lavel_data (id, lavel) values ('Keelia', 1);
insert into lavel_data (id, lavel) values ('Clay', 4);
insert into lavel_data (id, lavel) values ('Grace', 2);
insert into lavel_data (id, lavel) values ('Maura', 5);
insert into lavel_data (id, lavel) values ('Karolina', 4);
insert into lavel_data (id, lavel) values ('Mal', 5);
insert into lavel_data (id, lavel) values ('Annette', 4);
insert into lavel_data (id, lavel) values ('Issy', 2);
insert into lavel_data (id, lavel) values ('Reid', 2);
insert into lavel_data (id, lavel) values ('Dall', 4);
insert into lavel_data (id, lavel) values ('Sukey', 2);
insert into lavel_data (id, lavel) values ('Etty', 5);
insert into lavel_data (id, lavel) values ('Kendall', 5);
insert into lavel_data (id, lavel) values ('Gibby', 4);
insert into lavel_data (id, lavel) values ('Kylila', 2);
insert into lavel_data (id, lavel) values ('Orelia', 2);
insert into lavel_data (id, lavel) values ('Alexei', 4);
insert into lavel_data (id, lavel) values ('Iorgo', 1);
insert into lavel_data (id, lavel) values ('Clive', 1);
insert into lavel_data (id, lavel) values ('Roger', 1);
insert into lavel_data (id, lavel) values ('Halette', 3);
insert into lavel_data (id, lavel) values ('Clyve', 3);
insert into lavel_data (id, lavel) values ('Peadar', 1);
insert into lavel_data (id, lavel) values ('Mose', 4);
insert into lavel_data (id, lavel) values ('Raimundo', 3);
insert into lavel_data (id, lavel) values ('Glori', 1);
insert into lavel_data (id, lavel) values ('Merrel', 2);
insert into lavel_data (id, lavel) values ('Ulberto', 2);
insert into lavel_data (id, lavel) values ('Bren', 4);
insert into lavel_data (id, lavel) values ('Ker', 2);
insert into lavel_data (id, lavel) values ('Rosalinda', 1);
insert into lavel_data (id, lavel) values ('Delphinia', 5);
insert into lavel_data (id, lavel) values ('Johnette', 3);
insert into lavel_data (id, lavel) values ('Marilyn', 3);
insert into lavel_data (id, lavel) values ('Paddy', 2);
insert into lavel_data (id, lavel) values ('Antony', 3);
insert into lavel_data (id, lavel) values ('Kinna', 5);
insert into lavel_data (id, lavel) values ('Rogers', 5);
insert into lavel_data (id, lavel) values ('Zolly', 5);
insert into lavel_data (id, lavel) values ('Lance', 1);
insert into lavel_data (id, lavel) values ('Carroll', 2);
insert into lavel_data (id, lavel) values ('Geralda', 2);
insert into lavel_data (id, lavel) values ('Riobard', 2);
insert into lavel_data (id, lavel) values ('Sunshine', 4);
insert into lavel_data (id, lavel) values ('Betteanne', 2);
insert into lavel_data (id, lavel) values ('Andrea', 1);
insert into lavel_data (id, lavel) values ('Theresina', 3);
insert into lavel_data (id, lavel) values ('Koenraad', 4);
insert into lavel_data (id, lavel) values ('Eydie', 1);
insert into lavel_data (id, lavel) values ('Karolina', 2);
insert into lavel_data (id, lavel) values ('Sutton', 5);
insert into lavel_data (id, lavel) values ('Ikey', 5);
insert into lavel_data (id, lavel) values ('Ugo', 1);
insert into lavel_data (id, lavel) values ('Mallory', 4);
insert into lavel_data (id, lavel) values ('Mariska', 2);
insert into lavel_data (id, lavel) values ('Edmund', 3);
insert into lavel_data (id, lavel) values ('Twyla', 5);
insert into lavel_data (id, lavel) values ('Laney', 5);
insert into lavel_data (id, lavel) values ('Onida', 4);

COMMIT;

SELECT * FROM lavel_data;

-- 1: 100포인트, 2:1000포인트, 3:5000포인트, 4:10000포인트, 5:20000포인트
-- point

SELECT id, lavel,
DECODE(lavel,
1, 100,
2, 1000,
3, 5000,
4, 10000,
5, 20000) || ' point' AS point
FROM lavel_data;

-- 10 '총무부', 20 '인사부', 30 '마케팅'
SELECT id, pw, name, deptno,
DECODE(deptno, 
    10, '총무부',
    20, '인사부',
    30, '마케팅'
) FROM mem;

-- DECODE 는 일치하는 경우만 사용가능
-- CASE, DECODE 같은 기능이지만, 비교연산자를 사용할 수 있음.
SELECT id, pw, name, deptno,
CASE
WHEN deptno = 10 THEN '총무부'
WHEN deptno = 20 THEN '인사부'
WHEN deptno = 30 THEN '마케팅'
END AS deptName
FROM mem;


-- 1, 2, 3 : 5000포인트, 4, 5 : 20000포인트
SELECT id, lavel,
DECODE(lavel,
1, 100,
2, 1000,
3, 5000,
4, 10000,
5, 20000) || ' point' AS point
FROM lavel_data;

SELECT id, lavel,
CASE
WHEN 1 <= lavel AND lavel <= 3 THEN 5000
WHEN 4 <= lavel THEN 20000
END point
FROM lavel_data;

SELECT * FROM students;

-- avg : 90점 이상 A, 80점 이상 B, 70 C, 60 D, 50 F
-- result 컬럼을 출력하시오.
SELECT name, ROUND(avg, 2) avg,
CASE
WHEN avg >= 90 THEN 'A'
WHEN avg >= 80 THEN 'B'
WHEN avg >= 70 THEN 'C'
WHEN avg >= 60 THEN 'D'
WHEN avg < 60 THEN 'F'
END AS result
FROM students;

-- 테이블 전체 복사
CREATE TABLE stu AS SELECT * FROM students;

-- 컬럼 추가
SELECT * FROM stu;

ALTER TABLE stu ADD result VARCHAR2(2);

-- result 컬럼에 추가하시오.
SELECT
CASE
WHEN avg >= 90 THEN 'A'
WHEN avg >= 80 THEN 'B'
WHEN avg >= 70 THEN 'C'
WHEN avg >= 60 THEN 'D'
WHEN avg < 60 THEN 'F'
END AS re
FROM stu;

UPDATE stu SET result = (
CASE
WHEN avg >= 90 THEN 'A'
WHEN avg >= 80 THEN 'B'
WHEN avg >= 70 THEN 'C'
WHEN avg >= 60 THEN 'D'
WHEN avg < 60 THEN 'F'
END
);

-- 파이썬에서 if문 구현해서 처리

-- RANK() OVER() : 순위를 구현하는 함수
SELECT no, name, total, RANK() OVER(ORDER BY total DESC) FROM stu
ORDER BY no;

-- RANK() OVER() : 중복 순위 개수만큼 다음 순 값을 증가해서 표시
-- DENSE_RANK() OVER() : 중복 순위가 존재해도 순차적으로 다음 순위 표시
SELECT no, name, total, DENSE_RANK() OVER(ORDER BY total DESC) AS ra FROM stu;

-- 순위를 rank컬럼에 추가하시오.
UPDATE stu a SET rank = (
    SELECT ra FROM (
    SELECT no, RANK() OVER(ORDER BY total DESC) AS ra FROM stu
    ) b
    WHERE a.no = b.no
);

SELECT no, rank FROM stu;
SELECT no, RANK() OVER(ORDER BY total DESC) AS ranks FROM stu;

-- RANK 등수 입력처리
UPDATE stu a SET rank = (
    SELECT ra FROM (
    SELECT no, RANK() OVER(ORDER BY total DESC) AS ra FROM stu
    ) b
    WHERE a.no = b.no
);

-- CASE
-- salary 5000 이하는 월급 15% 인상, 5000 ~ 8000 : 10% 인상, 8000 이상 : 5% 인상을 해서 출력하시오.
SELECT emp_name, salary,
CASE
WHEN salary >= 8000 THEN salary * 1.05
WHEN salary >= 5000 THEN salary * 1.1
WHEN salary < 5000 THEN salary * 1.15
END AS y_salary
FROM employees;

-- emp_name 대문자 D가 포함되어 있으면 10% 인상, M이 포함되어 있으면 5%, 그 외 0%
SELECT emp_name, salary,
CASE
WHEN emp_name LIKE '%D%' THEN salary * 1.1
WHEN emp_name LIKE '%M%' THEN salary * 1.05
ELSE salary
END y_salary
FROM employees;

SELECT * FROM employees;
SELECT department_id, commission_pct FROM employees
WHERE commission_pct IS NOT NULL
;

-- 커미션이 있는 사원 수를 출력하시오.
SELECT COUNT(*) FROM employees
WHERE commission_pct IS NOT NULL
;

-- 부서별 사원 수를 출력하시오.
SELECT department_id, COUNT(*) FROM employees
GROUP BY department_id;

-- 부서별 평균 월급을 출력하시오.
SELECT department_id, AVG(salary) FROM employees
GROUP BY department_id;

-- 그룹 함수 조건을 사용하려면, HAVING 절을 사용함.
-- 부서별 평균 월급이 7000보다 높은 사람의 인원 수를 출력하시오.
SELECT department_id, AVG(salary), COUNT(*) FROM employees
GROUP BY department_id
HAVING AVG(salary) >= 7000
;

-- 전체 평균 월급보다 적게 받는 사원 수를 출력하시오.
SELECT COUNT(*) FROM employees
WHERE salary < (SELECT AVG(salary) FROM employees)
;

SELECT department_id, COUNT(*) FROM employees
WHERE salary < (SELECT AVG(salary) FROM employees)
GROUP BY department_id
;

SELECT department_id, COUNT(*) FROM employees e
WHERE salary < (
    SELECT a FROM (
        SELECT department_id, AVG(salary) a FROM employees GROUP BY department_id) e2
    WHERE e.department_id = e2.department_id)
GROUP BY department_id
ORDER BY department_id
;

-- 부서별 평균 월급이 6000이하인 부서별 인원 수를 출력하시오.
-- 그룹 함수는 HAVING절에 조건문을 사용해야 함. WHERE절에는 사용불가
SELECT department_id, COUNT(*) FROM employees
GROUP BY department_id
HAVING AVG(salary) > 6000;

-- 부서번호, 부서별 평균 월급
SELECT department_id, AVG(salary) FROM employees
GROUP BY department_id
;

-- 부서번호, 개인별 월급, 인원
SELECT department_id, salary, COUNT(*) FROM employees
GROUP BY department_id, salary
;

SELECT salarys FROM (
    SELECT department_id, AVG(salary) salarys FROM employees
    GROUP BY department_id
);

SELECT department_id, AVG(salary) salarys FROM employees
GROUP BY department_id

-- 부서별 평균 월급보다 적게 받는 사원을 출력하시오.
SELECT department_id, emp_name, salary FROM employees a
WHERE salary < (
    SELECT salarys FROM (
        SELECT department_id, AVG(salary) salarys FROM employees
        GROUP BY department_id
    ) b
    WHERE a.department_id = b.department_id
)
;

-- 부서별 평균 월급보다 적게 받는 사원 수
SELECT department_id, COUNT(*) FROM employees a
WHERE salary < (
    SELECT salarys FROM (
        SELECT department_id, AVG(salary) salarys FROM employees
        GROUP BY department_id
    ) b
    WHERE a.department_id = b.department_id
)
GROUP BY department_id
ORDER BY department_id
;

SELECT department_id, emp_name, salary FROM employees
WHERE department_id = 30;

SELECT AVG(salary) FROM employees
WHERE department_id = 30; -- 4150

-- 부서의 최대 급여와 최소 급여를 출력하되, 최대 급여가 5000이상인 부서만 출력하시오.
SELECT department_id, MAX(salary), MIN(salary) FROM employees
GROUP BY department_id
HAVING MAX(salary) > 5000
ORDER BY department_id DESC
;

-- 학번, 이름, 전화번호, 주소, 성별, 학년, 학기, 국어, 영어, 수학, 합계, 평균, 등수
-- 1001, 홍길동, 010, 서울, 남자, 1, 1, 100, 100, 100, 300, 1
-- 1001, 홍길동, 010, 서울, 남자, 1, 2, 90, 90, 90, 270, 8
-- 1001, 홍길동, 010, 서울, 남자, 1, 3, 95, 95, 95, 285, 15
-- 1001, 홍길동, 010, 서울, 남자, 1, 4, 100, 100, 99, 299, 2
-- 1001, 홍길동, 010, 서울, 남자, 2, 1, 100, 100, 100, 300, 1
-- 1001, 홍길동, 010, 서울, 남자, 2, 2, 90, 90, 90, 270, 8
-- 1001, 홍길동, 010, 서울, 남자, 2, 3, 95, 95, 95, 285, 15
-- 1001, 홍길동, 010, 서울, 남자, 2, 4, 100, 100, 99, 299, 2
-- 1001, 홍길동, 010, 서울, 남자, 3, 1, 100, 100, 100, 300, 1
-- 1001, 홍길동, 010, 서울, 남자, 3, 2, 90, 90, 90, 270, 8
-- 1001, 홍길동, 010, 서울, 남자, 3, 3, 95, 95, 95, 285, 15
-- 1001, 홍길동, 010, 서울, 남자, 3, 4, 100, 100, 99, 299, 2

-- 부서명 departments
SELECT * FROM departments;

SELECT * FROM employees;

-- Donald OConnell 의 부서명을 알고 싶어요.
SELECT emp_name, department_id FROM employees
WHERE emp_name = 'Donald OConnell';

SELECT department_id, department_name FROM departments
WHERE department_id = 50;

-- JOIN을 사용해샤 두개의 쿼리를 1개의 쿼리로 구성이 가능해짐.
-- JOIN
-- 1. CROSS JOIN
-- 1-1 INNER JOIN (equi join, non-equi join)

-- 2. INNER JOIN
-- 3. OUTER JOIN
-- 4. SELF JOIN

-- CROSS JOIN : 특별한 키워드 없이 두 개의 테이블을 검색하는 것
SELECT * FROM employees; -- 107
SELECT * FROM departments; -- 27

SELECT COUNT(*) FROM employees, departments; -- 2889 (107 * 27)
SELECT * FROM employees, departments;

-- INNER JOIN : EQUI JOIN - 같은 컬럼을 가지고 비교해서 두개의 테이블을 검색
SELECT emp_name, a.department_id, department_name FROM employees a, departments b
WHERE a.department_id = b.department_id
;

SELECT bno, btitle, bcontent, id FROM board;
SELECT * FROM member;
SELECT * FROM board;

-- 101 * 4 = 404

SELECT * FROM board;

SELECT bno, btitle, bcontent, a.id, email, phone, bgroup, bstep, bindent, bhit, bdate, bfile
FROM member a, board b
WHERE a.id = b.id
;

SELECT * FROM jobs;
SELECT * FROM employees;

-- inner join : 사원번호, 사원명, job_id, job_title을 출력하시오.
SELECT employee_id, emp_name, a.job_id, job_title
FROM employees a, jobs b
WHERE a.job_id = b.job_id AND a.job_id = 'SH_CLERK'
;

-- 사원번호, 사원명, 부서번호, 부서명, job_id, job_title을 출력하시오.
SELECT employee_id, emp_name, a.department_id, department_name, a.job_id, job_title
FROM employees a, departments b, jobs c
WHERE a.department_id = b.department_id AND a.job_id = c.job_id
;

-- 
SELECT bno, btitle, bcontent, a.name, bgroup, bstep, bindent, bhit, bdate, bfile
FROM member a, board b
WHERE a.id = b.id
;

-- 사원번호, 사원명, 월급, 부서번호, 부서명
-- 월급 평균 월급보다 적은 사원을 출력하시오.
SELECT employee_id, emp_name, salary, a.department_id, department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id AND salary < (
    SELECT AVG(salary) FROM employees
)
;

-- 부서별 평균월급보다 작은 사원을 출력하시오.
SELECT employee_id, emp_name, salary, a.department_id, department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id AND salary < (
    SELECT y_salary FROM (
    SELECT department_id, AVG(salary) y_salary FROM employees
    GROUP BY department_id
    ) c
    WHERE a.department_id = c.department_id
)
;

SELECT department_id, AVG(salary) FROM employees
GROUP BY department_id;

-- job_id가 CLERK 인 사원의 사원명, 사원번호, 부서명, 부서번호, 직급번호, 직급명 출력하시오.
SELECT emp_name, employee_id, department_name, a.department_id, a.job_id, job_title
FROM employees a, departments b, jobs c
WHERE a.department_id = b.department_id AND a.job_id = c.job_id
AND SUBSTR(a.job_id, 4) IN ('CLERK', 'MAN')
;


SELECT salary FROM employees
ORDER BY salary
;

-- 2000 - 4000 E등급, 4000 - 6000 D등급, 6000 - 8000 C등급, 8000 - 10000 B등급, 10000 - 100000 A등급
CREATE TABLE salgrade (
    grade VARCHAR2(10),
    losal NUMBER(6),
    hisal NUMBER(6)
);

INSERT INTO salgrade VALUES (
    'E등급', 2000, 4000
);

INSERT INTO salgrade VALUES (
    'D등급', 4001, 6000
);

INSERT INTO salgrade VALUES (
    'C등급', 6001, 8000
);

INSERT INTO salgrade VALUES (
    'B등급', 8001, 10000
);

INSERT INTO salgrade VALUES (
    'A등급', 10001, 100000
);

SELECT * FROM salgrade;

-- salary, 등급을 넣을려고 함 
-- salgrade, employees 같은 컬럼이 없음
-- non-equi join을 사용해서 테이블을 join하려고 함
SELECT salary FROM employees;

SELECT emp_name, salary, grade
FROM employees, salgrade; -- 107 * 5 = 535

-- non-equi join : 두 테이블간 같은 컬럼이 없으면서, 두 테이블의 값을 비교해서 출력
SELECT emp_name, salary, grade
FROM employees, salgrade
WHERE salary BETWEEN losal AND hisal
;

-- non-equi join 활용해서 students total A, B, C, D, F 등급을 출력하시오.
-- 100 - 90 A, 89 - 80 B, 79 - 70 C, 69 - 60 D, 60점 미만 F
-- 테이블명 : stu_grade grade, lototal, hitotal

CREATE TABLE stu_grade (
    grade VARCHAR2(10),
    loavg NUMBER(6),
    hiavg NUMBER(6)
);

DROP TABLE stu_grade;

INSERT INTO stu_grade VALUES (
    'A등급', 90, 100
);

INSERT INTO stu_grade VALUES (
    'B등급', 80, 89
);

INSERT INTO stu_grade VALUES (
    'C등급', 70, 79
);

INSERT INTO stu_grade VALUES (
    'D등급', 60, 69
);

INSERT INTO stu_grade VALUES (
    'F등급', 0, 59
);

COMMIT;

SELECT * FROM stu_grade;
SELECT * FROM students;

SELECT name, total, avg, grade FROM students, stu_grade
WHERE avg BETWEEN loavg AND hiavg
;

SELECT * FROM stu;

UPDATE stu SET result = '';
COMMIT;

-- result 결과값을 non-equi join을 사용해서 입력하시오.
SELECT no, grade FROM stu, stu_grade
WHERE avg BETWEEN loavg AND hiavg;

ALTER TABLE stu MODIFY result VARCHAR2(10);

UPDATE stu a SET result = (
    SELECT grade FROM
        (SELECT no, grade FROM stu, stu_grade
        WHERE FLOOR(avg) BETWEEN loavg AND hiavg) b
    WHERE a.no = b.no
);

SELECT * FROM stu;

-- self join
SELECT employee_id, emp_name, manager_id FROM employees
WHERE employee_id = 124
;

-- self join :자신의 테이블 2개를 join 결과값을 출력
SELECT a.employee_id, a.emp_name, a.manager_id, b.emp_name manager_name
FROM employees a, employees b
WHERE a.manager_id = b.employee_id AND a.manager_id = 124
;

