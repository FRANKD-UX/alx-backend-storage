-- Creates an index idx_name_first_score on the table names
-- Index on the first letter of name AND score

CREATE INDEX idx_name_first_score ON names (name(1), score);
