CREATE SEQUENCE IF NOT EXISTS public.node_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;


CREATE TABLE IF NOT EXISTS public.database (
	node_id                 bigint NOT NULL DEFAULT nextval('public.node_seq'),
	parent_id               bigint NULL,
	"value"                 text NOT NULL,
	is_deleted              bool NOT NULL DEFAULT FALSE,
	created_at              timestamp NOT NULL DEFAULT now()::timestamp without time zone,
	updated_at              timestamp NOT NULL DEFAULT now()::timestamp without time zone,
	deleted_at              timestamp NULL,
	CONSTRAINT database_pk PRIMARY KEY (node_id)
);


INSERT INTO public.database (parent_id, "value")
VALUES (NULL, 'value_1'),
    (1, 'value_2'),
    (1, 'value_3'),
    (1, 'value_4'),
    (2, 'value_5'),
    (2, 'value_6'),
    (2, 'value_7'),
    (5, 'value_8'),
    (5, 'value_9'),
    (8, 'value_10'),
    (1, 'value_11'),
    (11, 'value_12'),
    (12, 'value_13'),
    (13, 'value_14');

