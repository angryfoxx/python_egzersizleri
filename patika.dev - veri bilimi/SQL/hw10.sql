/* 1- city tablosu ile country tablosunda bulunan şehir (city) ve ülke (country) isimlerini birlikte görebileceğimiz LEFT JOIN sorgusunu yazınız. */

SELECT city, country FROM country LEFT JOIN city ON country.country_id = city.country_id;
SELECT city, country FROM city LEFT JOIN country ON country.country_id = city.country_id;

/* 2- customer tablosu ile payment tablosunda bulunan payment_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz RIGHT JOIN sorgusunu yazınız. */

SELECT payment.payment_id, first_name, last_name FROM customer RIGHT JOIN payment ON payment.customer_id = customer.customer_id;
SELECT payment.payment_id, first_name, last_name FROM payment RIGHT JOIN customer ON payment.customer_id = customer.customer_id;


/* 3- customer tablosu ile rental tablosunda bulunan rental_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz FULL JOIN sorgusunu yazınız. */

SELECT rental.rental_id, first_name, last_name FROM customer FULL JOIN rental ON rental.customer_id = customer.customer_id;