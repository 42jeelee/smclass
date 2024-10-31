SELECT * FROM member;

UPDATE member SET id = 'abc', pw = '1111', name = 'my_name', email = 'jeelee553@gmail.com'
WHERE id = 'abc';
COMMIT;

SELECT * FROM member;

UPDATE member SET pw = '1111' WHERE id = 'Towell';
COMMIT;

SELECT SYSDATE - 1, SYSDATE, SYSDATE + 1 FROM dual;
SELECT hire_date, ROUND(hire_date, 'month') FROM employees;
SELECT hire_date, TRUNC(hire_date, 'month') FROM employees;

SELECT ADD_MONTHS(TRUNC(SYSDATE, 'month'), 1) FROM dual;

-- VIP요금제로 변경을 하면 다음달부터 1일부터 혜택
SELECT SYSDATE, ADD_MONTHS(TRUNC(SYSDATE, 'month'),1) FROM dual;

-- 입사일 기준 다음달 1일부터 혜택을 주겠다고 함.
-- 입사일 다음달 1일 출력하시오.
SELECT hire_date, ADD_MONTHS(TRUNC(hire_date, 'month'), 1) FROM employees;

-- 입사일 기준 1년 후 날짜를 출력하시오.
SELECT SYSDATE, ADD_MONTHS(SYSDATE, 12) FROM employees;
SELECT SYSDATE, SYSDATE + 365, ADD_MONTHS(SYSDATE, 12) FROM employees;

SELECT hire_date, ADD_MONTHS(hire_date, 12) FROM employees;

-- 입사일 기준 1년 후 날짜와, 1년 후 마지막 그 달의 날짜를 출력하시오.
SELECT hire_date, LAST_DAY(hire_date) FROM employees;

SELECT hire_date, ADD_MONTHS(hire_date, 12), LAST_DAY(ADD_MONTHS(hire_date, 12)) FROM employees;


-- 입력일 기준 1년 후 마지막 날짜가 8/31, 11/30, 12/31인 학생들을 모두 출력하시오.
SELECT sdate FROM students;

SELECT sdate, ADD_MONTHS(sdate, 12) sdate2, ADD_MONTHS(LAST_DAY(sdate), 12) sdate3 FROM students
WHERE ADD_MONTHS(LAST_DAY(sdate), 12) IN ('25/8/31', '25/11/30', '25/12/31');

SELECT sdate, ADD_MONTHS(sdate, 12) sdate2, ADD_MONTHS(LAST_DAY(sdate), 12) sdate3 FROM students
WHERE ADD_MONTHS(LAST_DAY(sdate), 12) = '25/8/31'
OR ADD_MONTHS(LAST_DAY(sdate), 12) = '25/11/30'
OR ADD_MONTHS(LAST_DAY(sdate), 12) = '25/12/31';

SELECT sdate, ADD_MONTHS(sdate, 12) sdate2, ADD_MONTHS(LAST_DAY(sdate), 12) sdate3 FROM students
WHERE TO_CHAR(sdate, 'mm') IN ('08', '11', '12');

-- EXTRACT 함수 : 특정 년, 월, 일, 시, 분, 초 만 분리해서 가져오는 함수
-- SYSDATE 년, 월, 일
SELECT SYSDATE FROM dual;
SELECT EXTRACT(year FROM SYSDATE) FROM dual;
SELECT EXTRACT(month FROM SYSDATE) FROM dual;
SELECT EXTRACT(day FROM SYSDATE) FROM dual;

-- SYSTIMESTAMP 년, 월, 일, 시, 분, 초
SELECT SYSTIMESTAMP FROM dual;
SELECT EXTRACT(hour FROM SYSTIMESTAMP) FROM dual;
SELECT EXTRACT(minute FROM SYSTIMESTAMP) FROM dual;
SELECT EXTRACT(second FROM SYSTIMESTAMP) FROM dual;

SELECT sdate, EXTRACT(month FROM sdate) FROM students
WHERE EXTRACT(year FROM LAST_DAY(sdate+365)) = 2025 AND EXTRACT(month FROM LAST_DAY(sdate+365)) In (8, 11, 12)
;

-- SUBSTR 함수 : 문자에서 시작위치, 가져올 개수
SELECT SUBSTR(SYSDATE, 4, 2) FROM dual;

SELECT sdate, LAST_DAY(sdate + 365) sdate2 FROM students
WHERE SUBSTR(LAST_DAY(sdate + 365), 4, 2) IN (8, 11, 12)
ORDER BY sdate2
;

-- 날짜 -> 문자 to_char     ## 날짜포맷
-- 문자 -> 날짜 to_date     ## 날짜 사칙연산
-- 숫자 -> 문자 to_char     ## 천단위, 숫자앞에 0 을표시, 통화표시
-- 문자 -> 숫자 to_number   ## 천단위 표시 , 천단위 삭제해서 사칙연산

-- 날짜 형변환해서 날짜 포맷을 변경
-- date 타입 -> char 타입으로 변경해서 포맷.
SELECT SYSDATE FROM dual;
SELECT SYSDATE, TO_CHAR(SYSDATE, 'yyyy-mm-dd') FROM dual;
SELECT SYSDATE, TO_CHAR(SYSDATE, 'yyyy-mm-dd hh24:mi:ss') FROM dual;
SELECT SYSDATE, TO_CHAR(SYSDATE, 'yyyy-mm-dd am hh:mi:ss day') FROM dual;
SELECT SYSDATE, TO_CHAR(SYSDATE, 'yy-mm-dd hh24:mi:ss dy') FROM dual;
SELECT SYSDATE, TO_CHAR(SYSDATE, 'yy-MON-dd hh24:mi:ss') FROM dual;

SELECT hire_date, TO_CHAR(hire_date, 'yyyy-mm-dd hh:mi:ss') FROM employees;

-- students 테이블 sdate 2024/01/01 형태로 출력하시오.
SELECT sdate, TO_CHAR(sdate, 'yyyy/mm/dd') FROM students;

SELECT kor FROM students
WHERE kor=70;

-- 숫자타입 -> 문자타입 변경해서 포맷 천단위 표시
SELECT salary * 1382.86 * 12 FROM employees;

-- 자릿수 채우기 9 : 빈공백으로 채움, 0 : 0으로 채움
-- L : 국가통화기호 표시, $ : $표시가 됨.
SELECT TO_CHAR(salary * 1382.86 * 12, 'L999,999,999') FROM employees;

SELECT TO_CHAR(12, '00000') FROM dual;
SELECT 12 FROM dual;

SELECT TO_CHAR(123456, '000000000'),TO_CHAR(123456, '999,999,999') FROM dual;

CREATE TABLE chartable2 (
    no NUMBER(4),
    kor NUMBER(10),
    kor_char NUMBER(10),
    kor_mark NUMBER(10)
);

INSERT INTO chartable2 VALUES (
    3, 3000000, 3000000, 3000000
);

-- 숫자형타입은 숫자앞에 0 있어도 표시가 되지 않음. : 문자형 타입만 가능
-- 천단위 표시는 숫자형 타입에 입력이 안됨 : 문자형 타입에만 가능
INSERT INTO chartable2 VALUES (
    5, 5000000, 005000000, 005000000
);

COMMIT;

-- NUMBER, NUMBER, str - NUMBER 타입을 넣어도 입력
-- 문자형 타입에는 숫자형 타입 가능
INSERT INTO chartable VALUES (
    1, 10000, TO_CHAR(10000, '00000000'), TO_CHAR(100000, '0,000,000')
);

SELECT * FROM chartable;

-- 숫자형 타입, 문자형(숫자)타입은 사칙연산 가능
-- 숫자형 타입과 문자 천단위 표시 숫자타입은 사칙연산 불가능, 천단위 표시는 문자형 타입
-- 숫자형 타입 + 문자(숫자형) 타입 = 두 타입 결과값 출력됨.
SELECT kor + kor_char FROM chartable;
SELECT kor + kor_mark FROM chartable;

DESC chartable; -- NUMBER, VARCHAR2
DESC chartable2; -- 모든타입 NUMBER

SELECT * FROM chartable;

INSERT INTO chartable VALUES (
    1,10000,10000,10000
);

-- 2일 이후의 날짜를 출력하시오.
SELECT '20241031', TO_DATE('20241031') + 2 FROM dual;
SELECT SYSDATE, SYSDATE + 2 FROM dual;

SELECT TO_DATE('20241031') + 2 FROM dual;

SELECT TO_DATE('20231031') FROM dual;

-- NUMBER형 타입 -> 날짜형 타입
SELECT SYSDATE - TO_DATE(20231101) FROM dual;
-- 문자형 타입 -> 날짜형 타입
SELECT SYSDATE - TO_DATE('20231101') FROM dual;

-- 문자형 타입 -> 숫자형 타입
-- 천단위 문자형 타입 -> 천단위 제외 숫자형 타입
SELECT TO_NUMBER('20,000', '999,999') FROM dual;
-- 문자형 천단위 타입 -> 숫자형 타입 변환
SELECT kor, TO_NUMBER(kor_mark, '999,999,999') FROM chartable;

-- 숫자형 타입 이기에 사칙연산 가능
SELECT kor + TO_NUMBER(kor_mark, '999,999,999') FROM chartable;

SELECT department_id FROM employees;

SELECT department_id FROM employees WHERE department_id IS NULL;

SELECT commission_pct FROM employees
WHERE commission_pct IS NOT NULL;

-- 월급 * 커미션을 계산하시오.
SELECT salary + salary * NVL(commission_pct, 0) FROM employees;

-- null 경우 : 0 표시
SELECT NVL(department_id, 0) FROM employees;

-- null 경우 : CEO 표시 숫자형 타입을 문자형 타입으로 변경
SELECT NVL(TO_CHAR(department_id), 'CEO') FROM employees;

-- 그룹함수
-- SUM : 합계, AVG : 평균, COUNT : 개수, MIN : 최소값, MAX : 최대값, MEDIAN : 중간값

SELECT salary FROM employees;

SELECT SUM(salary) FROM employees;
SELECT TO_CHAR(SUM(salary), '999,999') FROM employees;

SELECT AVG(salary) FROM employees;
-- 소수점 2자리 반올림
SELECT ROUND(AVG(salary), 4) FROM employees;
SELECT TRUNC(AVG(salary), 4) FROM employees;
-- 최대값, 최소값
SELECT MAX(salary) FROM employees;
SELECT MIN(salary) FROM employees;

-- 평균값보다 월급이 높은 사원을 출력하시오.
SELECT AVG(salary) FROM employees;

SELECT COUNT(salary) FROM employees
WHERE salary >= 6461.83
;

SELECT COUNT(salary) FROM employees
WHERE salary >= (SELECT AVG(salary)FROM employees)
;

-- emp_name : 단일함수, AVG : 그룹함수
SELECT emp_name, AVG(salary) FROM employees;
-- 단일함수, 그룹함수 함께 사용할 수 없음.
SELECT department_id, MAX(salary) FROM employees;


-- students 테이블 모든 학생의 kor점수 합계, 평균, 최대값, 최소값을 구하시오.
SELECT kor FROm students;

SELECT SUM(kor), AVG(kor), MAX(kor), MIN(kor), MEDIAN(kor) FROM students;

-- 부서번호가 50 사원들의 월급의 합, 평균, 최대값, 최소값을 출력하시오.
SELECT SUM(salary), AVG(salary), MAX(salary), MIN(salary)
FROM employees WHERE department_id = 50;

-- 부서번호가 30
SELECT SUM(salary), AVG(salary), MAX(salary), MIN(salary)
FROM employees WHERE department_id = 30;
SELECT SUM(salary), AVG(salary), MAX(salary), MIN(salary)
FROM employees WHERE department_id = 10;

SELECT MAX(salary) FROM employees
WHERE department_id = 50;

SELECT department_id, MAX(salary) FROM employees
GROUP BY department_id;

SELECT emp_name, salary FROM employees;

-- 107명 평균
SELECT AVG(salary) FROM employees;

SELECT emp_name, MAX(salary) FROM employees
GROUP BY emp_name;

-- 단일함수, 그룹함수 함께 사용하려면, GROUP BY 지정
SELECT department_id, ROUND(AVG(salary)), MAX(salary), MIN(salary) FROM employees
GROUP BY department_id
ORDER BY department_id;

-- 평균 월급보다 높은 사람 수를 출력하시오.
SELECT COUNT(salary), MIN(salary), MAX(salary) FROM employees
WHERE salary >= (SELECT AVG(salary) FROM employees);

-- 수학함수 : ABS : 절대값, CEIL : 올림, FLOOR : 버림, ROUND : 반올림, TRUNC : 절삭, MOD : 나머지, POWER : 제곱, SQRT : 제곱근
-- 제곱
SELECT POWER(2, 3), 2 * 2 * 2 FROM dual;

-- 문자, 숫자형 타입 -> 날짜형 타입 변경가능
-- 숫자, 날짜형 타입 -> 문자형 타입 변경가능
-- 문자형 타입 -> 숫자형 타입 변경가능
-- 날짜형 타입 -> 숫자형 타입 변경불가
-- 날짜형 타입 -> 숫자형타입 변경불가, 형태를 변경해서 문자형으로 변경한 후, 숫자형으로 변경가능
SELECT 20240101, TO_DATE(20240101) FROM dual;
SELECT '2', TO_NUMBER('2') FROM dual;

SELECT '20240101', TO_NUMBER('20240101') FROM dual;
SELECT TO_DATE('20240101') FROM dual;

-- 날짜형 -> 문자형 변환
SELECT SYSDATE, TO_NUMBER(TO_CHAR(SYSDATE, 'yyyymmdd')) FROM dual;

-- 날짜형타입을 문자형 타입으로 변경시, 년 월 일 한글, 특수문자 입력방법
SELECT SYSDATE, TO_CHAR(SYSDATE, 'yyyy"년" mm"월" dd"일" day') FROM dual;
SELECT SYSDATE, TO_CHAR(SYSDATE, 'yyyy/mm/dd day') FROM dual;

-- 숫자형 타입 : 사칙연산 계산해서 출력됨.
SELECT employee_id + salary FROM employees;

-- 문자형 함수
SELECT emp_name, email FROM employees;

-- 문자형 타입을 합쳐서 + 기호를 사용해서 합치려고 하면 에러
--SELECT emp_name + email FROM employees;

-- ||, concat 함수
SELECT emp_name || email FROM employees; -- 속도가 조금 더 빠름
SELECT CONCAT(emp_name, email) FROM employees;

SELECT name FROM member;

-- lower : 소문자 치환, upper : 대문자 치환, initcap : 첫글자 대문자 치환
SELECT * FROM member
WHERE lower(name) = 'bryan';

SELECT 'joHn', INITCAP('joHn'), LOWER('joHn'), UPPER('joHn') FROM dual;

-- LPAD : 왼쪽 자리수 채우기
SELECT 'john', LPAD('john', 10, '#') FROM dual;

-- RPAD : 오른쪽 자리수 채우기
SELECT 'john', RPAD('john', 10, '#') FROM dual;

-- TRIM : 앞뒤 공백 없애기, LTRIM : 왼쪽 공백, RTRIM : 오른쪽 공백
SELECT LENGTH('    aaa   '), LENGTH(TRIM('    aaa   ')) FROM dual;
-- REPLACE : 치환
SELECT '   a  b c  ', TRIM('   a  b c  ') FROM dual;

SELECT LENGTH('    a  b c   '), LENGTH(TRIM('    a  b c   ')), LENGTH(REPLACE('    a  b c   ', ' ','')) FROM dual;

-- SUBSTR : 특정 위치 자르기 ( 시작위치, 개수 )
SELECT 'abcedfg', SUBSTR('abcedfg', 0, 3), SUBSTR('abcedfg', 3, 2) FROM dual;

-- 입사일이 3, 8, 10월인 사원을 출력하시오.
SELECT * FROM employees
WHERE TO_CHAR(hire_date, 'mm') = '03';

SELECT hire_date, SUBSTR(hire_date, 4, 2) FROM employees
WHERE SUBSTR(hire_date, 4, 2) IN (3, 8, 10);

-- 7월 이상
SELECT hire_date, SUBSTR(hire_date, 4, 2) FROM employees
WHERE SUBSTR(hire_date, 4, 2) >= 7;

-- TRANSLATE 치환
-- 한글자, 한글자에 해당되는 단어를 각각의 단어로 치환
-- 순서에 없는 변환글자는 삭제처리
SELECT 'axyz', TRANSLATE('axyzxbbcyaccx', 'xy', 'ab') FROM dual;
SELECT 'axyz', REPLACE('axyzxbbcyaccx', 'xy', 'ab') FROM dual;

-- LEGNTH() : 문자열 길이
-- students 테이블 name 글자 길이가 10자 이상인 학생만 출력하시오.
SELECT COUNT(*) FROM students
WHERE LENGTH(name) >= 10;

-- 사원의 월급의 합과 평균을 구하시오.
SELECT SUM(salary), ROUND(AVG(salary)) FROM employees;
-- 영어 점수의 합, 평균, 최대값, 최소값을 구하시오.
SELECT SUM(eng), ROUND(AVG(eng)), MAX(eng), MIN(eng) FROM students;
-- students 테이블에서
-- 홍길동, 등록일 : 2023년 12월 02일
-- 유관순, 등록일 : 2024년 01월 19일...
SELECT name, TO_CHAR(sdate, '"등록일 :" yyyy"년" mm"월" dd"일"') 등록일 FROM students;
SELECT name || ', ' || TO_CHAR(sdate, '"등록일 :" yyyy"년" mm"월" dd"일"') 등록일 FROM students;
