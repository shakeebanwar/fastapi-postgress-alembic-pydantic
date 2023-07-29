--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3 (Debian 15.3-1.pgdg120+1)
-- Dumped by pg_dump version 15.3 (Debian 15.3-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO "user";

--
-- Name: items; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.items (
    id integer NOT NULL,
    name character varying,
    description character varying,
    created_date timestamp with time zone DEFAULT now()
);


ALTER TABLE public.items OWNER TO "user";

--
-- Name: items_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.items_id_seq OWNER TO "user";

--
-- Name: items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.items_id_seq OWNED BY public.items.id;


--
-- Name: items id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.items ALTER COLUMN id SET DEFAULT nextval('public.items_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.alembic_version (version_num) FROM stdin;
14e88eb04eca
\.


--
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.items (id, name, description, created_date) FROM stdin;
6	iPhone 13	The latest iPhone with a powerful A15 Bionic chip.	2023-07-28 13:28:36.753802+00
7	Samsung Galaxy S21	A flagship Android smartphone with a stunning display.	2023-07-28 13:28:36.803087+00
8	Google Pixel 6	A feature-rich phone with the latest Android OS.	2023-07-28 13:28:36.819282+00
9	OnePlus 9 Pro	A high-performance phone known for its smooth experience.	2023-07-28 13:28:36.835444+00
10	Xiaomi Mi 11	A budget-friendly phone with great value for money.	2023-07-28 13:28:36.851447+00
11	Sony Xperia 1 III	A multimedia powerhouse with advanced camera features.	2023-07-28 13:28:36.867001+00
12	LG Velvet	A stylish phone with a sleek design and 5G support.	2023-07-28 13:28:36.882657+00
13	Motorola Edge Plus	A capable device with a large battery and 108MP camera.	2023-07-28 13:28:36.898776+00
14	Nokia 8.3	A durable phone with a PureDisplay and ZEISS optics.	2023-07-28 13:28:36.914213+00
15	Realme GT	A gaming-oriented phone with a Snapdragon 888 chipset.	2023-07-28 13:28:36.929636+00
\.


--
-- Name: items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.items_id_seq', 15, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: items items_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_pkey PRIMARY KEY (id);


--
-- Name: ix_items_created_date; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_items_created_date ON public.items USING btree (created_date);


--
-- Name: ix_items_description; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_items_description ON public.items USING btree (description);


--
-- Name: ix_items_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_items_id ON public.items USING btree (id);


--
-- Name: ix_items_name; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_items_name ON public.items USING btree (name);


--
-- PostgreSQL database dump complete
--

