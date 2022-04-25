CREATE FUNCTION updatecheckin() RETURNS trigger as '
BEGIN
        UPDATE Business
        SET numCheckins=(SELECT COUNT(business_id) FROM CheckIn WHERE Business.business_id=CheckIn.business_id)
RETURN NEW;
END
'LANGUAGE plpgsql;

CREATE TRIGGER UpdateCheckIns
AFTER INSERT OR DELETE ON CheckIn
FOR EACH ROW
EXECUTE PROCEDURE updateCheckIn();

CREATE FUNCTION updatetips() RETURNS trigger as '
BEGIN
        UPDATE Business
        SET totalTips = (SELECT COUNT(business_id) FROM Tips WHERE Business.business_id=Tips.business_id);
        RETURN NEW;
END
'LANGUAGE plpgsql;

CREATE TRIGGER updatetips
AFTER INSERT OR DELETE ON Tips
FOR EACH ROW
EXECUTE PROCEDURE updateTips();

CREATE FUNCTION updatetipsuser() RETURNS trigger as
'
BEGIN
        UPDATE UserInfo SET tipCount = Total.t_count  FROM (SELECT user_id, COUNT(user_id)
        FROM Tips GROUP BY Tips.user_id) Total WHERE UserInfo.user_id = Total.user_id;
        RETURN NEW;
END 
'LANGUAGE plpgsql;

CREATE TRIGGER updatetipsuser
AFTER INSERT OR DELETE ON Tips
FOR EACH ROW 
EXECUTE PROCEDURE updateTipsUser();

CREATE FUNCTION updatelikes() RETURNS trigger as'
BEGIN 
        UPDATE UserInfo SET totalLikes = Totals.total_likes FROM 
        (SELECT Tips.user_id, SUM(totalLikes)) likesTotal
        FROM Tips
        GROUP BY user_id) Totals WHERE UserInfo.user_id=Totals.user_id;
        RETURN NEW;
END
'LANGUAGE plpgsql;

CREATE TRIGGER updatelikes
AFTER INSERT OR DELETE OR UPDATE ON Tips
FOR EACH ROW
EXECUTE PROCEDURE updatelikes();


