with player_caps as (
    select 
        Player,
        Position,
        Caps,
        Age,
        Club
    from 
        {{ ref('players') }}
    where 
        Caps > 0
    order by 
        Caps desc
)


select * from player_caps