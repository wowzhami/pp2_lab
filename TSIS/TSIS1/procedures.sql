CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name VARCHAR, p_group_name VARCHAR)
AS $$
DECLARE
    v_group_id INTEGER;
BEGIN
    INSERT INTO groups (name) VALUES (p_group_name)
    ON CONFLICT (name) DO NOTHING;
    
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;

    UPDATE phonebook SET group_id = v_group_id WHERE user_name = p_contact_name;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(name VARCHAR, email_addr VARCHAR, phone_num VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT pb.user_name, pb.email, ph.phone
    FROM phonebook pb
    LEFT JOIN phones ph ON pb.id = ph.contact_id
    WHERE pb.user_name ILIKE '%' || p_query || '%'
       OR pb.email ILIKE '%' || p_query || '%'
       OR ph.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;