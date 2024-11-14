SELECT sysdate FROM dual;

SELECT sysdate - 30, sysdate, sysdate + 30 FROM dual;

-- employees 테이블 hire_date 컬럼
SELECT hire_date, hire_date - 1 FROM employees;

-- 날짜 범위 검색가능, 정렬 ORDER BY, ASC: 순차 정렬, DESC: 역순 정렬
SELECT emp_name, hire_date FROM employees
WHERE hire_date >= '02/01/01' AND hire_date <= '04/12/31'
ORDER BY hire_date DESC;

SELECT emp_name, hire_date FROM employees
WHERE hire_date BETWEEN '02/01/01' AND '04/12/31'
ORDER BY hire_date DESC;

-- LIKE
SELECT emp_name FROM employees
WHERE emp_name LIKE '___a%';

SELECT emp_name FROM employees
WHERE emp_name LIKE '%a_';

-- 정렬 DESC: null 값이 제일 위에 검색, ASC: 제일 아래에 검색
SELECT department_id FROM employees
ORDER BY department_id DESC;

-- students 테이블에서 total 역순 정렬
SELECT no, name, total FROM students
ORDER BY total DESC;

-- hire_date 기준, 순차정렬
SELECT * FROM employees
ORDER BY hire_date ASC;

SELECT name, kor, eng, math FROM students
ORDER BY kor DESC, eng DESC;

SELECT name, kor, eng, math FROM students
ORDER By kor DESC;

-- 한국어 순차 정렬:ㄱ, ㄴ, ㄷ, ... , 역순 정렬: ㅎ, ㅍ, ㅌ, ...
SELECT name FROM students
ORDER BY name;

-- 입사일이 빠른 순으로 정렬하는데, 이름은 역순으로 정렬하시오.
SELECT emp_name, hire_date FROM employees
ORDER BY hire_date ASC, emp_name DESC;

-- ABS 절대값
SELECT -10, ABS(-10) AS 절대값 FROM dual;

SELECT kor, kor - eng, ABS(kor - eng) abs FROM students
ORDER BY abs DESC;

-- FLOOR 소수점 이하 버림
SELECT 3.141592, FLOOR(3.141592) FROM dual;
-- TRUNC : 버림, 자리수 지정
SELECT 34.5678, TRUNC(34.5678, 2) FROM dual;

-- ceil 소수점 이하 올림
SELECT 3.141592, CEIL(3.141592) FROM dual;

-- ROUND 반올림, 자리수 범위 지정
SELECT 34.5678, ROUND(34.5678) FROM dual;
SELECT 34.5678, TRUNC(34.5678, -1) FROM dual;

-- 소수점 둘째자리까지 출력, 셋째자리에서 반올림 됨.
SELECT 34.5678, ROUND(34.5678, 2) FROM dual;

-- 양수 첫째자리에서 반올림, 소수점자리수에서 앞쪽으로 한칸 위치 반올림.
SELECT 34.5678, ROUND(34.5678, -1) FROM dual;

-- mod: 나머지
SELECT 27/2, MOD(27,2) FROM dual;
SELECT 30/3, MOD(31,7) FROM dual;

-- 사원번호가 홀수 인 사원을 출력하시오.
SELECT employee_id, emp_name FROM employees
WHERE MOD(employee_id, 2) = 1
ORDER BY employee_id;

-- 최종연봉 : 월급 * 12 + (월급 * 12) * 커미션, 소수점 2자리에서 반올림, 첫째자리로 만들시오.
SELECT salary, TRUNC(salary * 12 + ((salary * 12) * NVL(commission_pct, 0)) * 1386.86795, 1) ysalary FROM employees;

SELECT * FROM students;

-- 시퀀스 : 자동으로 번호 부여
CREATE SEQUENCE stu_seq
START WITH 1
INCREMENT BY 1
MINVALUE 1
MAXVALUE 9999
NOCYCLE
NOCACHE;

-- 시퀀스에서 번호 생성
SELECT stu_seq.NEXTVAL FROM dual;

SELECT stu_seq.CURRVAL FROM dual;

-- 게시판 테이블 생성
CREATE TABLE board(
    bno NUMBER(4),
    btitle VARCHAR2(100),
    bcontent VARCHAR2(4000),
    id VARCHAR2(30),
    bhit NUMBER(10),
    hdate DATE
);

INSERT INTO board VALUES(
    1,'제목입니다.','내용입니다.','aaa',1,SYSDATE
);

INSERT INTO board VALUES(
    2,'제목입니다.2','내용입니다.2','aaa',1,SYSDATE
);

INSERT INTO board VALUES(
    stu_seq.NEXTVAL,'제목입니다.','내용입니다.','aaa',1,SYSDATE
);

SELECT * FROM board;
COMMIT;

CREATE SEQUENCE board_seq
START WITH 15       -- 시작번호
INCREMENT BY 1      -- 증감 숫자
MINVALUE 1          -- 최소값
MAXVALUE 9999       -- 최대값
NOCYCLE             -- 1 - 9999 이상이 되면, 다시 1
NOCACHE             -- 메모리에 시퀀스값 미리 할당
;

INSERT INTO board VALUES(
    board_seq.NEXTVAL, '제목15', '내용15', 'aaa', 1, SYSDATE
);

SELECT * FROM board;

UPDATE board SET btitle = '제목을 다시 변경' WHERE bno = 15;
COMMIT;

DROP TABLE board;

CREATE TABLE board(
    bno NUMBER(4),
    btitle VARCHAR2(100),
    bcontent clob,          -- 대용량 글자 타입
    id VARCHAR2(20),
    bgroup NUMBER(4),       -- 답변 달기 그룹핑
    bstep NUMBER(4),        -- 답변 달기 경우 순서정의
    bindent NUMBER(4),      -- 답변 달기 들여쓰기
    bhit NUMBER(10),        -- 조회수
    bdate DATE              -- 등록일
);

SELECT board_seq.CURRVAL from dual;

INSERT INTO board VALUES (
    board_seq.NEXTVAL, '제목1','내용1','aaa',board_seq.CURRVAL, 0, 0, 1, SYSDATE
);

SELECT * FROM board;

-- 시퀀스 생성
-- students_seq.NEXTVAL
-- students 테이블 100 -> 101
-- 101, '홍길순', 99, 99, 90, total, avg, rank, date
-- 1명을 입력하시오.

CREATE SEQUENCE students_seq
START WITH 101
INCREMENT BY 1
MINVALUE 1
MAXVALUE 9999
NOCYCLE
NOCACHE
;

INSERT INTO students VALUES (
    students_seq.NEXTVAL, '홍길순', 99, 99, 90, 99+99+90, (99+99+90)/3, 1, SYSDATE
);

SELECT * FROM students;

-- DELETE students WHERE name='홍길순';
COMMIT;

SELECT no, name, kor, eng, math, total, ROUND(avg, 2), rank, sdate FROM students;

SELECT ROUND(avg, 2) FROM students;
SELECT s.*, ROUND(avg, 2) FROM students s;

SELECT dept_seq.NEXTVAL FROm dual;

-- s_seq
-- 시작 1, 증분 1, 최대값 99999
CREATE SEQUENCE s_seq
START WITH 1
INCREMENT BY 1
MAXVALUE 99999
NOCYCLE
NOCACHE
;

-- 시퀀스 생성, NEXTVAL: 다음 시퀀스번호 생성, CURRVAL: 현재 시퀀스 번호 보여줌
SELECT s_seq.NEXTVAL FROM dual;
SELECT emp_seq.NEXTVAL FROM dual;
SELECT emp_seq.CURRVAL FROM dual;

--DROP SEQUENCE s_seq;

-- 타입
-- 문자형, 숫자형, 날짜형
-- char, varchar2, nchar, nvarchar2, long, clob
-- char, varchar2: 한글문자 입력시, 3byte 사용
-- varchar2(6): 한글 2글자 입력
-- nvarchar2(5): 한글 입력 5자리까지 입력가능 - 2byte
-- number
-- date - 초까지 입력, timestamp - 밀리세컨드까지 입력

SELECT '홍길동' FROM dual;
-- LENGTH: 문자 길이
SELECT LENGTH('홍길동') FROM dual;

-- 이름의 길이로 역순정렬
SELECT name, LENGTH(name) n FROM students
ORDER BY n DESC;

-- LENGTHB: byte 크기
SELECT LENGTHB('홍길동') FROM dual;

SELECT * FROM studnets;

-- 합계 200점 이상이면서, 번호가 10이상 50번 이하이면서 이름의 2번째 자리에 e가 들어가 있는 학생을 출력하시오.
SELECT * FROM students
WHERE total >= 200 AND 10 <= no AND no <= 50 AND name LIKE '_e%';

SELECT * FROM students
WHERE total >= 200;

-- SELECT * FROM 테이블

SELECT * FROM (
    SELECT * FROM students
    WHERE total >= 200
) WHERE name LIKE '_e%' AND no >= 30;

ROLLBACK;
SELECT * FROM students;

SELECT no, name, total, rank FROM students;

-- 등수함수: RANK() OVER(기준점) 입력, no 중복이 없음, 유일키, 기본키, 프라이머리 키(primary key)
SELECT no, RANK() OVER(ORDER BY total DESC) ranks FROM students;
SELECT ranks FROM (SELECT no, RANK() OVER(ORDER BY total DESC) ranks FROM students);
SELECT * FROM students;

SELECT no, name, total FROM students
ORDER BY total DESC;

-- 수정: UPDATE
UPDATE students SET rank = 1
WHERE no = 101;

UPDATE students a
SET rank = (SELECT ranks
FROM
(SELECT no, RANK() OVER(ORDER BY total DESC) ranks FROM students) b
WHERE a.no = b.no);

SELECT * FROM students ORDER BY rank;

ROLLBACK;

SELECT no, RANK() OVER(ORDER BY total DESC) AS ranks FROM students;

UPDATE students
SET rank = 1
WHERE no = 101;

UPDATE students
SET rank = 2
WHERE no = 96;

UPDATE students
SET rank = 3
WHERE no = 64;

UPDATE students
SET rank = 4
WHERE no = 49;

UPDATE students
SET rank = 5
WHERE no = 14;

-- 사원번호가 높은 순으로 등수를 생성하시오.
-- 사원번호, 사원명, 등수
SELECT * FROM employees
ORDER BY employee_id DESC;

SELECT employee_id, emp_name, RANK() OVER(ORDER BY employee_id DESC) AS RANKS FROM employees;

-- emp2 테이블 복사, employees 테이블 복사 생성
CREATE TABLE emp2 AS SELECT * FROM employees;

-- RANK() 실행
SELECT RANK() OVER(ORDER BY employee_id DESC) FROM employees;

DESC emp2;
-- 테이블 컬럼 추가
ALTER TABLE emp2 ADD rank NUMBER(4);

DESC emp2;

SELECT * FROM emp2;

-- RANK() 등수를 rank에 입력
UPDATE emp2 e SET rank = (
    SELECT ranks FROM (SELECT employee_id, RANK() OVER(ORDER BY employee_id DESC) ranks FROM emp2) e2
    WHERE e.employee_id = e2.employee_id
);

SELECT * FROM emp2;


-- 컬럼의 순서를 변경
-- emp_name 뒤에 rank 컬럼 배치

ALTER TABLE emp2 MODIFY email INVISIBLE;
ALTER TABLE emp2 MODIFY phone_number INVISIBLE;
ALTER TABLE emp2 MODIFY hire_date INVISIBLE;
ALTER TABLE emp2 MODIFY salary INVISIBLE;
ALTER TABLE emp2 MODIFY manager_id INVISIBLE;
ALTER TABLE emp2 MODIFY commission_pct INVISIBLE;
ALTER TABLE emp2 MODIFY retire_date INVISIBLE;
ALTER TABLE emp2 MODIFY department_id INVISIBLE;
ALTER TABLE emp2 MODIFY job_id INVISIBLE;
ALTER TABLE emp2 MODIFY create_date INVISIBLE;
ALTER TABLE emp2 MODIFY update_date INVISIBLE;
-- 컬럼을 나타남
ALTER TABLE emp2 MODIFY email VISIBLE;
ALTER TABLE emp2 MODIFY phone_number VISIBLE;
ALTER TABLE emp2 MODIFY hire_date VISIBLE;
ALTER TABLE emp2 MODIFY salary VISIBLE;
ALTER TABLE emp2 MODIFY manager_id VISIBLE;
ALTER TABLE emp2 MODIFY commission_pct VISIBLE;
ALTER TABLE emp2 MODIFY retire_date VISIBLE;
ALTER TABLE emp2 MODIFY department_id VISIBLE;
ALTER TABLE emp2 MODIFY job_id VISIBLE;
ALTER TABLE emp2 MODIFY create_date VISIBLE;
ALTER TABLE emp2 MODIFY update_date VISIBLE;

SELECT * FROM emp2;

-- 컬럼 삭제
DESC emp2;

ALTER TABLE emp2 DROP COLUMN email;
ALTER TABLE emp2 DROP COLUMN phone_number;

ALTER TABLE emp2 DROP COLUMN hire_date;
ALTER TABLE emp2 DROP COLUMN salary;
ALTER TABLE emp2 DROP COLUMN commission_pct;
ALTER TABLE emp2 DROP COLUMN retire_date;
ALTER TABLE emp2 DROP COLUMN create_date;
ALTER TABLE emp2 DROP COLUMN update_date;

SELECT * FROM emp2;

SELECT * FROM departments;

DESC departments;

ALTER TABLE emp2 ADD department_name VARCHAR2(80);
-- 부서명이 없음.
SELECT * FROM emp2;

-- 부서명은 departments
SELECT * FROM departments;

SELECT department_id, department_name FROM emp2;
SELECT department_id, department_name FROM departments;

UPDATE emp2 SET department_name = '배송부'
WHERE department_id = 50;

UPDATE emp2 e SET department_name = (
    SELECT department_name FROM departments d
    WHERE e.department_id = d.department_id
);

SELECT department_id, department_name FROM emp2;

--DROP TABLE stu;

-- 테이블 복사
CREATE TABLE stu AS SELECT * FROM students;

DESC stu;
ALTER TABLE stu DROP COLUMN rank;

SELECT * FROM stu;

-- total 컬럼, avg 컬럼 추가하시오.
ALTER TABLE stu ADD total NUMBER(3);
ALTER TABLE stu ADD avg NUMBER;
ALTER TABLE stu ADD rank NUMBER(3);

ALTER TABLE stu MODIFY sdate INVISIBLE;
ALTER TABLE stu MODIFY sdate VISIBLE;

--

ROLLBACK;

SELECT * FROM stu;

-- 합계, 평균 추가
UPDATE stu SET total = kor+eng+math, avg = (kor+eng+math)/3;

SELECT no, name, RANK() OVER(ORDER BY total DESC) rank FROM stu;

-- rank 입력
UPDATE stu s SET rank = (
    SELECT ranks FROM (SELECT no, RANK() OVER(ORDER BY total DESC) ranks FROM stu) s2
    WHERE s.no = s2.no
);

SELECT * FROM stu;

COMMIT;

----- 날짜 함수
-- 현재 날짜: SYSDATE
SELECT SYSDATE FROM dual;
SELECT SYSDATE - 1 FROM dual;
SELECT SYSDATE + 30 FROM dual;

CREATE TABLE datetable (
    no NUMBER(4),
    predate DATE,
    today DATE,
    nextdate DATE
);

-- 회원가입 1달치, 6개월, 1년
INSERT INTO datetable VALUES (
    1, SYSDATE - 30, SYSDATE, SYSDATE + 180
);

SELECT no, predate, today AS "가입일", nextdate 만료일  FROM datetable;


SELECT * FROM member;

SELECT id, name, mdate, SYSDATE, ROUND(SYSDATE - mdate) FROM member
WHERE SYSDATE >= mdate + 180
;

-- 입사일 현재날짜와 입사일 몇일 지났는지 출력하시오.
-- employees, hire_date
SELECT SYSDATE-hire_date, ROUND(SYSDATE - hire_date) FROM employees;

-- 15일 이상이면 1달을 올림, 15일 미만이면 일을 초기화
SELECT hire_date, ROUND(hire_date, 'month') FROM employees;

-- 일의 숫자를 1로 초기화
SELECT hire_date, TRUNC(hire_date, 'month') FROM employees;

-- 입사일, 현재일 기준의 달수
SELECT hire_date, SYSDATE, MONTHS_BETWEEN(SYSDATE, hire_date) FROM employees;
-- MONTHS_BETWEEN: 두 일자 가운데 지나간 달수를 알려줌
SELECT hire_date, SYSDATE, ROUND(MONTHS_BETWEEN(SYSDATE, hire_date)) 달수, ROUND(SYSDATE - hire_date) 일수 FROM employees;

-- ADD_MONTHS 3개월 추가
SELECT hire_date, ADD_MONTHS(hire_date, 3) FROM employees;

-- NEXT_DAY: 다음 주 수요일 날짜를 알려줌.
SELECT SYSDATE, NEXT_DAY(SYSDATE, '수요일') FROM dual;

SELECT SYSDATE, NEXT_DAY(SYSDATE, '토요일') FROM dual;
 
-- LAST_DATE: 그 달의 마지막 날짜를 알려줌
SELECT hire_date, LAST_DAY(hire_date) FROM employees;

SELECT SYSDATE, LAST_DAY(SYSDATE) FROM dual;

-- 형변환 함수
SELECT SYSDATE FROM dual;
SELECT TO_CHAR(SYSDATE, 'yyyy/mm/dd hh24:mi:ss') FROM dual;

SELECT hire_date, TO_CHAR(hire_date, 'yyyy-mm-dd') FROM employees;

SELECT * FROM member WHERE id='aaa' AND pw='1111';

SELECT * FROM member;

UPDATE member SET id='abc', pw='1111', name='my_name', email='mymail@gmail.com'
WHERE id='Trineman';

SELECT * FROM member WHERE id='abc';

SELECT * FROM member WHERE id='aaa';