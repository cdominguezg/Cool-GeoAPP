\connect coolgeoapp;
CREATE TABLE "postal_code" (
  "id" integer NOT NULL,
  "code" integer NOT NULL,
  "geom" geometry NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "paystat" (
  "id" integer NOT NULL,
  "month" date NOT NULL,
  "age_range" varchar NOT NULL,
  "gender" varchar NOT NULL,
  "amount" numeric NOT NULL,
  "postal_code_id" integer NOT NULL,
  PRIMARY KEY ("id"),
  FOREIGN KEY ("postal_code_id") REFERENCES "postal_code"("id")
);