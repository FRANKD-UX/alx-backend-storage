-- Creates a stored procedure ComputeAverageWeightedScoreForUsers that 
-- computes and stores the average weighted score for all students

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Update average_score for each user based on weighted average
    UPDATE users u
    SET average_score = (
        SELECT IFNULL(SUM(c.score * p.weight) / SUM(p.weight), 0)
        FROM corrections c
        INNER JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = u.id
    );
END$$

DELIMITER ;
