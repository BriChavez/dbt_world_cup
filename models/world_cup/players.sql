

with players as (

  SELECT  
    Player,
    Jersey_num,
    Position,
    DOB_Age,
    Club,
    Cup_year
  FROM `dbtweek.world_cup.world_cup`
  ORDER BY Cup_Year DESC
)

select * from players