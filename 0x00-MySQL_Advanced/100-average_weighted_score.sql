-- Creates a stored procedure ComputeAverageWeightedScoreForUser that 
-- computes and stores the average weighted score for a student

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE weighted_avg_score FLOAT;
    
    -- Calculate weighted average score
    SELECT SUM(c.score * p.weight) / SUM(p.weight) INTO weighted_avg_score
    FROM corrections c
    INNER JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;
    
    -- Update user's average_score
    UPDATE users
    SET average_score = weighted_avg_score
    WHERE id = user_id;
END$$

DELIMITER ;
