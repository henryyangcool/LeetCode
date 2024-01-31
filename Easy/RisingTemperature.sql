SELECT a.id FROM Weather a, Weather b WHERE a.Temperature > b.Temperature AND a.recordDate = b.recordDate + INTERVAL '1 day'
