#!/usr/bin/env python2.7

"""
Columbia's COMS public.001 Introduction to Databases
Example Webserver

To run locally:

    python server.py

Go to http://localhost:8111 in your browser.

A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import datetime
import os

from flask import Flask, g, render_template
from flask_cors import CORS
from flask_restful import Resource, Api, request
from sqlalchemy import *

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__)
CORS(app)
api = Api(app)

#
# The following is a dummy URI that does not connect to a valid database. You will need to modify it to connect to your Part 2 database in order to use the data.
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@104.196.18.7/public
#
# For example, if you had username biliris and password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://biliris:foobar@104.196.18.7/public"
#
DBNAME = 'yelp'
DBUSER = 'w4111'
DBPASS = 'w4111'
DBPORT = '5432'
DATABASEURI = 'postgresql+psycopg2://{user}:{passwd}@localhost:{port}/{db}'.format(
    user=DBUSER,
    passwd=DBPASS,
    port=DBPORT,
    db=DBNAME)
#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)


@app.before_first_request
def init_db():
    try:
        g.conn = engine.connect()
        g.conn.execute("""
DROP SEQUENCE IF EXISTS "public"."category_cid_seq";
CREATE SEQUENCE "public"."category_cid_seq"
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 17
 CACHE 1;
SELECT setval('"public"."category_cid_seq"', 17, true);
DROP SEQUENCE IF EXISTS "public"."customer_uid_seq";
CREATE SEQUENCE "public"."customer_uid_seq"
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 22
 CACHE 1;
SELECT setval('"public"."customer_uid_seq"', 22, true);
DROP SEQUENCE IF EXISTS "public"."ingredient_iid_seq";
CREATE SEQUENCE "public"."ingredient_iid_seq"
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 12
 CACHE 1;
SELECT setval('"public"."ingredient_iid_seq"', 12, true);
DROP SEQUENCE IF EXISTS "public"."recipe_rid_seq";
CREATE SEQUENCE "public"."recipe_rid_seq"
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 48
 CACHE 1;
SELECT setval('"public"."recipe_rid_seq"', 48, true);
DROP SEQUENCE IF EXISTS "public"."restaurant_rid_seq";
CREATE SEQUENCE "public"."restaurant_rid_seq"
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 33
 CACHE 1;
SELECT setval('"public"."restaurant_rid_seq"', 33, true);
DROP SEQUENCE IF EXISTS "public"."review_rid_seq";
CREATE SEQUENCE "public"."review_rid_seq"
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 36
 CACHE 1;
SELECT setval('"public"."review_rid_seq"', 36, true);
DROP SEQUENCE IF EXISTS "public"."wishlist_wid_seq";
CREATE SEQUENCE "public"."wishlist_wid_seq"
 INCREMENT 1
 MINVALUE 1
 MAXVALUE 9223372036854775807
 START 22
 CACHE 1;
SELECT setval('"public"."wishlist_wid_seq"', 22, true);
DROP TABLE IF EXISTS "public"."category";
CREATE TABLE "public"."category" (
"cid" int4 DEFAULT nextval('category_cid_seq'::regclass) NOT NULL,
"name" char(20) COLLATE "default" NOT NULL
)
WITH (OIDS=FALSE);
INSERT INTO "public"."category" VALUES ('1', 'Pizza               ');
INSERT INTO "public"."category" VALUES ('2', 'Chinese cuisine     ');
INSERT INTO "public"."category" VALUES ('3', 'Japanese food       ');
INSERT INTO "public"."category" VALUES ('4', 'Mexican food        ');
INSERT INTO "public"."category" VALUES ('5', 'Bar&Grill           ');
INSERT INTO "public"."category" VALUES ('6', 'Caffe               ');
INSERT INTO "public"."category" VALUES ('7', 'Korean food         ');
INSERT INTO "public"."category" VALUES ('8', 'French food         ');
INSERT INTO "public"."category" VALUES ('9', 'Other               ');
DROP TABLE IF EXISTS "public"."customer";
CREATE TABLE "public"."customer" (
"uid" int4 DEFAULT nextval('customer_uid_seq'::regclass) NOT NULL,
"name" char(20) COLLATE "default" NOT NULL,
"password" char(20) COLLATE "default" NOT NULL
)
WITH (OIDS=FALSE);
INSERT INTO "public"."customer" VALUES ('1', 'Alan Xu             ', 'alan1995            ');
INSERT INTO "public"."customer" VALUES ('2', 'Grace               ', 'grace1996           ');
INSERT INTO "public"."customer" VALUES ('3', 'Anthony             ', 'anthony1996         ');
INSERT INTO "public"."customer" VALUES ('4', 'Sissel Wu           ', 'sissel1995          ');
INSERT INTO "public"."customer" VALUES ('5', 'Fever Xu            ', 'fever1996           ');
INSERT INTO "public"."customer" VALUES ('6', 'Mandi               ', 'mandi1992           ');
INSERT INTO "public"."customer" VALUES ('7', 'Krayc425            ', 'krayc425            ');
INSERT INTO "public"."customer" VALUES ('8', 'tjsoulshe           ', 'tjsoulshe           ');
INSERT INTO "public"."customer" VALUES ('12', 'rgponline           ', 's123456             ');
INSERT INTO "public"."customer" VALUES ('13', 'MengyuHAN           ', '123456              ');
INSERT INTO "public"."customer" VALUES ('14', 'MengyuHAN2          ', '123456              ');
INSERT INTO "public"."customer" VALUES ('15', 'MengyuHAN3          ', '123456              ');
INSERT INTO "public"."customer" VALUES ('16', 'Admin               ', '123456              ');
INSERT INTO "public"."customer" VALUES ('17', 'baln                ', 'alan1995            ');
INSERT INTO "public"."customer" VALUES ('18', 'MengyuHAN4          ', '123456              ');
INSERT INTO "public"."customer" VALUES ('19', 'alan                ', '123456              ');
INSERT INTO "public"."customer" VALUES ('20', 'test1               ', '123456              ');
INSERT INTO "public"."customer" VALUES ('22', '123@gmail.com       ', '123456789           ');
DROP TABLE IF EXISTS "public"."customer_preferred_category";
CREATE TABLE "public"."customer_preferred_category" (
"cid" int4 NOT NULL,
"uid" int4 NOT NULL,
"create_time" timestamp(6) NOT NULL
)
WITH (OIDS=FALSE);
INSERT INTO "public"."customer_preferred_category" VALUES ('1', '3', '2018-09-01 18:44:24');
INSERT INTO "public"."customer_preferred_category" VALUES ('2', '1', '2018-08-31 18:25:50');
INSERT INTO "public"."customer_preferred_category" VALUES ('2', '19', '2018-11-20 04:23:30');
INSERT INTO "public"."customer_preferred_category" VALUES ('2', '20', '2018-11-28 01:15:19');
INSERT INTO "public"."customer_preferred_category" VALUES ('3', '1', '2018-09-25 18:26:10');
INSERT INTO "public"."customer_preferred_category" VALUES ('5', '4', '2018-10-15 18:44:33');
INSERT INTO "public"."customer_preferred_category" VALUES ('6', '2', '2018-07-27 18:34:45');
INSERT INTO "public"."customer_preferred_category" VALUES ('6', '15', '2018-11-20 03:38:04');
INSERT INTO "public"."customer_preferred_category" VALUES ('8', '15', '2018-11-19 03:42:12');
DROP TABLE IF EXISTS "public"."customer_preferred_ingridient";
CREATE TABLE "public"."customer_preferred_ingridient" (
"uid" int4 NOT NULL,
"iid" int4 NOT NULL,
"create_time" timestamp(6) NOT NULL
)
WITH (OIDS=FALSE);
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('1', '1', '2018-10-08 18:45:34');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('1', '2', '2018-10-23 18:47:08');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('1', '3', '2018-10-23 18:47:13');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('1', '5', '2018-10-23 18:47:31');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('1', '10', '2018-11-20 02:55:52');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('2', '1', '2018-10-23 18:47:39');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('2', '4', '2018-10-23 18:47:47');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('2', '5', '2018-10-23 18:47:53');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('2', '7', '2018-10-23 18:48:01');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('2', '8', '2018-10-23 18:48:07');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('3', '1', '2018-10-23 18:48:16');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('3', '2', '2018-10-23 18:48:16');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('3', '7', '2018-10-23 18:48:16');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('3', '8', '2018-10-23 18:48:16');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('4', '2', '2018-10-23 18:48:16');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('4', '7', '2018-10-23 18:48:16');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('5', '7', '2018-10-23 18:48:16');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('6', '7', '2018-10-23 18:48:16');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('15', '7', '2018-11-20 03:38:22');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('15', '10', '2018-11-19 03:50:16');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('19', '1', '2018-11-20 04:23:39');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('19', '2', '2018-11-20 04:23:49');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('19', '3', '2018-11-20 04:23:52');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('20', '1', '2018-11-28 01:15:28');
INSERT INTO "public"."customer_preferred_ingridient" VALUES ('20', '2', '2018-11-28 01:15:32');
DROP TABLE IF EXISTS "public"."friends";
CREATE TABLE "public"."friends" (
"ruid" int4 NOT NULL,
"fuid" int4 NOT NULL,
"connected_time" timestamp(6) NOT NULL
)
WITH (OIDS=FALSE);
INSERT INTO "public"."friends" VALUES ('1', '2', '2014-09-01 00:00:00');
INSERT INTO "public"."friends" VALUES ('1', '3', '2014-11-23 00:00:00');
INSERT INTO "public"."friends" VALUES ('1', '4', '2017-02-01 00:00:00');
INSERT INTO "public"."friends" VALUES ('1', '5', '2018-11-20 03:58:54');
INSERT INTO "public"."friends" VALUES ('2', '1', '2014-09-01 00:00:00');
INSERT INTO "public"."friends" VALUES ('2', '5', '2018-06-01 00:00:00');
INSERT INTO "public"."friends" VALUES ('3', '8', '2018-09-25 00:00:00');
INSERT INTO "public"."friends" VALUES ('15', '1', '2018-11-20 03:56:41');
INSERT INTO "public"."friends" VALUES ('15', '13', '2018-11-19 05:10:35');
INSERT INTO "public"."friends" VALUES ('15', '14', '2018-11-20 03:38:59');
INSERT INTO "public"."friends" VALUES ('15', '16', '2018-11-20 04:01:18');
INSERT INTO "public"."friends" VALUES ('19', '1', '2018-11-20 04:24:42');
DROP TABLE IF EXISTS "public"."ingridient";
CREATE TABLE "public"."ingridient" (
"iid" int4 DEFAULT nextval('ingredient_iid_seq'::regclass) NOT NULL,
"name" char(20) COLLATE "default" NOT NULL
)
WITH (OIDS=FALSE);
INSERT INTO "public"."ingridient" VALUES ('1', 'beef                ');
INSERT INTO "public"."ingridient" VALUES ('2', 'pork                ');
INSERT INTO "public"."ingridient" VALUES ('3', 'chicken             ');
INSERT INTO "public"."ingridient" VALUES ('4', 'fish                ');
INSERT INTO "public"."ingridient" VALUES ('5', 'vegetable           ');
INSERT INTO "public"."ingridient" VALUES ('6', 'cheese              ');
INSERT INTO "public"."ingridient" VALUES ('7', 'coffee              ');
INSERT INTO "public"."ingridient" VALUES ('8', 'fruit               ');
INSERT INTO "public"."ingridient" VALUES ('9', 'lamb                ');
INSERT INTO "public"."ingridient" VALUES ('10', 'other               ');
INSERT INTO "public"."ingridient" VALUES ('11', 'flour               ');
DROP TABLE IF EXISTS "public"."recipe";
CREATE TABLE "public"."recipe" (
"rid" int4 DEFAULT nextval('recipe_rid_seq'::regclass) NOT NULL,
"reid" int4 NOT NULL,
"name" char(40) COLLATE "default" NOT NULL,
"price" float8 NOT NULL,
"photo_url" char(256) COLLATE "default"
)
WITH (OIDS=FALSE);
INSERT INTO "public"."recipe" VALUES ('1', '1', 'Cheese pizza                            ', '13.95', 'https://s3-media3.fl.yelpcdn.com/bphoto/mx2_vrS6G1w-W8ZpJwTboA/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('2', '1', 'Sausage Pizza                           ', '15.95', 'https://s3-media3.fl.yelpcdn.com/bphoto/DwL54BKBvoTcmhrwaF4ntA/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('3', '1', 'Salad                                   ', '7.95', 'https://s3-media1.fl.yelpcdn.com/bphoto/JZ_lYnLIIoVm9OlpMG1aBg/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('4', '1', 'Fried mozzarella                        ', '9.95', 'https://s3-media4.fl.yelpcdn.com/bphoto/-4wszGVapbrq7d2BsdaT0A/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('5', '2', 'Margherita                              ', '14', 'https://s3-media4.fl.yelpcdn.com/bphoto/YJN5ulnMKsawagXh3iyhpg/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('6', '2', 'Ceaser                                  ', '11', 'https://s3-media1.fl.yelpcdn.com/bphoto/9XW7enuiqa7A2GK-r2PQLQ/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('7', '2', 'Dessert                                 ', '12', 'https://s3-media1.fl.yelpcdn.com/bphoto/zQX_BlK8RQvyNMDxRV6ZTQ/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('8', '3', 'Cobe beef sliders                       ', '9.95', 'https://s3-media4.fl.yelpcdn.com/bphoto/obus_ufzcYoh5vQ2grQRmQ/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('9', '3', 'Chicken bowl                            ', '12', 'https://s3-media2.fl.yelpcdn.com/bphoto/BwKTHhI7ch2YbYXVvv_G2w/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('10', '4', 'An ocean of shrimps                     ', '7.95', 'https://s3-media1.fl.yelpcdn.com/bphoto/5E_H0x0HKetttht-o5KgNw/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('11', '5', 'Iced Coffee                             ', '4', 'https://globalassets.starbucks.com/assets/12be45c393e94b0e934535c905d9d44c.jpg                                                                                                                                                                                  ');
INSERT INTO "public"."recipe" VALUES ('12', '5', 'Cold Foam Cascara Nitro                 ', '5.95', 'https://globalassets.starbucks.com/assets/018fd98e15c347f3943d17b17b0e4406.jpg                                                                                                                                                                                  ');
INSERT INTO "public"."recipe" VALUES ('13', '5', 'Starbucks® Cold Brew Coffee with Milk   ', '6.59', 'https://globalassets.starbucks.com/assets/bf068e4a09d34812aed61ddc1139a57b.jpg                                                                                                                                                                                  ');
INSERT INTO "public"."recipe" VALUES ('14', '5', 'Hot Chocolate                           ', '6.59', 'https://globalassets.starbucks.com/assets/452d9229393844b9b57263a7d0d9cf1e.jpg                                                                                                                                                                                  ');
INSERT INTO "public"."recipe" VALUES ('15', '5', 'Caffè Misto                             ', '5.49', 'https://globalassets.starbucks.com/assets/60058630d5a14a679054712b6afa77c3.jpg                                                                                                                                                                                  ');
INSERT INTO "public"."recipe" VALUES ('16', '6', 'King Bao                                ', '7.99', 'https://s3-media4.fl.yelpcdn.com/bphoto/zqVRUepw0gJZl933sl9PSg/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('17', '6', 'Chicken bacon egg fried rice            ', '8.59', 'https://s3-media1.fl.yelpcdn.com/bphoto/2Q3_k14TVZ9PqXa_eUpVMA/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('18', '7', 'Beef cheese                             ', '12.59', 'https://s3-media3.fl.yelpcdn.com/bphoto/Ms7xIYlDjWK8TUOh5Y4jAQ/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('19', '7', 'Grilled shishamo                        ', '10.59', 'https://s3-media3.fl.yelpcdn.com/bphoto/BAPvWMhnTR7uynOIAHUhZg/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('20', '7', 'Salmon Sashimi Don                      ', '14.59', 'https://s3-media4.fl.yelpcdn.com/bphoto/P8B-NaaItDyXCKVCIGF3jQ/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('21', '7', 'California Roll                         ', '13.05', 'https://s3-media3.fl.yelpcdn.com/bphoto/NE-hiFaAjZKW0uF9gifWJQ/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('22', '8', 'Fish and chips                          ', '7.99', 'https://s3-media4.fl.yelpcdn.com/bphoto/LM2h9KzazrNYNj0r97zc5w/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('23', '9', 'Endive salad                            ', '20', 'https://s3-media4.fl.yelpcdn.com/bphoto/-mq5dTyh_iKEjYvcvRaXMA/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('24', '9', 'Celery puree                            ', '15.95', 'https://s3-media4.fl.yelpcdn.com/bphoto/dOepHhWxIzSVBCYwv391Bg/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('25', '9', 'Rack of lamb                            ', '25.95', 'https://s3-media1.fl.yelpcdn.com/bphoto/G05sVHQ4X6QEddiKq8Pd1A/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('26', '10', 'Vegatable soup                          ', '6.95', 'https://s3-media1.fl.yelpcdn.com/bphoto/iMDdsjbzw1sxh-B9TRIajA/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('27', '10', 'Fish and rice                           ', '8.95', 'https://s3-media2.fl.yelpcdn.com/bphoto/9Ga8yw4QUh8rimzKE41Qlw/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('28', '11', 'Fries                                   ', '5.95', 'https://s3-media3.fl.yelpcdn.com/bphoto/4Mrrx7PWhOEP5T5jhby4ng/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('29', '11', 'Chicken wings                           ', '9.55', 'https://s3-media2.fl.yelpcdn.com/bphoto/jjVQMLpnf_t1QJNpfG1DbQ/o.jpg                                                                                                                                                                                            ');
INSERT INTO "public"."recipe" VALUES ('47', '33', 'recipe1                                 ', '19', 'https://images.unsplash.com/photo-1532980400857-e8d9d275d858?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=5b501bf3957585b28199e54ec4700806&auto=format&fit=crop&w=634&q=80                                                                                        ');
DROP TABLE IF EXISTS "public"."recipe_ingridient";
CREATE TABLE "public"."recipe_ingridient" (
"rid" int4 NOT NULL,
"iid" int4 NOT NULL
)
WITH (OIDS=FALSE);
INSERT INTO "public"."recipe_ingridient" VALUES ('1', '6');
INSERT INTO "public"."recipe_ingridient" VALUES ('1', '11');
INSERT INTO "public"."recipe_ingridient" VALUES ('2', '2');
INSERT INTO "public"."recipe_ingridient" VALUES ('2', '11');
INSERT INTO "public"."recipe_ingridient" VALUES ('3', '5');
INSERT INTO "public"."recipe_ingridient" VALUES ('3', '8');
INSERT INTO "public"."recipe_ingridient" VALUES ('4', '3');
INSERT INTO "public"."recipe_ingridient" VALUES ('5', '6');
INSERT INTO "public"."recipe_ingridient" VALUES ('5', '11');
INSERT INTO "public"."recipe_ingridient" VALUES ('6', '5');
INSERT INTO "public"."recipe_ingridient" VALUES ('7', '11');
INSERT INTO "public"."recipe_ingridient" VALUES ('8', '1');
INSERT INTO "public"."recipe_ingridient" VALUES ('9', '3');
INSERT INTO "public"."recipe_ingridient" VALUES ('9', '5');
INSERT INTO "public"."recipe_ingridient" VALUES ('10', '10');
INSERT INTO "public"."recipe_ingridient" VALUES ('10', '11');
INSERT INTO "public"."recipe_ingridient" VALUES ('11', '7');
INSERT INTO "public"."recipe_ingridient" VALUES ('12', '7');
INSERT INTO "public"."recipe_ingridient" VALUES ('13', '7');
INSERT INTO "public"."recipe_ingridient" VALUES ('14', '7');
INSERT INTO "public"."recipe_ingridient" VALUES ('15', '7');
INSERT INTO "public"."recipe_ingridient" VALUES ('16', '2');
INSERT INTO "public"."recipe_ingridient" VALUES ('17', '3');
INSERT INTO "public"."recipe_ingridient" VALUES ('17', '5');
INSERT INTO "public"."recipe_ingridient" VALUES ('18', '1');
INSERT INTO "public"."recipe_ingridient" VALUES ('18', '6');
INSERT INTO "public"."recipe_ingridient" VALUES ('19', '10');
INSERT INTO "public"."recipe_ingridient" VALUES ('20', '10');
INSERT INTO "public"."recipe_ingridient" VALUES ('21', '10');
INSERT INTO "public"."recipe_ingridient" VALUES ('22', '4');
INSERT INTO "public"."recipe_ingridient" VALUES ('22', '11');
INSERT INTO "public"."recipe_ingridient" VALUES ('23', '5');
INSERT INTO "public"."recipe_ingridient" VALUES ('23', '8');
INSERT INTO "public"."recipe_ingridient" VALUES ('24', '3');
INSERT INTO "public"."recipe_ingridient" VALUES ('24', '5');
INSERT INTO "public"."recipe_ingridient" VALUES ('25', '9');
INSERT INTO "public"."recipe_ingridient" VALUES ('26', '5');
INSERT INTO "public"."recipe_ingridient" VALUES ('27', '4');
INSERT INTO "public"."recipe_ingridient" VALUES ('47', '1');
INSERT INTO "public"."recipe_ingridient" VALUES ('47', '2');
DROP TABLE IF EXISTS "public"."restaurant";
CREATE TABLE "public"."restaurant" (
"rid" int4 DEFAULT nextval('restaurant_rid_seq'::regclass) NOT NULL,
"cid" int4,
"name" char(40) COLLATE "default" NOT NULL,
"contact" char(20) COLLATE "default",
"location" char(128) COLLATE "default" NOT NULL,
"star" float8,
"photo_url" char(256) COLLATE "default",
"longitude" float8 NOT NULL,
"latitude" float8 NOT NULL
)
WITH (OIDS=FALSE);
INSERT INTO "public"."restaurant" VALUES ('1', '1', 'Metro Pizza House                       ', '(702) 486-4368      ', '5757 Wayne Newton Blvd                                                                                                          ', '3.125', 'https://s3-media1.fl.yelpcdn.com/bphoto/aAoUthFqsND23zdy1sZftw/o.jpg                                                                                                                                                                                            ', '-115.1391027', '36.0808997');
INSERT INTO "public"."restaurant" VALUES ('2', '6', 'Buddy V''s Ristorante E Caffe            ', '(702) 424-5786      ', '3930 Las Vegas Blvd S                                                                                                           ', '3.5', 'https://s3-media4.fl.yelpcdn.com/bphoto/tpzXs9AmhxeZj7CcI2ZFRA/o.jpg                                                                                                                                                                                            ', '-115.138026', '36.089494');
INSERT INTO "public"."restaurant" VALUES ('3', '5', 'Dragon Grille                           ', '(702) 435-8677      ', '6605 S Las Vegas Blvd                                                                                                           ', '4', 'https://s3-media4.fl.yelpcdn.com/bphoto/cKJ8u-oxytSVK3h7Uy7TDw/o.jpg                                                                                                                                                                                            ', '-115.1533426', '36.0765176');
INSERT INTO "public"."restaurant" VALUES ('4', '4', 'El Cachi Mexican Kitchen                ', '(702) 424-5777      ', '5030 Paradise Rd, Ste 110                                                                                                       ', '5', 'https://s3-media2.fl.yelpcdn.com/bphoto/uLi_neOc1mXpb7n9FneA5g/o.jpg                                                                                                                                                                                            ', '-115.148393846', '36.0977842437');
INSERT INTO "public"."restaurant" VALUES ('5', '6', 'Starbucks                               ', '(702) 433-2742      ', '5757 Paradise Rd                                                                                                                ', '4.16666666666667', 'https://s3-media2.fl.yelpcdn.com/bphoto/LNyfn8r63O4SXRWKAMj43w/o.jpg                                                                                                                                                                                            ', '-115.149700818', '36.0854594139');
INSERT INTO "public"."restaurant" VALUES ('6', '4', 'Pei Wei Asian Restaurant                ', '(702) 455-1057      ', '1198 Sir Patrick Ave                                                                                                            ', '3.83333333333333', 'https://s3-media3.fl.yelpcdn.com/bphoto/DYZxQfWGXRlDFbjQSHE9Zw/o.jpg                                                                                                                                                                                            ', '-115.147215269', '36.0811202017');
INSERT INTO "public"."restaurant" VALUES ('7', '3', 'Kyara Sushi                             ', '(702) 432-1038      ', '1224 Sir Patrick Ave                                                                                                            ', '4.33333333333333', 'https://s3-media1.fl.yelpcdn.com/bphoto/otSQXw8lQHOAARgo8-5RFw/o.jpg                                                                                                                                                                                            ', '-115.147665797', '36.0819322382');
INSERT INTO "public"."restaurant" VALUES ('8', '5', 'Village Pub and Grill                   ', '(702) 413-4869      ', '5757 Wayne Newton Dr                                                                                                            ', '3.5', 'https://s3-media3.fl.yelpcdn.com/bphoto/nxEd6xNvyGd2YYZPjxYvPg/o.jpg                                                                                                                                                                                            ', '-115.149927', '36.0854286');
INSERT INTO "public"."restaurant" VALUES ('9', '8', 'Ohlala                                  ', '(702) 455-3921      ', '115 E Tropicana Ave                                                                                                             ', '4.5', 'https://s3-media4.fl.yelpcdn.com/bphoto/jwCLmIWdULR0pRUG-tGt3w/o.jpg                                                                                                                                                                                            ', '-115.167874', '36.0993459');
INSERT INTO "public"."restaurant" VALUES ('10', '9', 'Nigerian Cuisine                        ', '(702) 422-8754      ', '5006 S Maryland Pkwy, Ste 11                                                                                                    ', '3', 'https://s3-media4.fl.yelpcdn.com/bphoto/p76lLampwMQ6ldQEJbkv8w/o.jpg                                                                                                                                                                                            ', '-115.1360641', '36.0986458');
INSERT INTO "public"."restaurant" VALUES ('11', '7', 'Koko Wings                              ', '(702) 466-3827      ', '5292 S Maryland Pkwy                                                                                                            ', '4.5', 'https://s3-media1.fl.yelpcdn.com/bphoto/zHvgDey8rghLDEVOFq30JQ/o.jpg                                                                                                                                                                                            ', '-115.135686', '36.095007');
INSERT INTO "public"."restaurant" VALUES ('33', '5', 'Relax                                   ', '1                   ', 'test location                                                                                                                   ', '0', 'https://images.unsplash.com/photo-1481833761820-0509d3217039?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=3fb6b264e88b8819ae92aa44494eca81&auto=format&fit=crop&w=1050&q=80                                                                                       ', '-0.1', '0.1');
DROP TABLE IF EXISTS "public"."review";
CREATE TABLE "public"."review" (
"rid" int4 DEFAULT nextval('review_rid_seq'::regclass) NOT NULL,
"reid" int4 NOT NULL,
"uid" int4 NOT NULL,
"content" char(1024) COLLATE "default" NOT NULL,
"star" float8 NOT NULL,
"create_time" timestamp(6) NOT NULL
)
WITH (OIDS=FALSE);
INSERT INTO "public"."review" VALUES ('1', '3', '1', 'THEY HAVE EXTRAORDINARY BEEF SLIDERS! pick Kobe beef, that''s really surprising.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ', '5', '2018-09-24 18:58:58');
INSERT INTO "public"."review" VALUES ('2', '3', '2', 'The beef is fairly good but there''s no service at all and the environment there is not ok as well.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ', '3', '2018-10-17 19:01:28');
INSERT INTO "public"."review" VALUES ('3', '1', '6', 'pizza is poor and the only food I''m satisfied with is the bottled water                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ', '2.5', '2018-10-09 19:04:11');
INSERT INTO "public"."review" VALUES ('4', '2', '7', 'Margherita is great, suitable for family dining                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ', '3.5', '2018-10-05 19:06:44');
INSERT INTO "public"."review" VALUES ('5', '4', '3', 'I''ve never had such great shrimp before! The menu calls it an ocean of shrimps and they sincerely put in so many fresh shrimps.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ', '5', '2018-10-03 19:09:20');
INSERT INTO "public"."review" VALUES ('6', '4', '8', 'Vote for an ocean of shrimps!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ', '5', '2018-09-24 19:09:45');
INSERT INTO "public"."review" VALUES ('7', '5', '5', 'Too crowded! And the service is quite slow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ', '3.5', '2018-10-04 19:10:11');
INSERT INTO "public"."review" VALUES ('8', '6', '4', 'Cheap and convenient for lunch but I think they''re a little bit unhealthy for I saw them grab vegatables and cashes using bare hands without cleaning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ', '2.5', '2018-08-15 19:12:40');
INSERT INTO "public"."review" VALUES ('9', '7', '4', 'Really authetic japanese cuisine and I will come back for their california rolls.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ', '4', '2018-10-09 19:14:44');
INSERT INTO "public"."review" VALUES ('10', '9', '1', 'So outstanding and expensive! What I learned from them is better food is worth of better price.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ', '4.5', '2018-10-10 19:18:09');
INSERT INTO "public"."review" VALUES ('11', '11', '2', 'not so authetic but the chicken wings are tasty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ', '4', '2018-10-23 19:19:15');
INSERT INTO "public"."review" VALUES ('20', '4', '15', 'Very Nice restaurant, and I enjoy eating at this place a lot.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ', '4.5', '2018-11-19 04:50:44');
INSERT INTO "public"."review" VALUES ('26', '11', '2', 'Pretty'' good chicken wings!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ', '5', '2018-11-19 14:04:55');
INSERT INTO "public"."review" VALUES ('29', '7', '1', 'Hello Kyara Sushi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ', '4', '2018-11-20 03:00:06');
INSERT INTO "public"."review" VALUES ('30', '7', '1', 'High star for this authentic one!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               ', '5', '2018-11-20 03:00:38');
INSERT INTO "public"."review" VALUES ('31', '6', '15', 'Like this restaurant!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ', '4', '2018-11-20 03:42:58');
INSERT INTO "public"."review" VALUES ('32', '5', '15', 'Like their coffee!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ', '4', '2018-11-20 03:50:12');
INSERT INTO "public"."review" VALUES ('33', '5', '15', 'Great Place to Study                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ', '5', '2018-11-20 03:52:04');
INSERT INTO "public"."review" VALUES ('34', '6', '19', 'I like its food so much! it brings me back to my hometown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ', '5', '2018-11-20 04:25:30');
INSERT INTO "public"."review" VALUES ('35', '1', '20', 'pretty bad                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ', '1', '2018-11-28 01:13:32');
INSERT INTO "public"."review" VALUES ('36', '1', '20', 'pretty good                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ', '5', '2018-11-28 01:14:15');
DROP TABLE IF EXISTS "public"."wishlist";
CREATE TABLE "public"."wishlist" (
"wid" int4 DEFAULT nextval('wishlist_wid_seq'::regclass) NOT NULL,
"uid" int4 NOT NULL,
"name" char(20) COLLATE "default" NOT NULL,
"create_time" timestamp(6) NOT NULL
)
WITH (OIDS=FALSE);
INSERT INTO "public"."wishlist" VALUES ('1', '2', 'Coffee collection   ', '2018-10-23 18:52:07');
INSERT INTO "public"."wishlist" VALUES ('2', '1', 'Meat seeker         ', '2018-10-23 18:55:51');
INSERT INTO "public"."wishlist" VALUES ('4', '15', 'default wishlist    ', '2018-11-18 21:53:12');
INSERT INTO "public"."wishlist" VALUES ('5', '16', 'default wishlist    ', '2018-11-18 22:50:47');
INSERT INTO "public"."wishlist" VALUES ('7', '15', 'FirstCustomeWishlist', '2018-11-19 04:31:02');
INSERT INTO "public"."wishlist" VALUES ('8', '15', 'SecondList          ', '2018-11-19 04:32:27');
INSERT INTO "public"."wishlist" VALUES ('9', '15', 'ThirdList           ', '2018-11-19 04:32:40');
INSERT INTO "public"."wishlist" VALUES ('13', '15', 'My first try        ', '2018-11-19 04:55:19');
INSERT INTO "public"."wishlist" VALUES ('14', '17', 'default wishlist    ', '2018-11-19 13:51:28');
INSERT INTO "public"."wishlist" VALUES ('15', '18', 'default wishlist    ', '2018-11-20 02:45:36');
INSERT INTO "public"."wishlist" VALUES ('16', '1', 'Test                ', '2018-11-20 02:54:51');
INSERT INTO "public"."wishlist" VALUES ('17', '15', 'Restaurants Nearby  ', '2018-11-20 03:38:37');
INSERT INTO "public"."wishlist" VALUES ('20', '19', 'test                ', '2018-11-20 04:24:35');
INSERT INTO "public"."wishlist" VALUES ('21', '20', 'default wishlist    ', '2018-11-28 01:10:23');
INSERT INTO "public"."wishlist" VALUES ('22', '22', 'default wishlist    ', '2018-11-28 03:37:45');
DROP TABLE IF EXISTS "public"."wishlist_restaurant";
CREATE TABLE "public"."wishlist_restaurant" (
"wid" int4 NOT NULL,
"rid" int4 NOT NULL
)
WITH (OIDS=FALSE);
INSERT INTO "public"."wishlist_restaurant" VALUES ('1', '5');
INSERT INTO "public"."wishlist_restaurant" VALUES ('1', '6');
INSERT INTO "public"."wishlist_restaurant" VALUES ('2', '2');
INSERT INTO "public"."wishlist_restaurant" VALUES ('2', '6');
INSERT INTO "public"."wishlist_restaurant" VALUES ('2', '7');
INSERT INTO "public"."wishlist_restaurant" VALUES ('2', '11');
INSERT INTO "public"."wishlist_restaurant" VALUES ('7', '4');
INSERT INTO "public"."wishlist_restaurant" VALUES ('7', '6');
INSERT INTO "public"."wishlist_restaurant" VALUES ('8', '5');
INSERT INTO "public"."wishlist_restaurant" VALUES ('8', '6');
INSERT INTO "public"."wishlist_restaurant" VALUES ('9', '3');
INSERT INTO "public"."wishlist_restaurant" VALUES ('9', '6');
INSERT INTO "public"."wishlist_restaurant" VALUES ('13', '6');
INSERT INTO "public"."wishlist_restaurant" VALUES ('20', '6');
INSERT INTO "public"."wishlist_restaurant" VALUES ('21', '1');
ALTER TABLE "public"."category" ADD PRIMARY KEY ("cid");
ALTER TABLE "public"."customer" ADD UNIQUE ("name");
ALTER TABLE "public"."customer" ADD CHECK (((length(name) >= 1) AND (length(password) >= 6)));
ALTER TABLE "public"."customer" ADD PRIMARY KEY ("uid");
ALTER TABLE "public"."customer_preferred_category" ADD PRIMARY KEY ("cid", "uid");
ALTER TABLE "public"."customer_preferred_ingridient" ADD PRIMARY KEY ("uid", "iid");
ALTER TABLE "public"."friends" ADD CHECK ((ruid <> fuid));
ALTER TABLE "public"."friends" ADD PRIMARY KEY ("ruid", "fuid");
ALTER TABLE "public"."ingridient" ADD PRIMARY KEY ("iid");
ALTER TABLE "public"."recipe" ADD CHECK ((price >= (0)::double precision));
ALTER TABLE "public"."recipe" ADD PRIMARY KEY ("rid");
ALTER TABLE "public"."recipe_ingridient" ADD PRIMARY KEY ("rid", "iid");
ALTER TABLE "public"."restaurant" ADD CHECK (((star <= (5)::double precision) AND (star >= (0)::double precision)));
ALTER TABLE "public"."restaurant" ADD CHECK (((latitude >= ((-90))::double precision) AND (latitude <= (90)::double precision)));
ALTER TABLE "public"."restaurant" ADD CHECK (((longitude >= ((-180))::double precision) AND (longitude <= (180)::double precision)));
ALTER TABLE "public"."restaurant" ADD PRIMARY KEY ("rid");
ALTER TABLE "public"."review" ADD CHECK (((star <= (5)::double precision) AND (star >= (0)::double precision)));
ALTER TABLE "public"."review" ADD PRIMARY KEY ("rid");
ALTER TABLE "public"."wishlist" ADD PRIMARY KEY ("wid");
ALTER TABLE "public"."wishlist_restaurant" ADD PRIMARY KEY ("wid", "rid");
ALTER TABLE "public"."customer_preferred_category" ADD FOREIGN KEY ("cid") REFERENCES "public"."category" ("cid") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."customer_preferred_category" ADD FOREIGN KEY ("uid") REFERENCES "public"."customer" ("uid") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."customer_preferred_ingridient" ADD FOREIGN KEY ("uid") REFERENCES "public"."customer" ("uid") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."customer_preferred_ingridient" ADD FOREIGN KEY ("iid") REFERENCES "public"."ingridient" ("iid") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."friends" ADD FOREIGN KEY ("ruid") REFERENCES "public"."customer" ("uid") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."friends" ADD FOREIGN KEY ("fuid") REFERENCES "public"."customer" ("uid") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."recipe" ADD FOREIGN KEY ("reid") REFERENCES "public"."restaurant" ("rid") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."recipe_ingridient" ADD FOREIGN KEY ("rid") REFERENCES "public"."recipe" ("rid") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."recipe_ingridient" ADD FOREIGN KEY ("iid") REFERENCES "public"."ingridient" ("iid") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."restaurant" ADD FOREIGN KEY ("cid") REFERENCES "public"."category" ("cid") ON DELETE SET NULL ON UPDATE NO ACTION;
ALTER TABLE "public"."review" ADD FOREIGN KEY ("reid") REFERENCES "public"."restaurant" ("rid") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."review" ADD FOREIGN KEY ("uid") REFERENCES "public"."customer" ("uid") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."wishlist" ADD FOREIGN KEY ("uid") REFERENCES "public"."customer" ("uid") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."wishlist_restaurant" ADD FOREIGN KEY ("rid") REFERENCES "public"."restaurant" ("rid") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "public"."wishlist_restaurant" ADD FOREIGN KEY ("wid") REFERENCES "public"."wishlist" ("wid") ON DELETE CASCADE ON UPDATE NO ACTION;
""")
    except:
        print("uh oh, problem connecting to database")
        import traceback
        traceback.print_exc()
        g.conn = None


@app.before_request
def before_request():
    """
    This function is run at the beginning of every web request
    (every time you enter an address in the web browser).
    We use it to setup a database connection that can be used throughout the request.

    The variable g is globally accessible.
    """
    try:
        g.conn = engine.connect()
    except:
        print("uh oh, problem connecting to database")
        import traceback
        traceback.print_exc()
        g.conn = None


@app.route('/')
def index():
    return render_template('index.html')


class Category(Resource):
    def get(self):
        cursor = g.conn.execute("SELECT * FROM category")
        data = []
        for result in cursor:
            data.append({
                "cid": result["cid"],
                "name": result["name"].strip()
            })
        cursor.close()
        return data

    def post(self):
        data = request.json
        cursor = g.conn.execute("SELECT name FROM category")
        for result in cursor:
            if result['name'].strip() == data['name']:
                cursor.close()
                return False
        cursor.close()
        g.conn.execute("INSERT INTO category(name) VALUES (%s)", data['name'])
        return True

    def delete(self):
        data = request.json
        g.conn.execute("DELETE FROM category WHERE cid=%s", data['cid'])
        return True


class RestaurantList(Resource):
    def get(self):
        cursor = g.conn.execute(
            "SELECT rid,c.cid as cid,c.name as cname,r.name as name,contact,location,star,photo_url,longitude,latitude FROM restaurant r, category c where r.cid=c.cid")
        data = []
        for result in cursor:
            data.append({
                "rid": result["rid"],
                "cid": result["cid"],
                "name": result["name"].strip(),
                "cname": result["cname"].strip(),
                "contact": result["contact"].strip(),
                "location": result["location"].strip(),
                "star": round(result["star"], 2),
                "photo_url": result["photo_url"].strip(),
                "longitude": result["longitude"],
                "latitude": result["latitude"]
            })
        cursor.close()
        return data

    def post(self):
        data = request.json
        cid = data["cid"]
        name = data["name"]
        contact = data["contact"]
        star = 0
        photo_url = data["photo_url"]
        location = data["location"]
        longitude = data["longitude"]
        latitude = data["latitude"]
        g.conn.execute(
            "INSERT INTO restaurant(cid, name, contact, star, location, photo_url, longitude, latitude) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
            (cid, name, contact, star, location, photo_url, longitude, latitude)
        )
        return True


class Restaurant(Resource):
    def get(self, rid):
        cursor = g.conn.execute(
            "SELECT rid,c.cid as cid,c.name as cname,r.name as name,contact,location,star,photo_url,longitude,latitude FROM restaurant r, category c where r.cid=c.cid and r.rid=" + rid)
        data = {}
        for result in cursor:
            data = {
                "rid": result["rid"],
                "cid": result["cid"],
                "name": result["name"].strip(),
                "cname": result["cname"].strip(),
                "contact": result["contact"].strip(),
                "location": result["location"].strip(),
                "star": round(result["star"], 2),
                "photo_url": result["photo_url"].strip(),
                "longitude": result["longitude"],
                "latitude": result["latitude"]
            }
        cursor.close()
        return data

    def put(self, rid):
        data = request.json
        cid = data['cid']
        name = data['name']
        contact = data["contact"]
        photo_url = data["photo_url"]
        location = data["location"]
        longitude = data["longitude"]
        latitude = data["latitude"]
        g.conn.execute(
            "UPDATE restaurant SET name = %s,cid = %s,contact = %s,location = %s,photo_url = %s,longitude = %s,latitude = %s WHERE rid=%s",
            name, cid, contact, location, photo_url, longitude, latitude, rid
        )
        return True

    def delete(self, rid):
        g.conn.execute("DELETE FROM restaurant WHERE rid=%s", rid)
        return True


class Recipe(Resource):
    def get(self, rid):
        cursor = g.conn.execute("SELECT rid,reid,name,price,photo_url FROM recipe WHERE reid=%s", rid)
        data = []
        for result in cursor:
            recipe_id = result["rid"]
            ingredients = []
            in_cursor = g.conn.execute(
                "SELECT i.iid as iid,name FROM recipe_ingridient ri, ingridient i WHERE ri.iid=i.iid AND ri.rid=%s",
                recipe_id)
            for in_result in in_cursor:
                ingredients.append({
                    "iid": in_result["iid"],
                    "name": in_result["name"].strip()
                })
            data.append({
                "rid": result["rid"],
                "reid": result["reid"],
                "name": result["name"].strip(),
                "price": round(result["price"], 2),
                "photo_url": result["photo_url"].strip(),
                "ingredients": ingredients
            })
        cursor.close()
        return data

    def post(self, rid):
        data = request.json
        name = data['name']
        price = data['price']
        photo_url = data['photo_url']
        ingredients = data['ingredients']
        g.conn.execute(
            "INSERT INTO recipe(reid, name, price, photo_url) VALUES (%s,%s,%s,%s)",
            (rid, name, price, photo_url)
        )
        cursor = g.conn.execute("SELECT rid FROM recipe WHERE reid=%s AND name=%s", (rid, name))
        recipe_id = -1
        for result in cursor:
            recipe_id = result['rid']
        for ingredient in ingredients:
            g.conn.execute("INSERT INTO recipe_ingridient(rid, iid) VALUES(%s,%s)", (recipe_id, ingredient['iid']))
        cursor.close()
        return True

    def delete(self, rid):
        data = request.json
        recipe_id = str(data['rid'])
        g.conn.execute("DELETE FROM recipe WHERE rid=%s", recipe_id)
        return True


class Ingredient(Resource):
    def get(self):
        cursor = g.conn.execute("SELECT * FROM ingridient")
        data = []
        for result in cursor:
            data.append({
                "iid": result["iid"],
                "name": result["name"].strip()
            })
        cursor.close()
        return data

    def post(self):
        data = request.json
        cursor = g.conn.execute("SELECT name FROM ingridient")
        for result in cursor:
            if data['name'] == result['name'].strip():
                cursor.close()
                return False
        cursor.close()
        g.conn.execute("INSERT INTO ingridient(name) VALUES (%s)", data['name'])
        return True

    def delete(self):
        data = request.json
        g.conn.execute("DELETE FROM ingridient WHERE iid=%s", data['iid'])
        return True


class Login(Resource):
    def post(self):
        data = request.json
        name = data["username"]
        password = data["password"]
        cursor = g.conn.execute("SELECT * FROM customer WHERE name=%s", name)
        res = {"msg": "", "status": True}
        empty = True
        user = {}
        for result in cursor:
            empty = False
            user = result

        if empty:
            res["status"] = False
            res["msg"] = "user not found"
        else:
            print(user)
            if password != user["password"].rstrip():
                res["status"] = False
                res["msg"] = "password mismatch"
            else:
                res["uid"] = user["uid"]
        cursor.close()
        return res


class Register(Resource):
    def post(self):
        data = request.json
        name = data["username"]
        password = data["password"]
        cursor = g.conn.execute("SELECT * FROM customer WHERE name=%s", name)
        res = {"msg": "", "status": True}
        empty = True
        for result in cursor:
            empty = False
        if not empty:
            res["status"] = False
            res["msg"] = "repeated user name, please change another one"
        else:
            g.conn.execute("INSERT INTO customer(name, password) VALUES(%s,%s)", (name, password))
            u_cursor = g.conn.execute("SELECT uid FROM customer WHERE name=%s", name)
            for result in u_cursor:
                res["uid"] = result['uid']
            u_cursor.close()
            # add default wishlist
            name = "default wishlist"
            create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            g.conn.execute(
                "INSERT INTO wishlist(uid, name, create_time) VALUES(%s,%s,%s)", (res["uid"], name, create_time))
        cursor.close()
        return res


class Friend(Resource):
    def get(self, uid):
        cursor = g.conn.execute("SELECT * FROM friends WHERE ruid=%s", uid)
        data = []
        for result in cursor:
            fuid = result["fuid"]
            f_cursor = g.conn.execute("SELECT * FROM customer WHERE uid=%s", fuid)
            friend = {}
            for f_result in f_cursor:
                friend = f_result
            data.append({
                "uid": fuid,
                "uname": friend["name"].strip(),
                "connected_time": str(result["connected_time"])
            })
        return data

    def post(self, uid):
        data = request.json
        name = data["uname_friend"]
        cursor = g.conn.execute("SELECT * FROM customer WHERE name=%s", name)
        friend = {}
        for result in cursor:
            friend = result

        fuid = friend["uid"]
        connected_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        g.conn.execute("INSERT INTO friends(ruid, fuid, connected_time) VALUES (%s,%s,%s)", (uid, fuid, connected_time))
        return True

    def delete(self, uid):
        data = request.json
        fuid = data["uid_friend"]
        g.conn.execute("DELETE FROM friends WHERE ruid=%s AND fuid=%s", (uid, fuid))
        return True


class Review(Resource):
    def get(self, rid):
        cursor = g.conn.execute("SELECT * from review where reid=%s", rid)
        data = []
        for result in cursor:
            data.append({
                "rid": result["rid"],
                "reid": result["reid"],
                "uid": result["uid"],
                "content": result["content"].strip(),
                "star": round(result["star"], 2),
                "create_time": str(result["create_time"])
            })
        cursor.close()
        return data

    def post(self, rid):
        data = request.json
        uid = data["uid"]
        content = data["content"]
        star = data["star"]
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        g.conn.execute(
            "INSERT INTO review (reid, uid, content, star, create_time) VALUES (%s,%s,%s,%s,%s)",
            (rid, uid, content, star, create_time)
        )

        # update average star of restaurant
        cursor = g.conn.execute("SELECT star FROM review WHERE reid=%s", rid)
        total_star = 0.0
        total_cnt = 0
        for result in cursor:
            total_cnt += 1
            total_star += result['star']
        ave_star = total_star / total_cnt
        cursor.close()
        g.conn.execute("UPDATE restaurant SET star = %s WHERE rid=%s", (ave_star, rid))

        return True


class ReviewRecord(Resource):
    def get(self, uid):
        cursor = g.conn.execute(
            "SELECT re.rid as rid,r.rid as reid, name as rname,uid,content,r.star as star,create_time FROM review r, restaurant re WHERE r.reid=re.rid AND uid=%s",
            uid)
        data = []
        for result in cursor:
            data.append({
                "rid": result["rid"],
                "reid": result["reid"],
                "rname": result["rname"].strip(),
                "uid": result["uid"],
                "content": result["content"].strip(),
                "star": round(result["star"], 2),
                "create_time": str(result["create_time"])
            })
        cursor.close()
        return data

    def delete(self, uid):
        data = request.json
        rid = data["reid"]
        g.conn.execute("DELETE FROM review WHERE rid=%s AND uid=%s", (rid, uid))
        return True


class WishList(Resource):
    def post(self):
        data = request.json
        uid = data["uid"]
        name = data["name"]
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        g.conn.execute(
            "INSERT INTO wishlist(uid, name, create_time) VALUES(%s,%s,%s)", (uid, name, create_time))
        return True

    def delete(self):
        data = request.json
        uid = data["uid"]
        wid = data["wid"]
        g.conn.execute("DELETE FROM wishlist WHERE wid=%s AND uid=%s", (wid, uid))
        return True


class UserWishList(Resource):
    def get(self, uid):
        w_cursor = g.conn.execute("SELECT * FROM wishlist w WHERE w.uid=%s", uid)
        data = []
        for w_result in w_cursor:
            wid = w_result["wid"]
            wr_cursor = g.conn.execute("SELECT * FROM wishlist_restaurant wr WHERE wr.wid=%s", wid)
            restaurants = []
            for wr_result in wr_cursor:
                re_cursor = g.conn.execute("SELECT * FROM restaurant WHERE rid=%s", wr_result['rid'])
                for re_result in re_cursor:
                    restaurants.append({
                        "rid": re_result["rid"],
                        "name": re_result["name"].strip()
                    })
                re_cursor.close()
            data.append({
                "wid": w_result["wid"],
                "name": w_result["name"].strip(),
                "create_time": str(w_result["create_time"]),
                "restaurants": restaurants
            })
            wr_cursor.close()
        w_cursor.close()
        return data

    def post(self, uid):
        data = request.json
        wid = data["wid"]
        rid = data["rid"]
        g.conn.execute("INSERT INTO wishlist_restaurant (wid, rid) VALUES (%s,%s)", (wid, rid))
        return True

    def delete(self, uid):
        data = request.json
        wid = str(data["wid"])
        rid = str(data["rid"])
        g.conn.execute("DELETE FROM wishlist_restaurant WHERE wid=%s AND rid=%s;", (wid, rid))
        return True


class FavoriteCategory(Resource):
    def get(self, uid):
        cursor = g.conn.execute(
            "SELECT * from customer_preferred_category cpc,category c where cpc.cid=c.cid and cpc.uid=%s", uid)
        data = []
        for result in cursor:
            data.append({
                "cid": result["cid"],
                "name": result["name"].strip(),
                "create_time": str(result["create_time"])
            })
        cursor.close()
        return data

    def post(self, uid):
        data = request.json
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cid = data["cid"]
        empty = True
        cursor = g.conn.execute("SELECT * FROM customer_preferred_category WHERE uid=%s AND cid=%s", (uid, cid))
        for result in cursor:
            empty = False
        cursor.close()
        if empty:
            g.conn.execute(
                "INSERT INTO customer_preferred_category (cid, uid, create_time) VALUES (%s,%s,%s)",
                (cid, uid, create_time)
            )
            return True
        else:
            return False

    def delete(self, uid):
        data = request.json
        cid = data["cid"]
        g.conn.execute("DELETE FROM customer_preferred_category WHERE cid=%s AND uid=%s", (cid, uid))
        return True


class FavoriteIngredient(Resource):
    def get(self, uid):
        cursor = g.conn.execute(
            "SELECT cpi.iid as iid,name,create_time from customer_preferred_ingridient cpi,ingridient i where cpi.iid=i.iid and cpi.uid=%s",
            uid)
        data = []
        for result in cursor:
            data.append({
                "iid": result["iid"],
                "name": result["name"].strip(),
                "create_time": str(result["create_time"])
            })
        cursor.close()
        return data

    def post(self, uid):
        data = request.json
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        iid = data["iid"]
        empty = True
        cursor = g.conn.execute("SELECT * FROM customer_preferred_ingridient WHERE uid=%s AND iid=%s", (uid, iid))
        for result in cursor:
            empty = False
        cursor.close()
        if empty:
            g.conn.execute(
                "INSERT INTO customer_preferred_ingridient (iid, uid, create_time) VALUES (%s,%s,%s)",
                (iid, uid, create_time))
            return True
        else:
            return False

    def delete(self, uid):
        data = request.json
        iid = data["iid"]
        g.conn.execute("DELETE FROM customer_preferred_ingridient WHERE iid=%s AND uid=%s", (iid, uid))
        return True


class Recommendation(Resource):
    def get(self, uid):
        cursor = g.conn.execute(
            "(SELECT DISTINCT cpc.uid, re.rid FROM customer_preferred_category cpc JOIN restaurant re ON cpc.cid = re.cid AND cpc.uid = " + uid + ") INTERSECT (SELECT DISTINCT cpi.uid, r.reid AS rid FROM customer_preferred_ingridient cpi JOIN recipe_ingridient ri ON cpi.iid = ri.iid AND cpi.uid = " + uid + " JOIN recipe r ON r.rid = ri.rid)")
        data = []
        for result in cursor:
            rid = result["rid"]
            re_cursor = g.conn.execute(
                "SELECT rid,c.cid as cid,c.name as cname,r.name as name,contact,location,star,photo_url,longitude,latitude FROM restaurant r, category c where r.cid=c.cid and r.rid=" + str(
                    rid))
            for re_result in re_cursor:
                data.append({
                    "rid": re_result["rid"],
                    "cid": re_result["cid"],
                    "name": re_result["name"].strip(),
                    "cname": re_result["cname"].strip(),
                    "contact": re_result["contact"].strip(),
                    "location": re_result["location"].strip(),
                    "star": round(re_result["star"], 2),
                    "photo_url": re_result["photo_url"].strip(),
                    "longitude": re_result["longitude"],
                    "latitude": re_result["latitude"]
                })
        cursor.close()
        return data


class CheapRecommendation(Resource):
    def get(self):
        data = []
        cursor = g.conn.execute(
            "SELECT * FROM restaurant WHERE rid IN ((SELECT re.rid FROM restaurant re WHERE star > (SELECT AVG(star) FROM restaurant)) INTERSECT(SELECT r.reid AS rid FROM recipe r GROUP BY r.reid HAVING AVG (r.price) < (SELECT AVG(price) FROM recipe)))")
        for result in cursor:
            data.append({
                "rid": result["rid"],
                "cid": result["cid"],
                "name": result["name"].strip(),
                "contact": result["contact"].strip(),
                "location": result["location"].strip(),
                "star": round(result["star"], 2),
                "photo_url": result["photo_url"].strip(),
                "longitude": result["longitude"],
                "latitude": result["latitude"]
            })
        cursor.close()
        return data


class Search(Resource):
    def get(self):
        keyword = request.args['keyword']
        data = []
        cursor = g.conn.execute(
            "SELECT * FROM restaurant WHERE lower(name) LIKE '%%" + keyword.lower() + "%%'")
        for result in cursor:
            data.append({
                "rid": result["rid"],
                "cid": result["cid"],
                "name": result["name"].strip(),
                "contact": result["contact"].strip(),
                "location": result["location"].strip(),
                "star": round(result["star"], 2),
                "photo_url": result["photo_url"].strip(),
                "longitude": result["longitude"],
                "latitude": result["latitude"]
            })
        cursor.close()
        return data


api.add_resource(RestaurantList, '/api/restaurant')
api.add_resource(Restaurant, '/api/restaurant/<rid>')
api.add_resource(Recipe, '/api/restaurant/<rid>/recipe')
api.add_resource(Review, '/api/restaurant/<rid>/review')
api.add_resource(WishList, '/api/wishlist')
api.add_resource(UserWishList, '/api/wishlist/<uid>')
api.add_resource(Category, '/api/category')
api.add_resource(FavoriteCategory, '/api/category/<uid>')
api.add_resource(Ingredient, '/api/ingredient')
api.add_resource(FavoriteIngredient, '/api/ingredient/<uid>')
api.add_resource(Recommendation, '/api/recommendation/<uid>')
api.add_resource(ReviewRecord, '/api/review/<uid>')
api.add_resource(Login, '/api/login')
api.add_resource(Register, '/api/register')
api.add_resource(Friend, '/api/friend/<uid>')
api.add_resource(CheapRecommendation, '/api/cheap-recommendation')
api.add_resource(Search, '/api/search')


@app.teardown_request
def teardown_request(exception):
    """
    At the end of the web request, this makes sure to close the database connection.
    If you don't, the database could run out of memory!
    """
    try:
        g.conn.close()
    except Exception as e:
        pass


if __name__ == "__main__":
    import click


    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True)
    @click.argument('HOST', default='0.0.0.0')
    @click.argument('PORT', default=5000, type=int)
    def run(debug, threaded, host, port):
        HOST, PORT = host, port
        print("running on %s:%d" % (HOST, PORT))
        app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


    run()
