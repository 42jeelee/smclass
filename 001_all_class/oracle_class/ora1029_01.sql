--DROP TABLE member;
--DROP TABLE date_tab;
--DROP TABLE students;

-- create 테이블 생성, alter 테이블 수정, drop 테이블 삭제
CREATE TABLE member(
    no NUMBER(4),
    id VARCHAR2(20),
    pw VARCHAR2(20),
    name VARCHAR2(20),
    phone VARCHAR2(20),
    mdate DATE
);

-- insert 데이터 입력
INSERT INTO member VALUES(
    1,'aaa','1111','홍길동','010-1111-1111','2024-10-29'
);

INSERT INTO member VALUES(
    2,'bbb','1111','유관순','010-2222-2222','2024-10-20'
);

-- insert 데이터 입력, select 데이터 검색, update 데이터 수정, delete 데이터 삭제
SELECT * FROM member;

-- delete 테이블 삭제
DELETE member where no=2;


-- update 테이블 수정
UPDATE member SET name='홍길자' WHERE no=1;
UPDATE member SET name='김구';

SELECT * FROM member;

-- create 테이블 생성
CREATE TABLE students (
    stuno NUMBER(4),
    name VARCHAR2(20),
    kor NUMBER(3),
    eng NUMBER(3),
    total NUMBER(3),
    sdate DATE
);

INSERT INTO students VALUES(
    1, '홍길동', 100, 100, 100 + 100, SYSDATE
);

COMMIT;
ROLLBACK;

-- 모든 컴럼 검색
SELECT * FROM students;

-- 특정 컬럼을 입력하면 컬럼만 검색
SELECT name,sdate FROM strudents;

-- 특정 컬럼만 입력하면 컬럼입력
INSERT INTO students (stuno,name) VALUES (
    2,'유관순'
);

SELECT * FROM students;

--
SELECT * FROM employees;

-- 테이블을 생성하면서 테이블 내용을 모두 복사
CREATE TABLE emp2 AS SELECT * FROM employees;
SELECT * FROM emp2;
SELECT COUNT(*) FROM emp2; -- 데이터 개수

-- 테이블을 생성하면서 테이블 구조만 복사
CREATE TABLE emp3 AS SELECT * FROM employees WHERE 1=2;
SELECT * FROM emp3;

-- 테이블이 존재할 경우 데이터만 복사
CREATE TABLE member2 AS SELECT * FROM member WHERE 1=2;
INSERT INTO member2 SELECT * FROM member;

-- 테이블 컬럼
-- 컬럼 데이터 타입, 길이 변경
-- ALTER 변경 member 테이블 no 컬럼의 타입길이를 변경
ALTER TABLE member MODIFY no NUMBER(10);
-- ALTER 변경, 컬럼의 이름을 변경
ALTER TABLE member RENAME COLUMN NO TO memberNo;

UPDATE member SET no='';
SELECT * FROM member;
ALTER TABLE member MODIFY no VARCHAR2(10);

DESC member;

SELECT * FROM member;

SELECT * FROM member;
select * from member;


SELECT * FROM member2;
COMMIT;

-- 테이블 구조
DESC employees;

-- employees 테이블에서 사원번호 (employee_id), 사원이름(emp_name), 입사일(hire_date)을 출력하시오.
SELECT employee_id, emp_name, hire_date
FROM employees;

SELECT * FROM employees;

-- 연산자 : 산술연산자 +,-,*,/

--DROP TABLE member;
--DROP TABLE member2;
--DROP TABLE emp2;

create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);
SELECT * FROM member;

DROP TABLE students;
create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);

SELECT * FROM students;

COMMIT;

SELECT kor, eng, (kor+eng) FROM students;
SELECT kor, eng, (kor-eng), ABS(kor-eng) FROM students;

SELECT * FROM employees;

-- 문자 더하기 안됨.
SELECT employee_id + emp_name FROM employees;

-- concat 명령어, ||
SELECT CONCAT(employee_id, emp_name) FROM employees;
SELECT employee_id || emp_name FROM employees;

-- 달러 환산 1384
SELECT salary FROM employees;
SELECT salary * 1384 FROM employees;
-- 문자로 변환, 천 단위 표시
SELECT TO_CHAR(salary * 1384, '999,999,999') FROM employees;
SELECT emp_name, salary, salary * 1384 FROM employees;

CREATE TABLE stu(
    no NUMBER(4),
    name VARCHAR2(20),
    kor NUMBER(3)
);

INSERT INTO stu VALUES(1,'홍길동',100);
INSERT INTO stu VALUES(2,'유관순',99);

COMMIT;

INSERT INTO stu VALUES(3,'',0);
INSERT INTO stu VALUES(4,null,null);

SELECT * FROM stu;

-- null 값 검색 IS NULL
SELECT * FROM stu WHERE name IS NULL;

SELECT * FROM employees;
-- NULL 이 아닌 것 출력 : IS NOT NULL
SELECT commission_pct FROM employees WHERE commission_pct IS NOT NULL;

SELECT salary FROM employees;

-- 연봉 계산 * 12
SELECT salary, salary * 12 FROM employees;
SELECT salary, salary * 12, salary * 12 * 1384 FROM employees;

-- 커미션이 없는 사원은 null값이 있는데, null +,-,*,/ null 값으로 변경
SELECT salary, salary * 12, salary * 12 + (salary * 12) * commission_pct * 0.01 FROM employees;
SELECT salary, salary * 12 AS "연 봉", salary * 12 + (salary * 12) * NVL(commission_pct, 0) * 0.01 AS real_yearSalary FROM employees;

-- NVL() 함수, NVL(kor, 0) : kor 컬럼에 null값이 있으면 0으로 표시
SELECT * FROM stu;
SELECT no, name, kor, kor + 100 FROM stu;
SELECT no, name, kor, NVL(kor, 0) + 100 FROM stu;

-- 이름, 국어, 영어, 수학, 합계, 평균, 등수, 입력일
-- 컬럼명 별칭을 사용해서 출력하시오.
SELECT * FROM students;
SELECT name AS "이름", kor 국어, eng "영   어", math "수학", total "합계", avg "평균", rank "등수", sdate "입력일" FROM students;

SELECT * FROM students;

-- 사원번호, 이름, 이메일을 합쳐서 출력하시오.
SELECT * FROM employees;
SELECT employee_id, emp_name, email FROM employees;
SELECT employee_id || emp_name || email FROM employees;
SELECT CONCAT(CONCAT(employee_id, emp_name), email) FROM employees;
SELECT emp_name || ' is a ' || job_id FROM employees;

-- 중복제거
SELECT department_id FROM employees;
SELECT DISTINCT department_id FROM employees;

-- 정렬 : ORDER BY - 순차정렬, desc - 역순정렬
SELECT DISTINCT department_id FROM employees ORDER BY department_id desc;


-- job_id 중복제거 출력하시오.
SELECT DISTINCT job_id FROM employees;
SELECT job_id FROM employees;

-- 문자열 자르기 substr(0, 2) 0, 1 : 2앞 까지만 출력
SELECT SUBSTR(job_id, 0, 2) FROM employees;
-- 4번째 컬럼 데이터를 가져와서 중복을 제거함
SELECT DISTINCT SUBSTR(job_id, 4) FROM employees;

-- WHERE절 : 조건 비교 연산자
SELECT * FROM employees WHERE manager_id = 124;
SELECT * FROM employees WHERE job_id = 'SH_CLERK';
SELECT * FROM employees WHERE employee_id > 100;

-- students 합계 250 이상 출력하시오.
SELECT * FROM students WHERE total >= 250;

-- 합계 250, kor 90점 이상 출력하시오.
SELECT * FROM students WHERE total >= 250 AND kor >= 90;

-- 영어점수 70 이상, 90 이하 출력하시오.
SELECT * FROM students WHERE 70 <= eng AND eng <= 90;

-- 월급이 5000 이상 8000 이하 출력하시오.
SELECT * FROM employees WHERE 5000 <= salary AND salary <= 8000;

-- 7000이 아닌 것을 출력하시오. !=, <>, ^=
SELECT * FROM employees WHERE salary != 7000;

-- 부서(department_id) = 50,
-- COUNT 개수 확인
SELECT * FROM employees WHERE department_id = 50;
SELECT COUNT(*) FROM employees WHERE department_id = 50;
-- 50번이 아닌 것 출력하시오.
SELECT * FROM employees WHERE department_id <> 50;
SELECT COUNT(*) FROM employees WHERE department_id <> 50;

-- null값은 COUNT() 포함되지 않음
SELECT COUNT(*) FROM employees WHERE department_id IS NULL;

SELECT COUNT(employee_id) FROM employees;   -- 107개
SELECT COUNT(department_id) FROM employees; -- 106개

-- 급여 4000 이하 사원번호, 사원명, 급여 컬럼만 출력하시오.
SELECT employee_id 사원번호, emp_name 사원명, salary 급여 FROM employees WHERE salary <= 4000;

-- 숫자인 경우 비교연산자 가능, 날짜 비교연산자가 가능
SELECT emp_name, hire_date FROM employees;

SELECT emp_name, hire_date FROM employees WHERE hire_date >= '2002/01/01';

-- 1999/12/31 이전에 입사한 사람을 출력하시오.
SELECT emp_name, hire_date FROM employees WHERE hire_date <= '1999/12/31';

-- 2001/01/01 부터 2004/12/31 까지 출력하시오.
SELECT emp_name, hire_date FROM employees WHERE '2001/01/01' <= hire_date AND hire_date <= '20041231';

-- 논리연산자
-- 국어점수가 90점 이상 또는 영어점수가 90점 이상을 출력하시오. students 테이블
SELECT COUNT(*) FROM students WHERE kor >= 90 OR eng >= 90;
SELECT COUNT(*) FROM students WHERE kor >= 90 AND eng >= 90;
SELECT COUNT(*) FROM students WHERE NOT kor >= 90;

-- 부서번호(department_id) 80이면서 job_id - MAN
SELECT * FROM employees WHERE department_id = 80 AND SUBSTR(job_id, 4) = 'MAN';
SELECT * FROM employees WHERE department_id = 80 AND job_id = 'SA_MAN';

-- 커미션이 0.2, 0.3, 0.5 인 경우만 출력
SELECT commission_pct FROM employees WHERE commission_pct IS NOT NULL;
SELECT commission_pct FROM employees WHERE commission_pct = 0.2 OR commission_pct = 0.3 OR commission_pct = 0.5;

SELECT commission_pct FROM employees
WHERE
commission_pct IN (0.2, 0.3, 0.5);

-- 사원 번호(employee_id) 110,120,130 출력하시오.
SELECT employee_id, emp_name FROM employees WHERE employee_id = 110 OR employee_id = 120 OR employee_id = 130;
SELECT employee_id, emp_name FROM employees WHERE employee_id IN (110,120,130);

-- 150-170 사원번호를 출력하시오.
SELECT * FROM employees WHERE employee_id >= 150 AND employee_id <= 170;

-- between - and : <= 포함이 되어 있는 경우만 해당
SELECT * FROM employees
WHERE employee_id BETWEEN 150 AND 170;

-- 날짜 IN
SELECT hire_date FROM employees;
SELECT hire_date FROM employees
WHERE hire_date IN ('2004/02/17','2002/06/07');

-- 날짜 BETWEEN
SELECT hire_date FROM employees
WHERE hire_date BETWEEN '2002/06/17' AND '2004/12/31';

-- job MAN 출력하시오.
SELECT * FROM employees WHERE SUBSTR(job_id, 4) = 'MAN';

-- LIKE 연산자 : 포함되어 있는 글자 검색
SELECT * FROM employees
WHERE job_id = 'MAN';
-- MAN으로 끝나는 단어를 검색
SELECT * FROM employees
WHERE job_id LIKE '%MAN';
-- ST로 시작하는 단어를 검색
SELECT * FROM employees
WHERE job_id LIKE 'ST%';

-- emp_name a가 들어가 있는 이름 출력하시오.
SELECT emp_name FROM employees WHERE emp_name LIKE '%a%';

-- 2번째 자리에 T가 들어가 있는 이름 출력하시오.
SELECT * FROM employees WHERE emp_name LIKE '_t%';

-- 4번째 v가 들어가 있는 이름 출력하시오.
SELECT * FROM employees WHERE emp_name LIKE '___v%';

-- 뒤에서 2번째 자리에 l에 가 있는 이름을 출력하시오.
SELECT * FROM employees WHERE emp_name LIKE '%l_';

-- 첫번째 D가 들어가 잇는 이름을 출력하시오.
SELECT * FROM employees WHERE emp_name LIKE 'D%';

