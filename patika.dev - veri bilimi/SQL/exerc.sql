/* 1- film tablosundan 'K' karakteri ile başlayan en uzun ve replacement_cost u en düşük 4 filmi sıralayınız. */

SELECT * FROM film WHERE title LIKE 'K%' ORDER BY length DESC, replacement_cost LIMIT 4;

/* 2- film tablosunda içerisinden en fazla sayıda film bulunduran rating kategorisi hangisidir? */

SELECT rating FROM film GROUP BY rating ORDER BY COUNT(*) DESC LIMIT 1;

/* 3- customer tablosunda en çok alışveriş yapan müşterinin adı nedir? */

SELECT CONCAT(first_name,' ',last_name) FROM customer WHERE customer_id = (SELECT customer_id FROM payment GROUP BY customer_id ORDER BY COUNT(*) DESC LIMIT 1);

/* 4- category tablosundan kategori isimlerini ve kategori başına düşen film sayılarını sıralayınız. */

SELECT name, COUNT(*) FROM category JOIN film_category ON category.category_id = film_category.category_id GROUP BY name ORDER BY COUNT(*) DESC; 

/* 5- film tablosunda isminde en az 4 adet 'e' veya 'E' karakteri bulunan kaç tane film vardır? */

SELECT COUNT(*) FROM film WHERE title ILIKE '%e%e%e%e%';

/* 6- category tablosundan kategori isimlerini ve bu kategorilerle eşleşen filmleri sıralayınız. */

SELECT film.title, category.name FROM category JOIN film_category ON category.category_id = film_category.category_id JOIN film ON film_category.film_id = film.film_id;