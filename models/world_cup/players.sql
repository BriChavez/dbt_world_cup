
with players as (

  select
    Player,
    Jersey_num,
    Position,
    DOB_Age,
    Caps,
    Club,
    Cup_year
  from `dbtweek.world_cup.world_cup`
  order by Cup_Year desc
)

select * from players