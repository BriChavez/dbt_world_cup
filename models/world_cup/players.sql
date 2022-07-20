
with players as (

  select
    Player,
    Jersey_num,
    Position,
    Age,
    Caps,
    Club,
    Cup_year
  from {{ ref('source_data') }}
  order by Cup_Year desc
)

select * from players