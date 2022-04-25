CREATE OR REPLACE FUNCTION distance(l1 numeric(9,6), lt1 numeric(9,6), l2 numeric(9,6), lt2 numeric(9,6)) RETURNS numeric(9,6) $$
DECLARE
    total float = cos(radians(l1))*cos(radians(l2))*(sin(radians((lt2-lt1)/2))^2)
    value1 float = (sin(radians((l2-l1)/2)))
BEGIN
    RETURN 2*3961*asin(sqrt(value1*value1 + total))
END
$$ LANGUAGE plpgsql;