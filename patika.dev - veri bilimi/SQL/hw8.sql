/* 1- test veritabanınızda employee isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım.*/

CREATE TABLE IF NOT EXISTS employee (id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL, birthday DATE, email VARCHAR(100));

/* 2- Oluşturduğumuz employee tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.*/

INSERT INTO employee (name, email, birthday) VALUES ('Tedda Ternent', 'tternent0@narod.ru', '2021-02-28');
...
INSERT INTO employee (name, email, birthday) VALUES ('Euell Teese', 'eteese2r@purevolume.com', null);

/* 3- Sütunların her birine göre diğer sütunları güncelleyecek 5 adet UPDATE işlemi yapalım.*/

UPDATE employee SET name = 'Ömer Korkmaz', birthday = '2003-05-19', email = 'thefoxing06@gmail.com' WHERE id = 1;
...
UPDATE employee SET name = 'Sinem Korkmaz', birthday = '2003-07-19', email = NULL WHERE id = 2;

/* 4- Sütunların her birine göre ilgili satırı silecek 5 adet DELETE işlemi yapalım.*/

DELETE FROM employee WHERE name LIKE '%Korkmaz';
...
DELETE FROM employee WHERE name LIKE '%a';