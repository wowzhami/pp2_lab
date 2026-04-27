CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p_pattern TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT user_name, phone_number 
    FROM phonebook
    WHERE user_name ILIKE '%' || p_pattern || '%'
       OR phone_number ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE user_name = p_name) THEN
        UPDATE phonebook SET phone_number = p_phone WHERE user_name = p_name;
    ELSE
        INSERT INTO phonebook (user_name, phone_number) VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT user_name, phone_number 
    FROM phonebook 
    ORDER BY user_name
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_contact_adv(p_search VARCHAR)
AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE user_name = p_search OR phone_number = p_search;
END;
$$ LANGUAGE plpgsql;