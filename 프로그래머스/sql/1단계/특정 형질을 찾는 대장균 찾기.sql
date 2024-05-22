-- 비트 연산으로 문제를 풀자
-- 이진수 1111 일 때 2번째는 0이여야 하고 첫 번째나 세 번째가 1이면 COUNT 하는 문제다.
SELECT COUNT(ID) AS COUNT FROM ECOLI_DATA WHERE (GENOTYPE & 2 = 0) AND (GENOTYPE & 1>0 OR GENOTYPE & 4 > 0)