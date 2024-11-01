-- 입사일의 마지막 날짜를 출력하시오.
-- 10/1 -> 10/31, 9/5 -> 9/30
-- last_day
SELECT hire_date, LAST_DAY(hire_date) FROM employees;

-- 가입일
SELECT sdate FROM students;

-- 가입일, 1년 후 날짜를 출력하시오.
SELECT sdate, ADD_MONTHS(sdate, 12) FROM students;

-- 가입일이 6개월 이내의 회원만 출력하시오.
SELECT sdate, ADD_MONTHS(sdate, -6) FROM students;

-- 현재일 기준으로 입력일이 6개월 이내의 회원만 출력하시오.
-- 11/1
SELECT sdate FROM students
WHERE sdate >= ADD_MONTHS(SYSDATE, -6)
ORDER BY sdate
;

-- 월별로 가입 인원을 출력하시오.
SELECT mdate, LAST_DAY(mdate) FROM member;

SELECT LAST_DAY(mdate) md FROM member
ORDER BY md
;

SELECT SUBSTR(LAST_DAY(mdate), 1, 5) md, COUNT(*) FROM member
GROUP BY LAST_DAY(mdate)
;

-- employees 테이블에서 부서별(department_id) 인원을 출력하시오.
SELECT department_id, COUNT(*)
FROM employees
GROUP BY department_id
;

-- 그룹함수 : SUM, AVG, COUNT, MIN, MAX, MEDIAN

CREATE TABLE emp3
AS SELECT * FROM employees;

SELECT * FROM emp3;

CREATE TABLE emp4
AS SELECT * FROM employees WHERE 1=2;

SELECT * FROM emp4;

-- 테이블 구조가 있는 상태에서 모든 데이터를 입력하는 방법
INSERT INTO emp4 SELECT * FROM employees;
ROLLBACK;

INSERT INTO emp4 (employee_id, emp_name, hire_date)
SELECT employee_id, emp_name, hire_date FROM employees;

-- INSERT, UPDATE, DELETE
-- COMMIT, ROLLBACK

-- 테이블
-- CREATE : 생성, ALTER : 변경, DROP : 삭제

--

SELECT * FROM emp4;

-- ALTER ADD : 테이블 컬럼 추가
ALTER TABLE emp4
ADD(hire_date2 DATE);

DESC emp4;

-- 컬럼 변경 : 컬럼 안에 데이터가 있다면 제약조건, 65 길이의 문자가 있을 경우, 50으로 변경 안됨.
ALTER TABLE emp4
MODIFY (email VARCHAR2(70));

ALTER TABLE emp4
MODIFY (email VARCHAR2(50));

SELECT emp_name FROM emp4;

DESC emp4;

ALTER TABLE emp4
MODIFY (emp_name VARCHAR2(20));

-- 컬럼의 길이 확인
SELECT MAX(LENGTH(emp_name)) FROM employees;
SELECT LENGTH(emp_name) em FROM employees
ORDER BY em DESC;

-- 컬럼 타입 변경 -> 컬럼안 데이터가 null 이면 가능
-- 다른 타입인 경우 데이터를 null로 변경한 후 타입을 변경해야 함.
SELECT * FROM emp4;
ALTER TABLE emp4
MODIFY (email NUMBER(4));

ALTER TABLE emp4
MODIFY (emp_name NUMBER(20));

DESC emp4;

-- employee_id 값을 email 컬럼에 복사
UPDATE emp4 SET email = employee_id;

-- employee_id 값을 phone_number 입력하시오.
-- phone_number 문자형타입, employee_id 숫자형 타입
UPDATE emp4 SET phone_number = employee_id;

COMMIT;
ROLLBACK;

SELECT * FROM emp4;
UPDATE emp4 SET phone_number = '198a' WHERE employee_id = 198;

-- 문자형 타입을 숫자형 타입에 복사
-- 안에 있는 데이터가 모두 숫자형이기에 가능
-- 문자가 포함되어 있으면 안됨.
UPDATE emp4 SET manager_id = phone_number;

-- 컬럼 이름 변경
SELECT * FROM emp4;
ALTER TABLE emp4 RENAME COLUMN phone_number To p_number;

-- 속성 변경가능
ALTER TABLE emp4 MODIFY hire_date DATE NULL;
ALTER TABLE emp4 MODIFY hire_date DATE NOT NULL;

-- 컬럼 삭제
ALTER TABLE emp4
DROP COLUMN hire_date2;

DESC emp4;

-- 테이블 삭제
DROP TABLE emp2;
DROP TABLE emp3;

-- 테이블 이름 변경
RENAME emp4 TO emp44;

----
SELECT * FROM departments;

-- PRIMARY KEY : 중복 불가, null 값 불가
-- UNIQUE : 중복 불가, null 값 허용
-- NOT NULL : 중복 가능, null 값 불가
-- DEFAULT : 값이 입력되지 않았을 때 디폴트값 지정

SELECT gender FROM member;

DROP TABLE board;
CREATE TABLE bmember (
    id VARCHAR2(30) PRIMARY KEY,
    pw VARCHAR2(30) NOT NULL,
    name VARCHAR2(30) NOT NULL,
    age NUMBER(3) DEFAULT 0,
    gender VARCHAR2(6) CHECK(gender IN ('Male', 'Female')),
    nicname VARCHAR2(30),
    email VARCHAR2(20),
    bdate DATE DEFAULT SYSDATE
);

DROP TABLE bmember;

-- 입력
INSERT INTO bmember (id, pw, name, nicname, age, gender, email, bdate) VALUES (
    'aaa', '1111', '홍길동', '길동스', 20, 'Male', 'aaa@aaa.com', SYSDATE
);

INSERT INTO bmember (id, pw, name, nicname, gender, email) VALUES (
    'bbb', '2222', '유관순', '관순스', 'Female', 'bbb@bbb.com'
);

-- CHECK - Male, Female 2가지 형태외에는 입력이 안됨.
-- male, MALE, malE 데이터 입력 불가
INSERT INTO bmember (id, pw, name, nicname, age, gender, email, bdate) VALUES (
    'ccc', '1111', '이순신', '순신스', 20, 'Male', 'ccc@ccc.com', SYSDATE
);

-- NOT NULL : null 허용하지 않음, 빈공백은 가능함
INSERT INTO bmember (id, pw, name, nicname, age, gender, email, bdate) VALUES (
    'ddd', ' ', '강감찬', '감찬스', 20, 'Male', 'ddd@ddd.com', '2024/01/01'
);

-- PRIMARY KEY : 중복 불가, null 불가
INSERT INTO bmember (id, pw, name, nicname, age, gender, email, bdate) VALUES (
    'eee', '1111', '김구', '구스', 20, 'Male', 'eee@eee.com', '2024/02/21'
);

COMMIT;
SELECT * FROM bmember;

CREATE TABLE emp3 (
    empno NUMBER(4) UNIQUE,
    ename VARCHAR2(30) NOT NULL,
    job VARCHAR2(9),
    deptno NUMBER(2)
);

INSERT INTO emp3 VALUES (
    1, '홍', '01', '01'
);

INSERT INTO emp3 VALUES (
    2, '유', '02', '02'
);

-- unique null값은 허용
INSERT INTO emp3 (ename, job, deptno) VALUES (
    '이', '03', '03'
);

-- unique 중복은 불가
INSERT INTO emp3 VALUES (
    2, '강', '04', '04'
);

SELECT * FROM emp3;

-- PRIMARY KEY 추가, 수정
-- CONSTRAINT id_pk : 이름 설정
ALTER TABLE member ADD CONSTRAINT id_pk PRIMARY KEY (id);

SELECT * FROM member;

-- PRIMARY KEY 등록 : 중복불가, null불가
INSERT INTO member VALUES (
    'fff', '1111', '홍길자', 'aaa@aaa.com', '123-456-7890', 'Female', 'golf', SYSDATE
);

COMMIT;

----
-- primary key 등록 시 null 값이 존재하면 안됨, 중복도 존재하면 안됨.
-- PRIMARY KEY 추가, 수정
-- CONSTRAINT id_pk : 이름 설정
ALTER TABLE member ADD CONSTRAINT id_pk PRIMARY KEY (id);

-- PRIMARY KEY 삭제
ALTER TABLE member DROP CONSTRAINT id_pk;

ALTER TABLE member ADD CONSTRAINT id_pk PRIMARY KEY (id);

CREATE TABLE board (
    bno NUMBER(4) PRIMARY KEY,
    btitle VARCHAR2(100) NOT NULL,
    bcontent CLOB,
    id VARCHAR2(30),
    bgroup NUMBER(4),
    bstep NUMBER(4),
    bindent NUMBER(4),
    bhit NUMBER(4),
    bdate DATE,
    bfile VARCHAR2(100)
);

INSERT INTO board VALUES (
    board_seq.NEXTVAL, '제목1', '내용1', 'aaa', board_seq.CURRVAL, 0, 0, 0, SYSDATE, ''
);

INSERT INTO board VALUES (
    board_seq.NEXTVAL, '제목2', '내용2', 'bbb', board_seq.CURRVAL, 0, 0, 0, SYSDATE, ''
);

INSERT INTO board VALUES (
    board_seq.NEXTVAL, '제목5', '내용5', 'eee', board_seq.CURRVAL, 0, 0, 0, SYSDATE, ''
);



SELECT * FROM board;    -- 개수 5개 : bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile
SELECT * FROM bmember;  -- 개수 5개 : id, pw, name, nicname, age, gender, email, bdate

DESC board;

-- 테이블 create할 때, foreign key 생성
CREATE TABLE board2(
    bno NUMBER(4) PRIMARY KEY,
    btitle VARCHAR2(1000) NOT NULL,
    bcontent CLOB,
    id VARCHAR2(30),
    CONSTRAINT fk_board2_id FOREIGN KEY (id) REFERENCES bmember (id)
);

-- 닉네임 : id_fk, foreign key : id, bmember 테이블의 primary key : id 등록
ALTER TABLE board ADD CONSTRAINT id_fk FOREIGN KEY (id) REFERENCES bmember (id);

-- foreign key 삭제
ALTER TABLE board DROP CONSTRAINT id_fk;

SELECT * FROM board;
SELECT * FROM bmember; -- aaa, bbb, ccc, ddd, eee

-- abc 글을 등록하면, 등록이 안됨.
INSERT INTO board VALUES (
    board_seq.NEXTVAL, '제목6', '내용6', 'abc', board_seq.CURRVAL, 0, 0, 0, SYSDATE, ''
);

-- bmember 테이블 id, foreign key로 board, board2에 등록
SELECT * FROM bmember;

-- [ foreign key 등록된 id 삭제 방법 ]
-- foreign key : 외래키
-- 원본의 primary key 데이터를 지우려면, 원칙으로는 foreign key의 데이터를 모두 삭제해야 삭제가 됨.
-- foreign key를 해제해야 삭제 가능
-- primaary key : 기본키
DELETE bmember WHERE id='aaa';
DELETE board WHERE id='aaa';

SELECT * FROM bmember;
SELECT * FROM board;


ALTER TABLE board DROP CONSTRAINT id_fk;

-- foreign key로 등록이 되면, primary key를 삭제할 때 foreign key가 데이터가 있으면 삭제가 안됨.
-- primary key가 삭제가 되면, foreign key로 등록된 모든 글을 삭제시킴
ALTER TABLE board ADD CONSTRAINT id_fk FOREIGN KEY (id) REFERENCES bmember (id) ON DELETE CASCADE;

-- 1. ON DELETE RESTRICTED
-- 기본값 : 입력하지 않을 시, 자식 데이터가 있을 경우, 부모 데이터가 삭제가 되지 않음.
ALTER TABLE board ADD CONSTRAINT id_fk FOREIGN KEY (id) REFERENCES bmember (id);
-- 자식테이블에 aaa로 쓴 데이터를 삭제해야 id를 삭제할 수 있음
DELETE bmember WHERE id = 'aaa';
DELETE board WHERE bno = 3;

-- 2. ON DELETE CASCADE
-- 부모 데이터 삭제 시, 자식 데이터 모두 삭제
ALTER TABLE board ADD CONSTRAINT id_fk FOREIGN KEY (id) REFERENCES bmember (id) ON DELETE CASCADE;
-- 부모 데이터를 삭제하면, 자식 데이터의 모든 글이 삭제됨
DELETE bmember WHERE id = 'aaa';
SELECT * FROM board;

-- 3. ON DELETE SET NULL
-- 부모 데이터 삭제 시, 자식 데이터에 해당되는 값이 NULL 표시
ALTER TABLE board ADD CONSTRAINT id_fk FOREIGN KEY (id) REFERENCES bmember (id) ON DELETE SET NULL;
-- 부모 데이터를 삭제하면 자식 데이터의 해당 컬럼만 null 변경되고, 데이터는 그대로 존재
DELETE bmember WHERE id = 'aaa';
-- 외래키 삭제
ALTER TABLE board DROP CONSTRAINT id_fk;

-- 자식 테이블에 aaa로 쓴 데이터를 삭제해야 id를 삭제할 수 있음
DELETE bmember WHERE id = 'aaa';
--
DELETE board WHERE bno = 3;

ROLLBACK;

--ALTER TABLE board ADD CONSTRAINT fk_board_id FOREIGN KEY (id) REFERENCES bmember (id) ON UPDATE CASCADE;


-- CHECK 구문
CREATE TABLE emp01(
    empno NUMBER(4) PRIMARY KEY,
    ename VARCHAR2(30) NOT NULL,
    salary NUMBER(7,2) CHECK (salary BETWEEN 2000 AND 20000),
    gender VARCHAR2(10) CHECK (gender IN ('Male', 'Female'))
);
-- check가 지정되어 있는 컬럼에 추가
INSERT INTO emp01 VALUES(
    1, '홍길동', 2500, 'Male'
);

-- salary 범위를 벗어나면 에러
INSERT INTO emp01 VALUES(
    2, '유관순', 20000, 'Female'
);

--  Male, Female 이외의 단어 입력 시 에러
INSERT INTO emp01 VALUES(
    3, '이순신', 20000, 'male'
);

DROP TABLE emp01;

-- default : insert 시 값이 입력이 되지 않을 시, 문자, 숫자, 날짜가 넣을 수 있음
CREATE TABLE emp02(
    empno NUMBER(4) PRIMARY KEY,
    ename VARCHAR2(30) DEFAULT '무명',
    income NUMBER(4) DEFAULT 0,
    salary NUMBER(7,2) CHECK (salary BETWEEN 2000 AND 20000),
    gender VARCHAR2(10) CHECK (gender IN ('Male', 'Female')),
    edate DATE DEFAULT SYSDATE
);

INSERT INTO emp02 (empno, salary, gender) VALUES(
    1, 5000, 'Male'
);

SELECT * FROM emp02;

COMMIT;
ROLLBACK;

DROP TABLE board2;
DROP TABLE emp01;
DROP TABLE emp3;
DROP TABLE emp44;
DROP TABLE stu;
DROP TABLE chartable;
DROP TABLE chartable2;
DROP TABLE datetable;


-- 5개만 (5개 * 5개 = 25개)
SELECT bno, btitle, bcontent, nicname, age, gender, pw, email, bgroup, bstep, bindent, bhit, bfile FROM board, bmember
WHERE board.id = bmember.id -- member.id : primary key, board.id : foreign key
;

-- 조인(join)
SELECT employee_id, emp_name, email, salary, employees.department_id, department_name FROM employees, departments
WHERE employees.department_id = departments.department_id
;

SELECT department_id, department_name FROM departments
WHERE department_id = 20;

CREATE TABLE mem(
    id VARCHAR2(30) PRIMARY KEY,
    pw VARCHAR2(30) NOT NULL,
    name VARCHAR2(30) DEFAULT '무명',
    age NUMBER(3) DEFAULT 0,
    birth DATE,
    gender VARCHAR2(6) CHECK (gender IN ('Male', 'Female')),
    hobby VARCHAR2(50) DEFAULT 'game',
    mdate DATE DEFAULT SYSDATE
);

INSERT INTO mem VALUES (
    'aaa', '1111', '홍길동', '24', '2000/05/05', 'Male', 'golf', SYSDATE
);

INSERT INTO mem VALUES (
    'bbb', '1111', '유관순', '24', '2000/06/05', 'Female', 'book', SYSDATE
);

INSERT INTO mem VALUES (
    'ccc', '1111', '이순신', '23', '2001/07/25', 'Male', 'game', SYSDATE
);

COMMIT;

SELECT * FROM mem;

SELECT employees.department_id, departments.department_name, COUNT(employees.department_id) FROM employees, departments
WHERE employees.department_id = departments.department_id AND departments.department_id = 50
GROUP BY employees.department_id, departments.department_name
;

-- employees 테이블 부서번호 50번인, 부서인원, 부서번호, 부서명 가져오시오.
SELECT COUNT(*) person, department_id FROM employees
WHERE department_id = 50
GROUP BY department_id;

-- employees 테이블의 부서번호, 부서이름
SELECT COUNT(*), a.department_id, department_name
FROM employees a, departments b
WHERE a.department_id = b.department_id
GROUP BY a.department_id, department_name
;